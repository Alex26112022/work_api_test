from django.contrib import admin
from django.urls import reverse

from electronics.models import Product, Element


@admin.action(description="Очистить задолженность перед поставщиком")
def delete_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


admin.site.register(Product)


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'supplier', 'debt', 'created_at')
    list_display_links = ('title', 'supplier', 'debt', 'created_at')
    fields = (
        'title', 'email', 'country', 'city', 'street', 'house_number',
        'product',
        'supplier', 'debt', 'supplier_link')
    list_filter = ('city',)
    actions = [delete_debt]
    readonly_fields = ('supplier_link',)

    # inlines = [ElementInline]
    def supplier_link(self, obj):
        from django.utils.html import format_html
        if obj.supplier:
            return format_html(u'<a href="{0}">{1}</a>'.format(
                reverse('admin:electronics_element_change',
                        args=(obj.supplier.pk,)),
                obj.supplier))
        else:
            return 'Нет поставщика!'
