from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db import models
from .models import POST
from django.views import View
import json

class Account(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'accounts'

class AccountView(View):
    def Post(self, request):
        data = json.loads(request.body)
        Account.objects.create(
            name=data['name'],
            password=data['password']
        )

        return HttpResponse(status=200)
    
    def get(self, request):
        Account_data = Account.objects.values()
        return JsonResponse({'accounts' : list(Account_data)}, status=200)
    
class SignView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(name = data['name']).exists():
                user = Account.objects.get(name=data['name'])
                
                if user.password == data['password']:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({'message' : "회원이 아닙니다."}, status=400)

