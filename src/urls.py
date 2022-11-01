from django.contrib import admin
from django.urls import path, include
from news_portal.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('news-portal/', include('news_portal.urls')),
]
