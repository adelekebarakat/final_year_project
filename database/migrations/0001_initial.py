# Generated by Django 5.0.4 on 2024-04-30 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('blood_group', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CanDonateTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.ForeignKey(db_column='blood_group', on_delete=django.db.models.deletion.CASCADE, related_name='can_donate_to', to='database.bloodtype')),
                ('can_donate_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='database.bloodtype')),
            ],
            options={
                'unique_together': {('blood_group', 'can_donate_to')},
            },
        ),
        migrations.CreateModel(
            name='CanReceiveFrom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.ForeignKey(db_column='blood_group', on_delete=django.db.models.deletion.CASCADE, related_name='can_receive_from', to='database.bloodtype')),
                ('can_receive_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='database.bloodtype')),
            ],
            options={
                'unique_together': {('blood_group', 'can_receive_from')},
            },
        ),
    ]
