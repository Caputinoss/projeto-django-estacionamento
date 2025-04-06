from django.contrib import admin
from veichles.models import Vehicle, VehicleType
# Register your models here.


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

    list_filter = ('name',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'license_plate',
        'brand',
        'model',
        'color'
    )
    search_fields = ('license_plate', 'model',)
    list_filter = ('vehicle_type',)
