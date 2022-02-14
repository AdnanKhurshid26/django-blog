from django.contrib import admin
from .models import Post, Tag, Author
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'last_modified','author','tag')
    list_display = ('title', 'created_on', 'last_modified','author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)