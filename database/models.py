from django.db import models

# Create your models here.
class BloodType(models.Model):
    blood_group = models.CharField(max_length=3, primary_key=True)

    def __str__(self):
        return self.blood_group

class CanDonateTo(models.Model):
    blood_group = models.ForeignKey(BloodType, related_name='can_donate_to', on_delete=models.CASCADE, db_column='blood_group')
    can_donate_to = models.ForeignKey(BloodType, on_delete=models.CASCADE, related_name='+')

    class Meta:
        unique_together = ('blood_group', 'can_donate_to')

    def __str__(self):
        return f"{self.blood_group} can donate to {self.can_donate_to}"

class CanReceiveFrom(models.Model):
    blood_group = models.ForeignKey(BloodType, related_name='can_receive_from', on_delete=models.CASCADE, db_column='blood_group')
    can_receive_from = models.ForeignKey(BloodType, on_delete=models.CASCADE, related_name='+')

    class Meta:
        unique_together = ('blood_group', 'can_receive_from')

    def __str__(self):
        return f"{self.blood_group} can receive from {self.can_receive_from}"
    

# class User(models.Model)