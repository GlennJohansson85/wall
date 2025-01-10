from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden

from cloudinary import CloudinaryImage
from cloudinary.uploader import upload

from .forms import PostForm, CommentForm
from .models import Post, Comment
from accounts.models import Profile


def postwall(request):
    posts_with_comments = []
    posts = Post.objects.filter(is_published=True).order_by('-created_at')

    for post in posts:
        comments = post.comments.all()
        posts_with_comments.append({'post': post, 'comments': comments})

    context = {
        'posts_with_comments': posts_with_comments,
        'user': request.user,
    }
    return render(request, "postwall.html", context)


@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        # Check if form is valid
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            # Handle the image upload with Cloudinary transformation
            if post.img:
                file = post.img

                # Apply transformation if the file is too large
                max_size = 13 * 1024 * 1024  # 13 MB
                if file.size > max_size:
                    transformed_image = upload(file, transformation=[
                        {'width': 1000, 'crop': 'scale'},
                        {'quality': 'auto'},
                        {'fetch_format': 'auto'}
                    ])
                    post.img = transformed_image['secure_url']
                else:
                    # If the file is small enough, upload it without transformation
                    transformed_image = upload(file)
                    post.img = transformed_image['secure_url']

            # If no image is uploaded, set the default image
            if not post.img:
                post.img = 'uploads/no-img.png'

            # Save the post to the database
            post.save()
            messages.success(request, "Your post was created successfully!")
            return redirect('postwall')

        else:
            # Handle form errors
            if not form.cleaned_data.get('title') and not form.cleaned_data.get('content'):
                messages.error(request, "Title and Content required")
            else:
                if form.errors.get('title'):
                    messages.error(request, "Title required")
                if form.errors.get('content'):
                    messages.error(request, "Content required")

            context = {'form': form}
            return render(request, 'post.html', context)

    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'post.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            profile = get_object_or_404(Profile, user=request.user)
            comment_form.save(user=profile, post=post)
            return redirect('postwall')

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user': request.user,
    }

    return render(request, 'post_detail.html', context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')

        if comment_text:
            Comment.objects.create(
                post = post,
                user = request.user,
                text = comment_text
            )
            messages.success(request, 'Comment added successfully!')
            return redirect(f"{reverse('postwall')}?post_id={post.id}")

        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('postwall')


@login_required
def delete_post_confirmation(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect('postwall')

    context = {'post': post}
    return render(request, 'delete_post_confirmation.html', context)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user == post.user or request.user.is_admin:
        post.delete()
        messages.success(request, 'The post has been successfully deleted.')
        return redirect('postwall')

    else:
        return HttpResponseForbidden("You are not authorized to delete this post.")


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user or request.user.is_admin:
        comment.delete()
        messages.success(request, 'The comment has been successfully deleted.')
        return redirect('post_detail', post_id=comment.post.id)

    else:
        return HttpResponseForbidden("You are not authorized to delete this comment.")


def search(request):
    keyword = request.GET.get('keyword', '')
    posts = []

    if keyword:
        posts = Post.objects.filter(title__icontains=keyword)
    return render(request, 'search_results.html', {'posts': posts})


def search_suggestions(request):
    keyword = request.GET.get('keyword', '')
    suggestions = []

    if keyword:
        posts = Post.objects.filter(title__icontains=keyword)[:10]
        suggestions = [{'id': post.id, 'title': post.title} for post in posts]
    return JsonResponse({'suggestions': suggestions})
