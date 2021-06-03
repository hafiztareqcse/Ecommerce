from django.contrib import admin
from OrderApp.models import Cart, Order, OrderProduct


# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']


admin.site.register(Cart, CartAdmin)


class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'status', 'transaction_id']
    list_filter = ['status']
    readonly_fields = ['user', 'first_name', 'last_name', 'phone', 'address', 'city', 'total', 'ip', 'transaction_id',
                       'transaction_image']
    can_delete = False
    inlines = [OrderProductInLine]


admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register(OrderProduct, OrderProductAdmin)
