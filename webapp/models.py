from django.db import models

class CreateTimeMixin(models.Model):
    """Mixin for adding create_at field into model"""
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Company(CreateTimeMixin, models.Model):
    """Company Model"""
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company_logos', )
    scope = models.ForeignKey('Scope', on_delete=models.SET_NULL, null=True, blank=True)

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


class Office(CreateTimeMixin, models.Model):
    """Office model"""
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='offices')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Oфисы'
