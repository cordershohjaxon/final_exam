# Generated by Django 5.0.6 on 2024-05-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
