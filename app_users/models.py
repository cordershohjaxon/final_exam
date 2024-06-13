import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField

from .managers import UserManager
from django.utils import timezone


class User(AbstractUser):
    """
    Custom User model extending AbstractUser.

    Fields:
    - first_name (CharField): User's first name with max length of 100.
    - last_name (CharField): User's last name with max length of 100.
    - username (CharField): Username with max length of 100, can be blank.
    - email (CharField): User's email, must be unique.
    - profile_image (ImageField): Profile image, default is 'images/profile_image.png'.
    - is_staff (BooleanField): Indicates if the user is a staff member.
    - is_superuser (BooleanField): Indicates if the user is a superuser.
    - is_active (BooleanField): Indicates if the user is active.

    Methods:
    - get_full_name: Returns the full name of the user.
    - __str__: Returns a string representation of the user.
    """

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
        """Returns the full name of the user."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """Returns a string representation of the user."""
        return f'{self.first_name} {self.last_name}'


class Kirim(models.Model):
    """
    Model representing income (Kirim).

    Fields:
    - user (ForeignKey): Reference to the User model.
    - summa (DecimalField): Amount of income.
    - qayerdan (CharField): Source of the income.
    - sana (DateTimeField): Date and time of the income.
    - tolov_turi (CharField): Payment type, either 'cash' or 'card'.
    - ish_haqqi_turi (CharField): Source type, either 'monthly', 'advance', or 'daily'.
    - status (str): Status of the transaction, fixed as 'kirim'.

    Methods:
    - __str__: Returns a string representation of the Kirim instance.
    """

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
        """Returns a string representation of the Kirim instance."""
        return f"{self.summa} - {self.qayerdan} UZS"


class Chiqim(models.Model):
    """
    Model representing expenses (Chiqim).

    Fields:
    - user (ForeignKey): Reference to the User model.
    - summa (DecimalField): Amount of expense.
    - qayerga (CharField): Destination of the expense.
    - tolov_turi (CharField): Payment type, either 'NAQT' or 'KARTA'.
    - chiqim_turi (CharField): Type of expense.
    - sana (DateTimeField): Date and time of the expense.
    - status (str): Status of the transaction, fixed as 'chiqim'.

    Methods:
    - __str__: Returns a string representation of the Chiqim instance.
    """

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
        """Returns a string representation of the Chiqim instance."""
        return f"{self.summa} UZS to {self.qayerga}"
