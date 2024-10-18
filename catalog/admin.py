from django.contrib import admin
from .models import Category,Post,Images


class ImageAdmin(admin.StackedInline):
    model = Images

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Post


admin.site.register(Category)
admin.site.register(Post, PostAdmin)