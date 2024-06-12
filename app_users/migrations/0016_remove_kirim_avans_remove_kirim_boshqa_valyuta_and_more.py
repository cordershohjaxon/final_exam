# Generated by Django 5.0.6 on 2024-06-10 09:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0015_kirim_avans_kirim_boshqa_valyuta_kirim_karta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kirim',
            name='avans',
        ),
        migrations.RemoveField(
            model_name='kirim',
            name='boshqa_valyuta',
        ),
        migrations.RemoveField(
            model_name='kirim',
            name='karta',
        ),
        migrations.RemoveField(
            model_name='kirim',
            name='kunlik_ish_haqqi',
        ),
        migrations.RemoveField(
            model_name='kirim',
            name='naqt',
        ),
        migrations.RemoveField(
            model_name='kirim',
            name='oylik',
        ),
        migrations.RemoveField(
            model_name='kirim',
            name='qayerdan',
        ),
        migrations.RemoveField(
            model_name='kirim',
            name='sana',
        ),
        migrations.AddField(
            model_name='kirim',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='kirim',
            name='source',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='kirim',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]