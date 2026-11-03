from django.contrib import admin

from .models import Vendor, Food
from django.utils.translation import gettext_lazy as _
# Register your models here.

class Morethanfifty(admin.SimpleListFilter):
    title = _("price")
    parameter_name = "compareprice"

    def lookups(self, request, model_admin):
        return (
            (">50", _("大於50元")),
            ("<=50", _("小於等於50元")),
        )
    def queryset(self, request, queryset):
        if self.value == ">50":
            return queryset.filter(price_name__gt=50)
        if self.value == "<=50":
            return queryset.filter(price_name__lte=50)
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vendor._meta.fields]
    search_fields = ('vendor_name',)  # 讓後台出現關鍵字搜尋框
    list_filter = ('vendor_name',)    # 讓右側出現篩選器外掛

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
    search_fields = ('food_name',)
    list_filter = (Morethanfifty,)
    ordering = ['price_name',]