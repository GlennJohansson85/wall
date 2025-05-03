# accounts urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('reset_password/', views.request_password_reset, name='request_password_reset'),
    path('reset/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('create_new_password/<uidb64>/<token>/', views.create_new_password, name='create_new_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/<int:user_id>/', views.profile_page, name='profile_page'),
    path('friends/', views.friends, name='friends'),
    path('send-request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept-request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('decline-request/<int:request_id>/', views.decline_friend_request, name='decline_friend_request'),
    path('remove-friend/<int:user_id>/', views.remove_friend, name='remove_friend'),
]
