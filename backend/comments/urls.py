from django.urls import path
from comments import views

urlpatterns = [
    path('', views.new_comment),
    path('<str:id>/', views.get_all_comment),
    path('like_status/<str:id>/', views.likes)
]