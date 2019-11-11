from django.contrib import admin
from .models import Add
from .models import LOGIN

# Register your models here.
admin.site.register(LOGIN)


@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    list_display = ['id', 'foodName', 'taste', 'GPS', 'pic']
    list_display_links = ['id', 'foodName', 'taste', 'GPS']
