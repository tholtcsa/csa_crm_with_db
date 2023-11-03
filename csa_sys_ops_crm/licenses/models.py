from django.db import models
from django.urls import reverse 
from utilities.models import Utility

class License(models.Model):
    license_id = models.CharField(primary_key=True, max_length=50, auto_created=True)
    license_distnum = models.ForeignKey(Utility, to_field='distnum', on_delete=models.CASCADE)
    license_utility = models.ForeignKey(Utility, to_field='utility', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, blank=True, null=True)
    sw_edition = models.CharField(max_length=50, blank=True, null=True)
    sw_version = models.CharField(max_length=50, blank=True, null=True)
    sw_type = models.CharField(max_length=50, blank=True, null=True)
    build_level = models.CharField(max_length=50, blank=True, null=True)
    sw_key = models.CharField(max_length=100, blank=True, null=True)
    sw_qty = models.IntegerField(max_length=50, blank=True, null=True)

    SWSTATE_CHOICES = (
        ('removed', 'Removed'),
        ('installed', 'Installed'),
        ('upgraded', 'Upgraded'),
        ('available', 'Available'),
    )

    sw_state = models.CharField(max_length=50, blank=True, null=True, choices=SWSTATE_CHOICES, default='Available')

    LICENSESTATUS_CHOICES = (
        ('available', 'Available'),
        ('expired', 'Expired'),
    )

    license_status = models.CharField(max_length=50, blank=True, null=True, choices=LICENSESTATUS_CHOICES)

    license_auth_number = models.CharField(max_length=50, blank=True, null=True)
    license_agreement_number = models.CharField(max_length=50, blank=True, null=True)
    agmt_start_date = models.DateField(verbose_name='Agreement Start Date', blank=True, null=True)
    license_po_number = models.CharField(max_length=50, blank=True, null=True)
    license_ticket_number = models.CharField(max_length=50, blank=True, null=True)
    agmt_expire_date = models.DateField(null=True, blank=True, verbose_name='Agreement Expiration Date')
    license_install_date = models.DateField(null=True, blank=True, verbose_name='License Install Date')
    license_removal_date = models.DateField(null=True, blank=True, verbose_name='License Removal Date')

    def __str__(self):
        return self.license_id
    
    def get_absolute_url(self):
        return reverse('license_detail', kwargs={"pk": self.pk})