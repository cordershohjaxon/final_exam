# Generated by Django 5.0.6 on 2024-06-10 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0016_remove_kirim_avans_remove_kirim_boshqa_valyuta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirim',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
