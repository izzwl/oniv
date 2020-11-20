from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from uuid import uuid4
import os
# Create your models here.

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_("Phone number must be entered in the format: '+99999999' up to 15 digits allowed")
)
@deconstructible
class UploadImage(object):
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        try:
            dt = instance.dt_add
        except:
            dt = None
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        if dt:
            return os.path.join(self.sub_path, str(dt.year), str(dt.month), filename)
        else:
            return os.path.join(self.sub_path, filename)

upload_venue_image = UploadImage('venue-images/')
upload_event_image = UploadImage('event-images/')
upload_bridegroom_image = UploadImage('bridegroom-images/')
upload_gallery_image = UploadImage('gallery-images/')

class Host(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    phone = models.CharField(_("Phone"),max_length=16)

    def __str__(self):
        return self.name

class BrideGroom(models.Model):
    CH_BRIDEGROOM = (
        ('bride','Bride'),
        ('groom','Groom'),
    )
    bridegroom = models.CharField(_("Bride/Groom"),max_length=100,choices=CH_BRIDEGROOM)
    name = models.CharField(_("Fullname"),max_length=100)
    short_name = models.CharField(_("Shortname"),max_length=100)
    mother = models.CharField(_("Mother"),max_length=100)
    father = models.CharField(_("Father"),max_length=100)
    image = models.ImageField(upload_to=upload_bridegroom_image, height_field='image_height', width_field='image_width', blank=True)
    image_width = models.PositiveIntegerField(default=0)
    image_height = models.PositiveIntegerField(default=0)
    dt_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    address = models.CharField(_("Address"),max_length=100)
    gmap_url = models.CharField(_("Google map URL"),max_length=255)
    gmap_embed = models.TextField(_("Google map Embed"),default='')
    lat = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=8)
    lng = models.DecimalField(_('Longitude'), max_digits=11, decimal_places=8)
    image = models.ImageField(upload_to=upload_venue_image, height_field='image_height', width_field='image_width', blank=True)
    image_width = models.PositiveIntegerField(default=0)
    image_height = models.PositiveIntegerField(default=0)
    dt_add = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(_('Event Name'), max_length=100, default='',unique=True)
    bride = models.ForeignKey(BrideGroom,on_delete=models.CASCADE,related_name='bride_event_set',verbose_name='Bride')
    groom = models.ForeignKey(BrideGroom,on_delete=models.CASCADE,related_name='groom_event_set',verbose_name='Groom')
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE,verbose_name='Venue')
    gcal_link = models.TextField(_('Google Calendar Link'),default='')
    dt_countdown = models.DateTimeField(_('Countdown'),null=True,default=None)
    d_ceremony = models.DateField(_('Ceremony (Date)'))
    d_reception = models.DateField(_('Reception (Date)'))
    p_ceremony = models.CharField(_('Ceremony (Time)'), max_length=100,)
    p_reception = models.CharField(_('Reception (Time)'), max_length=100,)
    image = models.ImageField(upload_to=upload_event_image, height_field='image_height', width_field='image_width', blank=True)
    image_width = models.PositiveIntegerField(default=0)
    image_height = models.PositiveIntegerField(default=0)
    dt_add = models.DateTimeField(auto_now_add=True)
    meta_image = models.ImageField(upload_to=upload_event_image, blank=True, null=True, default=None)
    def __str__(self):
        return self.bride.name + " - " + self.groom.name

class EventGallery(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,verbose_name='Event')
    name = models.CharField(_("Name"),max_length=100)
    image = models.ImageField(upload_to=upload_gallery_image, height_field='image_height', width_field='image_width', blank=True)
    image_width = models.PositiveIntegerField(default=0)
    image_height = models.PositiveIntegerField(default=0)
    dt_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Invitation(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,verbose_name='Event')
    name = models.CharField(_("Name"),max_length=100)
    address = models.CharField(_("Address"),max_length=100)
    is_attend = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CongratulationWhises(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,verbose_name='Event',default=None,null=True)
    message = models.TextField()

class Attendance(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE,verbose_name='Event',default=None,null=True)
    name = models.CharField(_("Name"),max_length=100,default='')
    phone = models.CharField(_("Phone"),max_length=16,default='')
    email = models.EmailField(_("Email"),default='')
    whises = models.TextField(_("Whises"),default='')
    is_attend = models.BooleanField(default=False)
    guest = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['-pk']



