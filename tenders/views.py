from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Tender, AccountList, State, CityList, Brand, ContractDuration, Month, Distributor,TenderB,GraphList
from .serializers import (
    TenderSerializer, AccountSerializer, StateSerializer, CitySerializer,
    BrandSerializer, ContractDurationSerializer, MonthSerializer, DistributorSerializer,TenderBSerializer
)
from .shared_data import win_prob

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = AccountList.objects.all()
    serializer_class = AccountSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = CityList.objects.all()
    serializer_class = CitySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ContractDurationViewSet(viewsets.ModelViewSet):
    queryset = ContractDuration.objects.all()
    serializer_class = ContractDurationSerializer

class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data)
            # Filter out the fields to be stored
            data_to_store = {
                'tender_name': data.get('tender_name', ''),
                'quantity': data.get('quantity', 0),
                'price_a': data.get('price', 0.0)
            }
            serializer = self.get_serializer(data=data_to_store)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            # sectionCData
            final_data = {}
            sectionCData = {}
            quan = int(data.get('quantity'))
            price = int(data.get('price'))
            revenue = quan*price
            final_data.update(serializer.data)
            sectionCData.update({'revenue':revenue})
            margin  = int((40/100)*revenue)
            sectionCData.update({'margin':margin})
            winProbability = 0
            for d in win_prob:
                if price in d:
                    winProbability = d[price]
            final_data.update({'winProbability':winProbability})
            final_data.update({'sectionCData':sectionCData})
            # sectionDData
            sectionDData = {}
            
            if not GraphList.objects.filter(win_probability=winProbability).exists():
                gl = GraphList.objects.create(margin=margin,win_probability=winProbability,price=price)
                tend = Tender.objects.get(tender_name=data.get('tender_name'))
                tend.graph_list=gl
                tend.save()
            else:
                gl = GraphList.objects.filter(win_probability=winProbability)
                tend = Tender.objects.get(tender_name=data.get('tender_name'))
                tend.graph_list=gl
                tend.save()

            sectionDData.update({'margin':margin})
            sectionDData.update({'winProbability':winProbability})
            sectionDData.update({'price':price})
            final_data.update({'sectionDData':sectionDData})
            print(final_data)
            return Response(final_data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError as e:
            return JsonResponse({'error': 'This value {} already exists'.format(e)}, status=400)

    

class TenderBViewSet(viewsets.ModelViewSet):
    queryset = TenderB.objects.all()
    serializer_class = TenderBSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data)
            # Filter out the fields to be stored
            data_to_store = {
                'tender_name': data.get('tender_name', ''),
                'quantity': data.get('quantity', 0),
                'price_b': data.get('price_b', 0.0)
            }
            serializer = self.get_serializer(data=data_to_store)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            # sectionBData
            final_data = {}
            sectionBData = {}
            quan = int(data.get('quantity'))
            price = int(data.get('price_b'))
            revenue = quan*price
            final_data.update(serializer.data)
            sectionBData.update({'revenue':revenue})
            margin  = int((40/100)*revenue)
            sectionBData.update({'margin':margin})
            winProbabilityb = 0
            for d in win_prob:
                if price in d:
                    winProbabilityb = d[price]
            final_data.update({'winProbabilityb':winProbabilityb})
            final_data.update({'sectionBData':sectionBData})
            # sectionDData
            
            if not GraphList.objects.filter(win_probability=winProbabilityb).exists():
                gl = GraphList.objects.create(margin=margin,win_probability=winProbabilityb,price=price)
                tend = TenderB.objects.get(tender_name=data.get('tender_name'))
                tend.graph_list=gl
                tend.save()
            else:
                gl = GraphList.objects.filter(win_probability=winProbabilityb)
                tend = TenderB.objects.get(tender_name=data.get('tender_name'))
                tend.graph_list=gl
                tend.save()

            graph_data = GraphList.objects.all().order_by('win_probability')
            sectionDData = [{'price':g.price,'margin':g.margin,'winProbability':g.win_probability} for g in graph_data]
            final_data.update({'sectionDData':sectionDData})
            print(final_data)
            return Response(final_data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError as e:
            return JsonResponse({'error': 'This value {} already exists'.format(e)}, status=400)
