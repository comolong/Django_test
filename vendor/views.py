from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Vendor, Food

# Create your views here.
def showtemplates(request):
    return render(request, 'test.html')

def food_list(request, food_id):
    food_data = get_object_or_404(Food, id=food_id) # id也可以直接改成pk，pk就是直接去找資料庫的主鍵(prime key)
    return HttpResponse(f'你點的餐點是{food_data.food_name}')

def vendor_index(request):
    vendor_list = Vendor.objects.all()
    context = {"Vendor_list":vendor_list}
    return render(request, 'vendor_test.html', context)

def block_test(request):
    context = {"Vendor_list":Vendor.objects.all()}
    return render(request, "vendor_block.html", context)