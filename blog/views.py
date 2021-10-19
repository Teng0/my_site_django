from django.http.response import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from datetime import date

from django.views import View
from .models import Post
from django.views.generic import ListView,DetailView

from blog import models
from .forms import CommentForm
# Create your views here.

all_posts = [
    {
        'slug':"hike-in-the-mountains",
        'image':"mountains.jpg",
        'author':'Tengo',
        'date':date(2021,10,1),
        'title':'Mountain Hicking',
        'excerpt':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum recusandae eum, cumque cupiditate, officia ab minus corrupti tempore debitis minima temporibus, tempora voluptatum optio nisi soluta dolore placeat nihil sunt.',
        'content':"""
                     Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                     Cum recusandae eum, cumque cupiditate, officia ab minus corrupti tempore debitis 
                     minima temporibus, tempora voluptatum optio nisi soluta dolore placeat nihil sunt.
                    """

    },
    {
        'slug':"programing-is-fan",
        'image':"coding.jpg",
        'author':'Tengo',
        'date':date(2021,9,1),
        'title':'programing',
        'excerpt':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum recusandae eum, cumque cupiditate, officia ab minus corrupti tempore debitis minima temporibus, tempora voluptatum optio nisi soluta dolore placeat nihil sunt.',
        'content':"""
                     Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                     Cum recusandae eum, cumque cupiditate, officia ab minus corrupti tempore debitis 
                     minima temporibus, tempora voluptatum optio nisi soluta dolore placeat nihil sunt.
                    """

    },
    {
        'slug':"woods-are-great",
        'image':"woods.jpg",
        'author':'Tengo',
        'date':date(2021,8,1),
        'title':'Woods',
        'excerpt':' Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum recusandae eum, cumque cupiditate, officia ab minus corrupti tempore debitis minima temporibus, tempora voluptatum optio nisi soluta dolore placeat nihil sunt.',
        'content':"""
                     Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                     Cum recusandae eum, cumque cupiditate, officia ab minus corrupti tempore debitis 
                     minima temporibus, tempora voluptatum optio nisi soluta dolore placeat nihil sunt.
                    """

    }
]
class SartPageView(ListView):
    template_name = "blog\index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


    def get_queryset(self):
        query = super().get_queryset()
        data = query[:3]
        return data




class AllPostsView(ListView):
    model = Post
    template_name = "blog\index.html"
    context_object_name = "posts"

# class SinglePostView(DetailView):
#     model = Post
#     template_name = "blog\post_details.html"
#     context_object_name = "post"
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['post_tags'] = self.object.tag.all()
#         form = CommentForm()
#         context["comment_form"] = CommentForm()
#         print(form)
#         print("works")

#         return context
class SinglePostView(View):
    def is_saved_for_later(self,request,post_id):
       
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "is_saved_for_later":self.is_saved_for_later(request,post.id)
            }
        return render(request,"blog\post_details.html",context)

class ReadLaterView(View):
    def get(self,request):
        print("works")
        return HttpResponseRedirect("/")

    def post(self,request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts
            
        return HttpResponseRedirect("/")
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context= {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request,"blog\stored_posts.html",context)
       

   

def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            post =Post.objects.get(slug=slug)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog_post_details", args=[slug]))
        
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "post_tags":post.tag.all(),
            "comment_form":comment_form,
            "comments":post.comments.all()
            }
        return render(request,"blog\post_details.html",context)

def get_date(post):
    return post['date']

def index(request):

    #sorted_posts=sorted(all_posts, key=get_date)

    latest_post= Post.objects.all().order_by('-date')[:3]
    return render(request,"blog\index.html",{'posts':latest_post})

def posts(request):
     all_posts = Post.objects.all().order_by("-date")
     return render(request,'blog\posts_all.html',{"all_posts":all_posts})

def post_details(request,slug):
    #post = next(post for post in all_posts if post['slug'] == slug)
    #post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post,slug=slug)
    return render(request,'blog\post_details.html',{'post':post,'post_tags':post.tag.all()})