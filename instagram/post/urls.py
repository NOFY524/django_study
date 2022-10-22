from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_post, name='new_post'),
    path('<int:post_id>/new_comment/', views.new_comment, name='new_comment')
]