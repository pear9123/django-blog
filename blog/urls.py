"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from .views import *
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('blog/', PostLV.as_view(), name='list'),
    path('blog/post/', PostLV.as_view(), name='list'),
    path('blog/post/<int:post_pk>', post_detail, name='detail'),

    # Comment
    path('<int:post_pk>/comment/create/', views.comment_create, name='comment_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
