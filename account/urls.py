from django.urls import path

from . import views
urlpatterns = [
    # path('login/', views.user_login, name='login')
    path('', views.home, name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutVieew.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),


]
