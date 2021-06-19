from django.urls import path, include
from .import views

app_name = 'Blog_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('single_post<slug>/', views.single_post, name='single_post'),
    path('about/', views.about, name='about'),
]
