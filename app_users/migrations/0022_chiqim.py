# Generated by Django 5.0.6 on 2024-06-11 09:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0021_alter_kirim_sana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chiqim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('qayerga', models.CharField(blank=True, max_length=300, null=True)),
                ('chiqim_turi', models.CharField(blank=True, max_length=300, null=True)),
                ('sana', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
