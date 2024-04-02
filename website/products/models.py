from typing import Any, Iterable
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = 'published')
class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = 'draft')
class ProductObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
class Product(models.Model):
    options = (
        ('draft','Draft'),
        ('published','Published')
        )
    name = models.CharField(max_length=255, unique = True , 
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9 ]+$',
                message='Only alphabets, spaces, and numbers are allowed.',
                code='invalid_your_field'
            ),
        ],)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.CharField(default = 'no rating' ,  max_length = 10, null=True, blank=True)
    description =  models.TextField(null=True, blank=True)
    provider = models.ForeignKey(get_user_model() , on_delete = models.CASCADE)
    number_of_comments = models.PositiveIntegerField(default = 0 , null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length = 10 , choices = options , default = 'draft')
    slug = models.SlugField(null=True, blank=True)
    objects = ProductObjectsManager()
    published = PublishedManager()
    draft = DraftManager()
    def __str__(self):
        return self.name
@receiver(pre_save, sender=Product)
def update_product(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = instance.name.replace(" ", "-")
    if instance.pk is None:
        if instance.status == 'published':
            instance.date = timezone.now()
    else:
        old_instance = Product.objects.get(pk=instance.pk)
        if old_instance.status == 'draft' and instance.status == 'published':
            instance.date = timezone.now()
class RateQuerySet(models.QuerySet):
    def get_average(self):
        if self.all().count() == 0:
            return 'no rating'
        total_rates = 0 
        total_raters = 0 
        for instance in self.all():
            total_rates += int(instance.rate)
            total_raters += 1
        average = total_rates / total_raters
        average = round(average , 1)
        return str(average)
class RateObjectsManager(models.Manager):
    def get_queryset(self):
        return RateQuerySet(self.model , using=self._db)
    def get_average(self):
        return self.get_queryset().get_average()
class Rate(models.Model):
    options = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    product = models.ForeignKey(Product, related_name = 'rates' , on_delete = models.CASCADE)
    rate = models.CharField(max_length = 2 , choices = options)
    rater = models.ForeignKey(get_user_model() , on_delete = models.CASCADE)
    objects = RateObjectsManager()
    def __str__(self):
        return self.rater.get_username() + f": {self.rate}"
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        myinstance = Product.objects.get(name = self.product.name)
        myinstance.rate = myinstance.rates.get_average()
        myinstance.save()
    def delete(self,*args, **kwargs):
        super().delete(*args, **kwargs)
        myinstance = Product.objects.get(name = self.product.name)
        myinstance.rate = myinstance.rates.get_average()
        myinstance.save()
class Comment(models.Model):
    product = models.ForeignKey(Product, related_name = 'comments' , on_delete = models.CASCADE)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user_comment = models.CharField(max_length=500)
    def __str__(self):
        return self.writer.get_username() + f": {self.user_comment[:10]}"
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        myinstance = Product.objects.get(name = self.product.name)
        myinstance.number_of_comments = myinstance.comments.all().count()
        myinstance.save()
    def delete(self,*args, **kwargs):
        super().delete(*args, **kwargs)
        myinstance = Product.objects.get(name = self.product.name)
        myinstance.number_of_comments = myinstance.comments.all().count()
        myinstance.save()