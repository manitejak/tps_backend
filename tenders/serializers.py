from rest_framework import serializers
from .models import Tender, AccountList, State, CityList, Brand, ContractDuration, Month, Distributor,TenderB,GraphList

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountList
        fields = ['id','name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityList
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ContractDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractDuration
        fields = '__all__'

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ['tender_name', 'quantity', 'price_a']

class TenderBSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderB
        fields = ['tender_name','quantity','price_b']


class GraphListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphList
        fields = '__all__'
