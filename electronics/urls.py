from django.urls import path

from electronics.apps import ElectronicsConfig
from electronics.views import ElementListApiView, ElementRetrieveApiView, \
    ElementCreateApiView, ElementUpdateApiView, ElementDestroyApiView

app_name = ElectronicsConfig.name

urlpatterns = [
    path('elements/', ElementListApiView.as_view(), name='elements_list'),
    path('element/<int:pk>/', ElementRetrieveApiView.as_view(),
         name='element_detail'),
    path('element/create/', ElementCreateApiView.as_view(),
         name='element_create'),
    path('element/<int:pk>/update/', ElementUpdateApiView.as_view(),
         name='element_update'),
    path('element/<int:pk>/delete/', ElementDestroyApiView.as_view(),
         name='element_delete'),
]
