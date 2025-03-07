"""
URL configuration for NCBCNet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path,include,re_path
from server import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
# import notifications.urls

urlpatterns = [
    path('favicon.ico', serve, {'path': 'server/favicon.ico'}),
    path('admin/', admin.site.urls),
    path('',views.index),
    path('server/', include('server.urls', namespace='server')),
    path('article/',include('article.urls',namespace='article')),
    path('usermanage/',include('usermanage.urls',namespace='usermanage')),
    path('comment/', include('comment.urls', namespace='comment')),
    path(r'mdeditor/', include('mdeditor.urls')),
    # path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)