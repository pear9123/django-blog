from django.contrib import admin
from .models import Post,PostImage,Comment

# Register your models here.
#admin.site.register(Post)
class PropertyImageInline(admin.TabularInline):
    model = PostImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]

admin.site.register(Post, PropertyAdmin)
admin.site.register(Comment)
