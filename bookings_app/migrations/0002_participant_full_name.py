# Generated by Django 5.2 on 2025-05-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='full_name',
            field=models.SlugField(blank=True, default='', max_length=200),
        ),
    ]
