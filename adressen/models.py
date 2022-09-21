from django.db import models
from django.urls import reverse
from django.db.models import Model
from datetime import date

# Create your models here.
class Adressen(models.Model):
    created_at = models.DateField(default=date.today)
    anlagenname = models.CharField(max_length=100)
    name =  models.CharField(max_length=200)
    vorname = models.CharField(max_length=200, default="")
    anschrift = models.CharField(max_length=200)
    plz = models.IntegerField()
    ort = models.CharField(max_length=100)
    telefon = models.CharField(default=0, max_length=30)
    handy = models.CharField(default=0, max_length=30)
    emailadresse = models.EmailField(max_length=100)
    inbetriebnahme = models.DateField(default=date.today)
    anlagenleistung = models.FloatField(default=0)
    einspeiseverguetung = models.FloatField(default=0)
    eigenverbrauch = models.BooleanField(default=False)
    wirkbegrenzung = models.BooleanField(default=False)
    spezifischer_jahresertrag = models.IntegerField(default=0)
    sn_homemanager = models.IntegerField(default = 0 )
    passwort_portal = models.CharField(max_length=20, default="-")
    wr1 = models.CharField(max_length=100, default="-")
    wr1_sn = models.IntegerField(default=0 )
    wr2 = models.CharField(max_length=100, default="-")
    wr2_sn = models.IntegerField(default=0)
    batteriewr = models.CharField(max_length=200, default="-")
    batteriewr_sn = models.IntegerField(default=0)
    batteriemodul = models.CharField(max_length=100, default="-")
    solarmodule = models.CharField(max_length=100, default="-")
    anlagenpasswort = models.CharField(max_length=20, default="Portal-PW")
    notizen = models.TextField(max_length=1000, default="-")
    termin_auf = models.DateField(default=date.today)
    termin_auf_erl = models.BooleanField(default=False)
    notizen_termin = models.TextField(max_length=1000, default="-")

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('adress_detail', args=[str(self.id)])

    class Meta:
       ordering = ('-id',)
