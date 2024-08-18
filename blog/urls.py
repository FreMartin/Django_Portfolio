from django.urls import path
from .views import render_posts, post_detail

app_name = 'blog'  #Esta variable referencia al conjunto de urls que contiene esta aplicacion

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail')
]
