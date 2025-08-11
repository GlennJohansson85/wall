from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden

from cloudinary import CloudinaryImage
from cloudinary.uploader import upload
from django.core.exceptions import ValidationError

from .forms import PostForm, CommentForm
from .models import Post, Comment
from accounts.models import Profile


def postwall(request):
    posts_with_comments = []
    posts               = Post.objects.filter(is_published=True).order_by('-created_at')

    for post in posts:
        comments = post.comments.all()
        posts_with_comments.append({'post': post, 'comments': comments})

    context = {
        'posts_with_comments': posts_with_comments,
        'user'               : request.user,
    }
    return render(request, "postwall.html", context)



@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post      = form.save(commit=False)
            post.user = request.user

            # If there is an image uploaded
            if 'img' in request.FILES and request.FILES['img']:
                img_file = request.FILES['img']

                # Check the file size before uploading
                max_size = 13 * 1024 * 1024  # 13 MB
                if img_file.size > max_size:
                    messages.error(request, "File size exceeds the 13 MB limit.")
                    context = {'form': form}
                    return render(request, 'post.html', context)

                # Check if the uploaded file is an image (optional, but good for validation)
                if not img_file.content_type.startswith('image/'):
                    messages.error(request, "The file must be an image.")
                    context = {'form': form}
                    return render(request, 'post.html', context)

                # Upload to Cloudinary
                try:
                    upload_result = upload(img_file)

                    # Save the uploaded image URL to the post
                    post.img = upload_result['secure_url']
                except Exception as e:
                    messages.error(request, f"An error occurred during image upload: {str(e)}")
                    context = {'form': form}
                    return render(request, 'post.html', context)
            else:
                # If no image uploaded, set default image
                post.img = 'uploads/no-img.png'  # Path to your default image

            # Save the post to the database
            post.save()
            messages.success(request, "Your post was created successfully!")
            return redirect('postwall')

        else:
            # Handle form errors if the form is not valid
            if not form.cleaned_data.get('title') and not form.cleaned_data.get('content'):
                messages.error(request, "Title and Content are required.")
            else:
                if form.errors.get('title'):
                    messages.error(request, "Title is required.")
                if form.errors.get('content'):
                    messages.error(request, "Content is required.")

            context = {'form': form}
            return render(request, 'post.html', context)

    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'post.html', context)


def post_detail(request, post_id):
    post     = get_object_or_404(Post, id=post_id)
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
        'post'        : post,
        'comments'    : comments,
        'comment_form': comment_form,
        'user'        : request.user,
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

            # Ensure a clean URL with a single `post_id` parameter
            return redirect(f'{request.META["HTTP_REFERER"].split("?")[0]}?post_id={post_id}')
        else:
            messages.error(request, 'Comment cannot be empty.')

    return redirect('postwall.html')


@login_required
def delete_post_confirmation(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect('postwall.html')

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
    posts   = []

    if keyword:
        posts = Post.objects.filter(title__icontains=keyword)
    return render(request, 'search_results.html', {'posts': posts})


def search_suggestions(request):
    keyword     = request.GET.get('keyword', '')
    suggestions = []

    if keyword:
        posts       = Post.objects.filter(title__icontains=keyword)[:10]
        suggestions = [{'id': post.id, 'title': post.title} for post in posts]
    return JsonResponse({'suggestions': suggestions})
