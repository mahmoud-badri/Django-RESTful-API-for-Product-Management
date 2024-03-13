from django.urls import path, include

from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Products_serializers', viewsets_product)

urlpatterns = [
    
    
    #1.1 GET POST from rest framework function based view @api_view
    path('data/', info_Products),

    #1.2 GET PUT DELETE from rest framework function based view @api_view
    path('data/<int:id>', info_Product),
    
    
    #2.1 GET POST from rest framework class based view generics
    path('generics/', generics_list.as_view()),

    #2.2 GET PUT DELETE from rest framework class based view generics
    path('generics/<int:pk>', generics_pk.as_view()),
    
    #3 Viewsets
    path('viewsets/', include(router.urls)),
    
    path('api-auth', include('rest_framework.urls'))
] 
