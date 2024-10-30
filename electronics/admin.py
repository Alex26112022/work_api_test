from django.contrib import admin

from electronics.models import Product, Element


@admin.action(description="Очистить задолженность перед поставщиком")
def delete_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


admin.site.register(Product)


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'supplier', 'debt', 'created_at')
    list_display_links = ('title', 'supplier', 'debt', 'created_at')
    fields = (
        'title', 'email', 'country', 'city', 'street', 'house_number',
        'product',
        'supplier', 'debt')
    list_filter = ('country',)
    actions = [delete_debt]
