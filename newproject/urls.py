"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from blog.views import home, post_detail, all_blogs, bloggers, user_detail

urlpatterns = [
    # An index page describing the site.
    path('',home, name = 'homepage'),
    path('blog/',home, name = 'homepage'),
    # admin site /admin/
    path('admin/', admin.site.urls),
    # list of all blogs
    path('blog/blogs/',all_blogs,name='all_blogs'),
    # list of all the bloggers
    path('blog/bloggers/',bloggers, name='bloggers'),
    # blog/<blog-id>
    path('blog/<slug:slug>/',post_detail, name = 'post_detail'),
    # blog/bloggers/<str:username>
    path('blog/bloggers/<str:username>/',user_detail, name = 'user_detail')
]
