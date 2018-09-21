from django.contrib import admin
from .models import Zone, Settlement, CarTypeSimple, CarTypeLabel, CarTypeMTSBU, CarBrand, CarModel, ContractOCV, CalculationOCV, InsuranceCompany, PriceOCV

admin.site.register(Zone)
admin.site.register(Settlement)
admin.site.register(CarTypeSimple)
admin.site.register(CarTypeLabel)
admin.site.register(CarTypeMTSBU)
admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(ContractOCV)
admin.site.register(CalculationOCV)
admin.site.register(InsuranceCompany)
admin.site.register(PriceOCV)

