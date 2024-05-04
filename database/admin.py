from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BloodType, CanDonateTo, CanReceiveFrom, BloodUser
# Register your models here.

class BloodUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'get_blood_type', 'phone_number', 'email')

    def get_blood_type(self, obj):
        return obj.blood_type  # Access blood type through the ForeignKey relationship

    get_blood_type.short_description = 'Blood Type'

admin.site.register(BloodType)
admin.site.register(BloodUser, BloodUserAdmin)
admin.site.register(CanDonateTo)
admin.site.register(CanReceiveFrom)
