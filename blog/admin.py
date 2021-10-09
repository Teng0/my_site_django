from django.contrib import admin

# Register your models here.

from .models import Post,Author,Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":('title',),}
    list_filter=('title','date',"tag","author", )
    list_display=('title','author','date',)

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
