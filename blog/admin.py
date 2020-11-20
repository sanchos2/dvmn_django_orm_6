from django.contrib import admin
from blog.models import Post, Tag, Comment


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author']
    list_per_page = 40


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['likes', 'tags']
    list_per_page = 40


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
