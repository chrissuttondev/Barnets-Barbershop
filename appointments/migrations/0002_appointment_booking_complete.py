# Generated by Django 4.2.13 on 2024-06-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment_booking',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]