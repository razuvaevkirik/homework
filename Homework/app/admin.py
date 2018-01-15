from django.contrib import admin
from app.models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id_order']
    list_filter = ['id_comp']


class ComuterAdmin(admin.ModelAdmin):
    list_filter = ['company_computer']
    search_fields = ['name_computer', 'company_computer', 'model_computer']


admin.site.register(Order, OrderAdmin)
admin.site.register(Computer, ComuterAdmin)
admin.site.site_header = 'Django Администрирование'
admin.site.index_title = 'Администрирование'