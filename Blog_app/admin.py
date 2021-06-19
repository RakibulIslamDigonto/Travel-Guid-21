from django.contrib import admin
from django.contrib import admin
from .models import Blog, Comment, User
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class BlogAdmin(SummernoteModelAdmin):

    list_display = [
        'title',
        'thumbnail',
        'country',
        'short_discription',
        'discription'
    ]
    summernote_fields = ('discription',)


admin.site.register(Blog, BlogAdmin)


class UserAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'email',
        'password',
    ]


admin.site.register(User, UserAdmin)


class CommentAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'body',
    ]


admin.site.register(Comment, CommentAdmin)
