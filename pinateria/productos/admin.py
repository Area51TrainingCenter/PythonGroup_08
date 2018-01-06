from django.contrib import admin

from productos.models import Producto, Categoria


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('personaje', 'nombre_comercial', 'precio_dos_decimales',)
    list_display_links = list_display
    list_filter = ('precio',)
    search_fields = ('personaje', 'nombre_comercial',)

    def precio_dos_decimales(self, obj):
        return '{:.2f}'.format(obj.precio)
    precio_dos_decimales.short_description = 'precio'


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)

# from django.contrib.auth.models import Group, User
# admin.site.unregister(Group)
# admin.site.unregister(User)
#
#
# class UserAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(User)
