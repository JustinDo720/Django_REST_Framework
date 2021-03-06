from django.urls import path, include
from . import views
from rest_framework import routers
from .views import DogViewSet, ProgrammingLanguageViewSet
from .models import Dog, ProgrammingLanguage

router = routers.DefaultRouter()
router.register('Dog', DogViewSet)
router.register('ProgrammingLanguage', ProgrammingLanguageViewSet)

urlpatterns = [
    path('rest_api/', include(router.urls)),
    path('', views.index, name='index')
]
