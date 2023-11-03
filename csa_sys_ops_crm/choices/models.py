from django.db import models
from django.urls import reverse

#EQUIPMENT MODEL CHOICES

from django.db import models
from utilities.models import Utility
from django.urls import reverse

class Program(models.Model):
    program_name = models.CharField(
        primary_key=True,
        max_length=200,
        default=None,
        help_text="Examples 'INovah', 'Adobe', etc..."
    )

    def __str__(self):
        return self.program_name
       
class PCManufacturers(models.Model):
    pcman_name = models.CharField(
        primary_key=True,
        max_length=100,
        default=None,
        help_text="Dell, HP, etc"
    )

    def __str__(self):
        return self.pcman_name
    
class PCModel(models.Model):
    pcmake_name = models.CharField(
        primary_key=True,
        max_length=100,
        default=None,
        help_text='Example: 7000, etc.'
    )

    def __str__(self):
        return self.pcmake_name
    
class PCOperatingSystem(models.Model):
    os_name = models.CharField(
        primary_key=True,
        max_length=40,
        default=None,
        help_text="Example: Windows 10 or 11, Server 2016 or 2019, etc."
    )
    
    def __str__(self):
        return self.os_name
    
class PCBuildConfig(models.Model):
    pcbuild_name = models.CharField(
        primary_key=True,
        max_length=50,
        default=None,
        help_text="Example: Cashier, Engineer, Regular, etc."
    )

    def __str__(self):
        return self.pcbuild_name
    
class PCChassisTypes(models.Model):
    chassis_name = models.CharField(
        primary_key=True,
        max_length=50,
        default=None,
        help_text="Example: Tower, Desktop, Laptop, etc."
    )

    def __str__(self):
        return self.chassis_name

class PCType(models.Model):
    pc_type = models.CharField(
        primary_key=True,
        max_length=255,
        verbose_name='Type',
        help_text='Example: Opiplex, PowerEdge, etc.'
    )
    
    def __str__(self):
        return self.pc_type
    
class PCShortcuts(models.Model):
    pcshortcut_name = models.CharField(
        primary_key=True,
            max_length=200,
            verbose_name="Any desktop shortcuts that CSA can install onto PC(s)",
            help_text="Examples 'GP', 'CMB'"
        )
        
    def __str__(self):
        return self.pcshortcut_name
