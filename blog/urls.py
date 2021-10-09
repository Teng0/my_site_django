
from django.urls.conf import path
from . import views


urlpatterns = [
    path("",views.index,name="blog_index"),
    path("posts",views.posts,name="blog_posts"),
    path("post/<slug:slug>",views.post_details,name="blog_post_details"),
]
