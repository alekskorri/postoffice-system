from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    shipment_value = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    client = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    ordered_time = models.DateTimeField(default=timezone.now)
    date_received = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    # create_by = models.CharField(max_length=100, blank=True, null=True)
    # created_date = models.DateField(blank=True, null=True)
    #
    # update_by = models.CharField(max_length=100, blank=True, null=True)
    # update_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = 0
        if self.shipment_value is None:
            self.shipment_value = 0

        self.total = self.price + self.shipment_value

        super().save(*args, **kwargs)


class SentPackages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_packages', default=1)
    product = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    shipment_value = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    client = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    ordered_time = models.DateTimeField()
    date_sent = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = 0
        if self.shipment_value is None:
            self.shipment_value = 0

        self.total = self.price + self.shipment_value

        super().save(*args, **kwargs)


class CancelledPackages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cancelled_packages', default=1)
    product = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    shipment_value = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    client = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    ordered_time = models.DateTimeField()
    date_cancelled = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = 0
        if self.shipment_value is None:
            self.shipment_value = 0

        self.total = self.price + self.shipment_value

        super().save(*args, **kwargs)
