# Generated by Django 5.1.2 on 2024-11-12 15:45

import homepage.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_message_service_type_alter_message_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='message',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[homepage.validators.iranian_phone_number_validator], verbose_name='شماره تماس'),
        ),
    ]
