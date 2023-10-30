from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Product

@api_view(['GET'])
def index(request):
    return HttpResponse ("hello")

@api_view(['GET','POST'])
def products(request):
    print(request)
    tempAr=[]
    for prod in Product.objects.all():
        tempAr.append({"description":prod.description,"price":prod.price,"id":stu.id})
    return HttpResponse(tempAr)