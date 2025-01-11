from .models import Profile


def profile_context(request):
    """
    Adds the profile picture URL to the request context if the user is authenticated.
    Returns None if the user has no profile picture or the profile doesn't exist.
    """
    profile_picture_url = None
    if request.user.is_authenticated:
        try:
            profile_picture_url = request.user.profile_picture.url if request.user.profile_picture else None
        except Profile.DoesNotExist:
            pass
    return {'profile_picture_url': profile_picture_url}