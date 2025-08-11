from .models import Profile

def profile_context(request):
    """
    Adds the profile picture URL and friends list to the context if the user is authenticated.
    """
    profile_picture_url = None
    friends             = []

    if request.user.is_authenticated:
        try:
            profile_picture_url = request.user.profile_picture.url if request.user.profile_picture else None
            friends             = request.user.friends.all()
        except Profile.DoesNotExist:
            pass

    return {
        'profile_picture_url': profile_picture_url,
        'friends'            : friends
    }

