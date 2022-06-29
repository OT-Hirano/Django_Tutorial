# Django ルーティング（URL）の構成
# https://docs.djangoproject.com/en/4.0/topics/http/urls/

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
