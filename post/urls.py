from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<int:id>/', views.detail_view, name='detail'),
    path('addpost/', views.add_post, name='addpost'),
    path('edit/<int:pk>/', views.PostUpdateView.as_view(), name='edit'),
]