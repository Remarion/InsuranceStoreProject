from django.db import models

'''Зона реєстрації авто'''
class Zone(models.Model):
    zoneName = models.CharField(max_length=50)

    def __str__(self):
        return self.zoneName

'''Населений пункт'''
class Settlement(models.Model):
    settlementName = models.CharField(max_length=50)
    settlementRegion = models.CharField(max_length=50)
    settlementZone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    settlementMTSBUCodeBool = models.BooleanField()
    settlementMTSBUCode = models.CharField(max_length=10)

    def __str__(self):
        return self.settlementName + ", " + self.settlementRegion

'''легковий, вантажний, мотоцикл....'''
class CarTypeSimple (models.Model):
    carTypeSimple = models.CharField(max_length=50)

    def __str__(self):
        return self.carTypeSimple

'''Вантажопідйомність, об'єм двигуна'''
class CarTypeLabel (models.Model):
    carTypeSimple = models.ForeignKey(CarTypeSimple, on_delete=models.CASCADE)
    carTypeLabel = models.CharField(max_length=20)

    def __str__(self):
        return self.carTypeLabel

'''Тип авто відповідно до довідника МТСБУ'''
class CarTypeMTSBU (models.Model):
    carTypeSimple = models.ForeignKey(CarTypeSimple, on_delete=models.CASCADE)
    carTypeLabel = models.ForeignKey(CarTypeLabel, on_delete=models.CASCADE)
    carTypeKind = models.CharField(max_length=30)
    carTypeMTSBU = models.CharField(max_length=10)

    def __str__(self):
        return self.carTypeMTSBU + "_" + self.carTypeSimple.carTypeSimple + "_" + self.carTypeKind

'''Марка авто'''
class CarBrand(models.Model):
    brandName = models.CharField(max_length=50)

    def __str__(self):
        return self.brandName

'''Модель авто'''
class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    modelName = models.CharField(max_length=50)

    def __str__(self):
        return self.modelName

'''страхова компанія партнер'''
class InsuranceCompany (models.Model):
    insuranceCompanyName = models.CharField(max_length=50)
    insuranceCompanyLogo = models.ImageField(upload_to='imgs')
    insuranceCompanyURL = models.URLField()

    def __str__(self):
        return self.insuranceCompanyName

'''Данні для розрахунку'''
class CalculationOCV(models.Model):
    setlCalc = models.ForeignKey(Settlement, on_delete=models.CASCADE)
    catTypeSimpleCalc = models.ForeignKey(CarTypeSimple, on_delete=models.CASCADE)
    carTypeLabelCalc = models.ForeignKey(CarTypeLabel, on_delete=models.CASCADE)
    carTypeMTSBUCalc = models.ForeignKey(CarTypeMTSBU, on_delete=models.CASCADE)

    def __str__(self):
        return self.setlCalc.settlementName + "" + self.catTypeMTSBUCalc.carTypeMTSBU

'''Ціна в розрізі страхових Компаній'''
class PriceOCV (models.Model):
    insuranceCompany = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    calculation = models.ForeignKey(CalculationOCV, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.insuranceCompany.insuranceCompanyName + "_" + self.price


'''Договір ОЦВ'''
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







