from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

    def total_cost(self, obj):
        return OrderItem.get_cost(obj)
    readonly_fields = ("total_cost",)

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city', 'paid', 'phone',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid',]
    inlines = [OrderItemInline]

    def total_cost(self, obj):
        return Order.get_total_cost(obj)
    readonly_fields = ("total_cost",)


admin.site.register(Order, OrderAdmin)
