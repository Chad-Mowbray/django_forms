from django.urls import path
from .views import all_ads, create_ad

urlpatterns = [

  path('', all_ads, name="all_ads"),
  path('new/', create_ad, name="create_ad")
]