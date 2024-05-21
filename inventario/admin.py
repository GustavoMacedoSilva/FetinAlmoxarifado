from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Componente)
admin.site.register(Equipamento)
admin.site.register(Emprestimo_has_components)