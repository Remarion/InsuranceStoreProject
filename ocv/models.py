from django.db import models

class Zone(models.Model):
    zoneName = models.CharField(max_length=50)

    def __str__(self):
        return self.zoneName

class Settlement(models.Model):
    settlementName = models.CharField(max_length=50)
    settlementRegion = models.CharField(max_length=50)
    settlementZone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    settlementMTSBUCodeBool = models.BooleanField()
    settlementMTSBUCode = models.CharField(max_length=10)

    def __str__(self):
        return self.settlementName + ", " + self.settlementRegion

class CarType(models.Model):
    carType = models.CharField(max_length=50)

    def __str__(self):
        return self.carType

class CarBrand(models.Model):
    brandName = models.CharField(max_length=50)

    def __str__(self):
        return self.modelsName

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    modelName = models.CharField(max_length=50)

    def __str__(self):
        return self.modelName

class CalculationOCV(models.Model):
    setlCalc = models.ForeignKey(Settlement, models.CASCADE)
    catTypeCalc = models.ForeignKey(CarType, models.CASCADE)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.setlCalc.settlementName + "" + self.catTypeCalc.carType + " " + self.price



class ContractOCV(models.Model):
    calc = models.OneToOneField(CalculationOCV, on_delete=models.CASCADE)
    klientName = models.CharField(max_length=70)
    klientAdress = models.CharField(max_length=200)
    objectBrand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    objectModel = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    objectRegNumber = models.CharField(max_length=10)
    objectVIN = models.CharField(max_length=17)
    contractBeginDate = models.DateTimeField()
    contractEndDate = models.DateTimeField()
    contractRegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.klientName + " " + self.objectBrand + " " + self.objectModel + " " + self.objectRegNumber







