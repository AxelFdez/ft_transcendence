from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatars/', default='avatars/defaultPic.png')
	bio = models.TextField(max_length=420, blank=True)
	games_id = models.ManyToManyField('game.Game', blank=True)
	win = models.IntegerField(default=0)
	lose = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username