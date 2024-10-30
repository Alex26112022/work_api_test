from rest_framework.serializers import ModelSerializer

from electronics.models import Element


class ElementSerializer(ModelSerializer):
    """ Сериализатор для объекта сети. """

    class Meta:
        model = Element
        fields = '__all__'


class ElementCreateSerializer(ModelSerializer):
    """ Сериализатор для создания объекта сети. """

    class Meta:
        model = Element
        fields = (
            'title', 'email', 'country', 'city', 'street', 'house_number',
            'product', 'supplier', 'debt')


class ElementUpdateSerializer(ModelSerializer):
    """ Сериализатор для редактирования объекта сети. """

    class Meta:
        model = Element
        fields = (
            'title', 'email', 'country', 'city', 'street', 'house_number',
            'product', 'supplier')
