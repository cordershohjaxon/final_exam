import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField

from .managers import UserManager
from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(
        upload_to='images/', default='images/profile_image.png', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Kirim(models.Model):
    CASH = 'cash'
    CARD = 'card'
    PAYMENT_CHOICES = [
        (CASH, 'Naqd'),
        (CARD, 'Karta'),
    ]

    MONTHLY = 'monthly'
    ADVANCE = 'advance'
    DAILY = 'daily'
    SOURCE_TYPE_CHOICES = [
        (MONTHLY, 'Oylik'),
        (ADVANCE, 'Avans'),
        (DAILY, 'Kunlik ish haqqi'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    summa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    qayerdan = models.CharField(max_length=255, null=True, blank=True)
    sana = models.DateTimeField(default=timezone.now)
    tolov_turi = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default=CASH)
    ish_haqqi_turi = models.CharField(max_length=10, choices=SOURCE_TYPE_CHOICES, default=MONTHLY)
    status = 'kirim'
    def __str__(self):
        return f"{self.summa} - {self.qayerdan} UZS"


class Chiqim(models.Model):
    NAQT = 'NAQT'
    KARTA = 'KARTA'

    TOLOV_TURLARI = [
        (NAQT, 'Naqt'),
        (KARTA, 'Karta'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    summa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    qayerga = models.CharField(max_length=255, null=True, blank=True)
    tolov_turi = models.CharField(max_length=5, choices=TOLOV_TURLARI, default=NAQT)
    chiqim_turi = models.CharField(max_length=50, null=True, blank=True)
    sana = models.DateTimeField(default=timezone.now)
    status = 'chiqim'
    def __str__(self):
        return f"{self.summa} UZS to {self.qayerga}"
