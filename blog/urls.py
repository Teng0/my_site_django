
from django.urls.conf import path
from . import views


urlpatterns = [
   # path("",views.index,name="blog_index"),
    path("",views.SartPageView.as_view(),name="blog_index"),
   # path("posts",views.posts,name="blog_posts"),
    path("posts",views.AllPostsView.as_view(),name="blog_posts"),
    path("post/<slug:slug>",views.SinglePostView.as_view(),name="blog_post_details"),
    path("read_later",views.ReadLaterView.as_view(),name="read_later"),
]
