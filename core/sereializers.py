
from rest_framework import serializers
from .models import Profession
from .models import Customer,DataSheet,Document


class customerSerial(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name','address','professions','data_sheet')

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profession
        fields =('id','description')
class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=DataSheet
        fields =('id','description','historical_data')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields =('id','dtype','doc_number','customer')
