from django.db import models

""" Svaka životinja ima ID, ime,
kategoriju, URLove do slika, tagove i statuse. 
Status može biti placed/approved/delivered.
Potrebno je omogućiti dodavanje, uređivanje, brisanje i 
pregledavanje životinja, kategorija,
tagova. """

class Animals(models.Model):

    STATUS_CHOICES = (
        (PLACED, u'Placed'),
        (APPROVED, u'Approved'),
        (DELIVERED, u'Delivered'),
    )


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    picture_url = models.CharField()
    tags = models.CharField()
    status = models.CharField(
    u'Status', max_length=20,
    choices=STATUS_CHOICES)