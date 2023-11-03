from django.db import models
from django.urls import reverse 
from utilities.models import Utility
from choices.models import PCBuildConfig, PCChassisTypes, PCManufacturers, PCModel, PCOperatingSystem, PCShortcuts, PCType, Program


class EquipmentInfo(models.Model):
    ip_id = models.BigAutoField(primary_key=True, auto_created=True, name='Equipment ID', unique=True)
    equipment_id = models.CharField(max_length=255, verbose_name='Equipment ID', null=True, blank=True)
    equipment_name = models.CharField(max_length=255, verbose_name='Equipment Name', null=True)
    serial_number = models.CharField(max_length=255, verbose_name='Serial Number', unique=True, null=True, blank=True)
    service_tag = models.CharField(max_length=255, verbose_name='Service Tag', unique=True, null=True, blank=True)
    utility = models.ForeignKey(Utility, on_delete=models.CASCADE, to_field='name')
    office = models.CharField(max_length=255, verbose_name='Office Location', null=True)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('decommissioned', 'Decommissioned'),
    ]
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, verbose_name='Status', null=True)
    suite_name = models.CharField(max_length=255, verbose_name='Suite Name', null=True)
    main_funtion = models.CharField(max_length=255, verbose_name='Main Function', null=True)
    HOSTING_CHOICES = [
        ('csa', 'CSA'),
        ('utility', 'Utility')
    ]
    hosting_type = models.CharField(max_length=25, choices=HOSTING_CHOICES, null=True)
    operating_system = models.ForeignKey(PCOperatingSystem, on_delete=models.CASCADE, verbose_name='OS', null=True)
    manufacturer = models.ForeignKey(PCManufacturers, on_delete=models.CASCADE, verbose_name='Manufacturer', null=True)
    type = models.ForeignKey(PCType, on_delete=models.CASCADE, verbose_name='Type (optiplex, etc)', null=True)
    model = models.ForeignKey(PCModel, on_delete=models.CASCADE, verbose_name='Model (i.e. 7000, etc)', null=True)
    shortcuts = models.ManyToManyField(PCShortcuts, verbose_name='Shortcuts on this PC')
    programs = models.ManyToManyField(Program, verbose_name='Programs on this PC')
    domain_name = models.CharField(max_length=255, verbose_name='Domain Name', null=True)
    user_name = models.CharField(max_length=255, verbose_name='Username', null=True)
    friendly_name = models.CharField(max_length=255, verbose_name='Friendly Name', null=True)
    dns_logon_name = models.CharField(max_length=255, verbose_name='DNS Logon Name', null=True)
    ip_address = models.CharField(max_length=255, verbose_name='IP Address', null=True)
    subnet_mask = models.CharField(max_length=255, verbose_name='Subnet Mask', null=True)
    gateway = models.CharField(max_length=255, verbose_name='Default Gateway', null=True)
    dns_preferred = models.CharField(max_length=255, verbose_name='DNS (Preferred)', null=True)
    
    def __str__(self):
        return self.equipment_id
    
    def get_absolute_url(self):
        return reverse("equipmentinfo_detail", kwargs={"pk": self.pk})
