from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    """
        Table for holding company details
    """

    branch_name = models.CharField(max_length=100, unique=True)
    branch_id = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)


class RevenueDetails(models.Model):
    """
        Table for holding revenue details
    """
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    receipt = models.BigIntegerField()
    updated_date = models.DateTimeField(default=timezone.now)
    total = models.FloatField()
