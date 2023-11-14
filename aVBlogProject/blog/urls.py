from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
    path('bakim/', views.bakim, name='bakim' ),
    path('',views.post_list,name="post_list"),
    path('<slug:post>/',views.post_detail,name="post_detail"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),


]
