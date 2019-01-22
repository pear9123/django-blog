from django.contrib import admin
from .models import Post,PostImage

# Register your models here.
#admin.site.register(Post)
class PropertyImageInline(admin.TabularInline):
    model = PostImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]

admin.site.register(Post, PropertyAdmin)
