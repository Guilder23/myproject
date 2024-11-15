from django.contrib import admin

# Register your models here.
#Para que aparezac la tabla en admin django
# myapp/admin.py
from .models import UserPlainText  # Importa el modelo

# Opcional: Clase para personalizar la visualización en el admin
class UserPlainTextAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # Mostrar campos como columnas en la tabla

# Registra el modelo con la clase personalizada
admin.site.register(UserPlainText, UserPlainTextAdmin)
