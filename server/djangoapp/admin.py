from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel


# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'carmake', 'year', 'type')
    list_filter = ('carmake', 'year', 'type')
    search_fields = ('name', 'type')
    ordering = ('carmake', 'name')
    inlines = [
        CarModelInline,
    ]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [
        CarModelInline,
    ]

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)