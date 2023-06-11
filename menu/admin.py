from django.contrib import admin
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'title', 'description',
        'weight', 'price', 'discount_price',
        'photo_url', 'add_date', 'active')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    list_editable = ('active',)
    list_filter = ('active',)


admin.site.register(Menu, MenuAdmin)
