from django.contrib import admin
from django.urls import path
from main.views import (home, detail, posts, create_post, latest_posts, 
    search_result)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug>/', detail, name='detail'),
    path('admin/', admin.site.urls),
    path("posts/<slug>/", posts, name="posts"),
    path('account/', include('register.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('create_post', create_post, name='create_post'),
    path('latest_posts', latest_posts, name='latest_posts'),
    path('search', search_result, name='search_result'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
