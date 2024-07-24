from django.urls import path
from rest_framework import routers
from . import views
from .views import BreedDetail, BreedList

router = routers.DefaultRouter()
router.register(r'breeds', BreedDetail, basename='breed-detail')
router.register(r'breeds', BreedList, basename='breed-list')

urlpatterns = [
    path('dogs/', views.DogDetailList.as_view()),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),

]

urlpatterns += router.urls
