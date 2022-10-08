from django.urls import path
from . import views

app_name = 'boardapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.PostDetailView, name='detail'),
    path('post_upload/', views.PostUploadView, name='upload'),
    path('<int:post_id>/comment_create/', views.CommentUploadView, name='comment_upload'),
    path('<int:post_id>/delete/', views.PostDeleteView, name='post_delete'),
    path('<int:post_id>/<int:comment_id>/delete/', views.CommentDeleteView, name='comment_delete'),
    path('<int:post_id>/like/', views.PostLikeView, name='post_like'),
    path('<int:post_id>/<int:comment_id>/like', views.CommentLikeView, name='comment_like')
]
