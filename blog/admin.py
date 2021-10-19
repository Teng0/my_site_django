from django.contrib import admin

# Register your models here.

from .models import Comment, Post,Author,Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":('title',),}
    list_filter=('title','date',"tag","author", )
    list_display=('title','author','date',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('user_name','post')



admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
