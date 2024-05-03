from django.contrib import admin
from .models import BloodType, CanDonateTo, CanReceiveFrom
# Register your models here.


admin.site.register(BloodType)
admin.site.register(CanDonateTo)
admin.site.register(CanReceiveFrom)