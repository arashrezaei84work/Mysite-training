from django.urls import path
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
]
