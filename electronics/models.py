from django.db import models

options = {'blank': True, 'null': True}


class Product(models.Model):
    """ Модель продукта. """
    title = models.CharField(max_length=100, verbose_name='Название',
                             **options)
    model_name = models.CharField(max_length=100, verbose_name='Модель',
                                  **options)
    launch_date = models.DateField(verbose_name='Дата выхода на рынок',
                                   **options)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Element(models.Model):
    """ Модель звеньев сети. """
    title = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=100, verbose_name='E-mail', **options)
    country = models.CharField(max_length=100, verbose_name='Страна',
                               **options)
    city = models.CharField(max_length=100, verbose_name='Город', **options)
    street = models.CharField(max_length=100, verbose_name='Улица', **options)
    house_number = models.CharField(max_length=10, verbose_name='Номер дома',
                                    **options)
    product = models.ManyToManyField(Product, related_name='element',
                                     verbose_name='Продукты')
    supplier = models.ForeignKey('Element', on_delete=models.SET_NULL,
                                 related_name='element',
                                 verbose_name='Поставщик', **options)
    debt = models.DecimalField(max_digits=12, decimal_places=2,
                               verbose_name='Задолженность',
                               default=0)
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name='Дата создания', **options)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент сети'
        verbose_name_plural = 'Элементы сети'
