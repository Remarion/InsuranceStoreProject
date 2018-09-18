from django.contrib import admin
from .models import Zone, Settlement, CarType, CarBrand, CarModel, ContractOCV

admin.site.register(Zone)
admin.site.register(Settlement)
admin.site.register(CarType)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(ContractOCV)