from django.urls import path
from . import views

app_name = 'boardapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.PostDetailView, name='detail'),
    path('post_upload/', views.PostUploadView, name='upload'),
    path('<int:post_id>/comment_create/', views.CommentUploadView, name='comment_upload')
]
