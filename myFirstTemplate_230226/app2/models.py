from django.db    import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title    = models.CharField(max_length=200)
    slug     = models.CharField(max_length=200)
    body     = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title



class Product(models.Model):
    PUMPS = (
        ('L', 'Log'   ),
        ('E', 'Erro'  ),
        ('O', 'Other' ),
    )
    title    = models.CharField(max_length=200)
    body     = models.TextField()
    pumps    = models.CharField(max_length=1, choices=PUMPS)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
