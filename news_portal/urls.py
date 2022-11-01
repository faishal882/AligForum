from django.urls import path

from .views import home_view

app_name = "news_portal"

urlpatterns = [
    path('', home_view),
]
