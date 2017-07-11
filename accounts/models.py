from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class Profile(models.Model):
    SERVER_CHOICES = (
        ('울프', '울프'),
        ('만돌린', '만돌린'),
        ('하프', '하프'),
        ('류트', '류트'),
    )
    RACE_CHOICES = (
        ('인간', '인간'),
        ('엘프', '엘프'),
        ('자이언트', '자이언트'),
    )
    SKILL_CHOICES =(
            ('근접 전투','근접 전투'),
			('랜스','랜스'),
			('궁술','궁술'),
			('마법','마법'),
			('격투술','격투술'),
         	('연금술','연금술'),
		 	('올라운더','올라운더')
    )
    server = models.CharField(max_length=3, choices=SERVER_CHOICES)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    userid = models.CharField(max_length=20)
    race = models.CharField(max_length=4, choices=RACE_CHOICES)
    skill = models.CharField(max_length=10, choices=SKILL_CHOICES)
    context = models.CharField(max_length=300, blank=True)
    image = ProcessedImageField(blank=True,
            processors=[Thumbnail(350, 350)],
            format='JPEG',
            options={'quality': 80})
