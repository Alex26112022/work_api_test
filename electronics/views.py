from rest_framework.generics import CreateAPIView, ListAPIView, \
    RetrieveAPIView, UpdateAPIView, DestroyAPIView

from electronics.models import Element
from electronics.serializers import ElementSerializer, ElementCreateSerializer, \
    ElementUpdateSerializer


class ElementCreateApiView(CreateAPIView):
    """ Создает новый объект сети. """
    queryset = Element.objects.all()
    serializer_class = ElementCreateSerializer


class ElementListApiView(ListAPIView):
    """ Отображает все объекты сети. """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class ElementRetrieveApiView(RetrieveAPIView):
    """ Отображает объект сети. """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class ElementUpdateApiView(UpdateAPIView):
    """ Редактирует объект сети. """
    queryset = Element.objects.all()
    serializer_class = ElementUpdateSerializer


class ElementDestroyApiView(DestroyAPIView):
    """ Удаляет объект сети. """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
