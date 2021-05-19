#DJANGO
from django.contrib import admin
#models
from posts.models import Post
# Register your models here.

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts admin """
    list_display = ('id','user','title','photo','created')
    list_editable= ('title',)
    search_fields = ('user','user__username','title')
    list_filter = ('created', 'user__username')