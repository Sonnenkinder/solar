from django.urls import path
from .views import AdressHome
from .views import AdressCreate
from .views import AdressDetail
from .views import AdressUpdate
from .views import AdressDelete
from .views import AdressLauf
from .views import AdressBer
from .views import AdressKal

from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
     path('', AdressHome.as_view(), name='adress_start'),
     path('neu/', AdressCreate.as_view(), name='neue_adresse'),
     path('<int:pk>/', AdressDetail.as_view(), name='adress_detail'),
     path('<int:pk>/update/', AdressUpdate.as_view(), name='adress_update'),
     path('<int:pk>/delete/', AdressDelete.as_view(), name='adress_delete'),
     path('<int:pk>/lauf/', AdressLauf.as_view(), name='adress_lauf'),
     path('<int:pk>/ber/', AdressBer.as_view(), name='adress_ber'),
     path('<int:pk>/kal/', AdressKal.as_view(), name='adress_kal'),
] 

urlpatterns+= staticfiles_urlpatterns()



