from django.contrib import admin

from .models import Vendor, Food

# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor_name")
    search_fields = ('vendor_name',)  # 讓後台出現關鍵字搜尋框
    list_filter = ('vendor_name',)    # 讓右側出現篩選器外掛

admin.site.register(Food)