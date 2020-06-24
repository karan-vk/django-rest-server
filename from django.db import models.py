from django.db import models

class Profession(models.Model):
    description = models.CharField(max_length=50)

class DataSheet(models.Model):
    description = models.CharField(max_length=50)
    historical_data=models.TextField()

    

class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    professions = models.ManyToManyField(Profession)
    data_sheet= models.OneToOneField(DataSheet,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Document(models.Model):
    PP='PP'
    ID='ID'
    OT='OT'

    DOC_TYPES=(
        (PP,'Passport'),
        (ID,'Idrntity card'),
        (OT,'Others')
    )

    dtype= models.CharField(choices=DOC_TYPES,max_length=2)
    doc_number= models.CharField(max_length=50)
    def __str__(self):
        return self.doc_number
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE)


# Create your models here.
