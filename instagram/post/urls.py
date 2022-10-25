from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_post, name='new_post'),
    path('<int:post_id>/new_comment/', views.new_comment, name='new_comment'),
    path('<int:comment_id>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('<int:post_id>/like/', views.post_like, name='post_like'),

]
