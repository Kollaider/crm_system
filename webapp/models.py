from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class CreateTimeMixin(models.Model):
    """Mixin for adding create_at field into model"""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdateTimeMixin(models.Model):
    """Mixin for adding updated_at field into model"""

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(CreateTimeMixin, UpdateTimeMixin, models.Model):
    """Company Model"""

    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company_logos', )
    scope = models.ForeignKey('Scope', on_delete=models.SET_NULL, null=True, blank=True)
    country = CountryField(blank_label='выберите страну', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Scope(CreateTimeMixin, models.Model):
    """Scope model"""

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'


class Office(CreateTimeMixin, UpdateTimeMixin, models.Model):
    """Office model"""

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='offices')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Oфисы'


class Profile(CreateTimeMixin, models.Model):
    """Profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    photo = models.ImageField(upload_to='user_photos', blank=True)
    languages = models.ManyToManyField('Language')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Position(CreateTimeMixin, models.Model):
    """Position model"""

    name = models.CharField(max_length=30)
    is_remote = models.BooleanField(default=False)
    salary = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.company.name})'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Language(CreateTimeMixin, models.Model):
    """Language model"""

    A0 = 'A0'
    A1 = 'A1'
    A2 = 'A2'
    B1 = 'B1'
    B2 = 'B2'
    C1 = 'C1'
    C2 = 'C2'
    LANGUAGE_LEVEL_CHOICES = [
        (A0, 'Beginner'),
        (A1, 'Elementary'),
        (A2, 'Pre-Intermediate'),
        (B1, 'Intermediate'),
        (B2, 'Upper-Intermediate'),
        (C1, 'Advanced'),
        (C2, 'Proficiency'),
    ]

    name = models.CharField(max_length=30)
    level = models.CharField(max_length=2, choices=LANGUAGE_LEVEL_CHOICES)
    is_native = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.level}'

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
