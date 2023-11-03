from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Utility(models.Model):
    distnum = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        help_text="Enter Utility Dist Number",
    )
    name = models.CharField(
        max_length=150,
        help_text="Enter Utility Name",
        verbose_name="Utility Name",
        unique=True,
    )
    mail_address = models.CharField(
        max_length=200,
        verbose_name="Mailing Address",
        help_text="Utility's mailing address",
        null=True,
        blank=True,
    )
    ship_address = models.CharField(
        max_length=200,
        verbose_name="Shipping Address",
        help_text="Utility's Shipping Address",
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=50,
        verbose_name="City",
        help_text="Enter Utility's city",
        null=True,
        blank=True,
    )
    state = models.CharField(
        max_length=40,
        verbose_name="State",
        help_text="Enter Utility's state",
        default="Mississippi",
        null=True,
        blank=True,
    )
    mail_zip = models.CharField(
        max_length=15,
        verbose_name="Zip Code",
        help_text="Enter Utility's Zip Code",
        null=True,
        blank=True,
    )
    ship_zip = models.CharField(max_length=15, verbose_name="Shipping Zip Code", null=True,
        blank=True,)
    phone = models.CharField(
        max_length=25,
        verbose_name="Main Phone Number",
        help_text="Enter Utility's Phone Number",
        null=True,
        blank=True,
    )
    fax = models.CharField(
        max_length=20,
        verbose_name="Fax Number",
        help_text="Utility's Fax Number",
        null=True,
        blank=True,
    )
    system = models.CharField(max_length=50, verbose_name="System", null=True,
        blank=True,)
    region = models.CharField(max_length=35, verbose_name="Region", null=True,
        blank=True,)
    hours = models.CharField(
        max_length=255,
        verbose_name="Utility Hours of Operation",
        help_text="Enter Hours of Operation if you have it",
        blank=True,
        null=True,
    )
    notes = models.TextField(
        verbose_name="Additional Notes",
        help_text="Please Enter Any Additional Info Here",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("utility_detail", kwargs={"pk": self.pk})

