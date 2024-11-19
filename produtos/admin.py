from django.contrib import admin

# shop/admin.py
from .models import Product

admin.site.register(Product)



from .models import Avaliacao


class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'usuario', 'nota', 'comentario', 'data']

admin.site.register(Avaliacao, AvaliacaoAdmin)


