from django.urls import path

from . import views
urlpatterns = [
    # path('login/', views.user_login, name='login')
    path('', views.home, name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutVieew.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change-password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('change-password/done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('reset-password/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done', views.UserPasswordResetView.as_view(), name='password_reset_done'),
    path('reset-password/', views.UserPasswordResetView.as_view(), name='password_reset_confirm'),
    path('reset-password/<uidb64>/<token>/', views.UserPasswordResetView.as_view(), name='password_reset_complete'),



]
