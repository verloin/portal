from django.contrib.auth import views
from django.urls import path
from .views import SignUpView, profile, ChangePasswordView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
