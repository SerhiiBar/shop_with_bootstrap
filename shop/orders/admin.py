from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

    def total_cost(self, obj):
        return float(str(obj.price)) * obj.quantity
    readonly_fields = ("total_cost",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city', 'paid', 'phone',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid',]
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
