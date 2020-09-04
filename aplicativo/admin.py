from django.contrib import admin
from .models import Relatorio


class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'sessp', 'patrimonio', 'usuario')
    list_display_links = ('sessp', 'id')


admin.site.register(Relatorio, RelatorioAdmin)
# Register your models here.