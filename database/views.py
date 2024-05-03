from django.shortcuts import render
from .models import BloodType, CanDonateTo, CanReceiveFrom

def blood_type_details(request):
    blood_groups = ['A-', 'A+', 'B-', 'B+', 'AB-', 'AB+', 'O-', 'O+']

    can_donate_to_data = get_blood_types_can_donate_to(blood_groups)
    can_receive_from_data = get_blood_types_can_receive_from(blood_groups)

    context = {
        'can_donate_to_data': can_donate_to_data,
        'can_receive_from_data': can_receive_from_data,
    }

    return render(request, 'database/blood_type_details.html', context)

def get_blood_types_can_donate_to(blood_groups):
    can_donate_to_list = []
    for blood_group in blood_groups:
        blood_type = BloodType.objects.get(blood_group=blood_group)
        can_donate_to = [donation.can_donate_to for donation in blood_type.can_donate_to.all()]
        can_donate_to_list.append((blood_group, can_donate_to))
    return can_donate_to_list

def get_blood_types_can_receive_from(blood_groups):
    can_receive_from_list = []
    for blood_group in blood_groups:
        blood_type = BloodType.objects.get(blood_group=blood_group)
        can_receive_from = [donation.can_receive_from for donation in blood_type.can_receive_from.all()]
        can_receive_from_list.append((blood_group, can_receive_from))
    return can_receive_from_list