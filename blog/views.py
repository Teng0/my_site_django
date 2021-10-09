from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import Post
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