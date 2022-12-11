from django.contrib import admin
from ticketingtoolapp.models import ProductModel,ApplicationModel,BookingModel,StationaryModel

@admin.register(ProductModel)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at','status']

@admin.register(ApplicationModel)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at','status']

@admin.register(BookingModel)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at','status']

@admin.register(StationaryModel)
class StationaryAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_name','your_requirement','Reason','request_raised_at','status']



