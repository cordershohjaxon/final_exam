# Generated by Django 5.0.6 on 2024-06-09 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0013_kirim_boshqa_valyuta_kirim_karta_kirim_naqt_and_more'),
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
    ]
