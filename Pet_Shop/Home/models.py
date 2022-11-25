from django.db import models

""" Svaka životinja ima ID, ime,
kategoriju, URLove do slika, tagove i statuse. 
Status može biti placed/approved/delivered.
Potrebno je omogućiti dodavanje, uređivanje, brisanje i 
pregledavanje životinja, kategorija,
tagova. """

class Animals(models.Model):

    STATUS_CHOICES = (
        ("PLACED", u'Placed'),
        ("APPROVED", u'Approved'),
        ("DELIVERED", u'Delivered'),
    )


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=False)
    tags = models.CharField(max_length=200)
    status = models.CharField(
    u'Status', max_length=20,
    choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name

    @property
    def pictureURL(self):
        try:
            url = self.pictureURL
        except:
            url= ''
        return url
