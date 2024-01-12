from django.db import models
from django.conf import settings

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
	bio = models.TextField(max_length=420, blank=True)