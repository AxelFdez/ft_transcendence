from django.db import models

class User(models.Model):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=254, unique=True)
	password = models.CharField(max_length=50)
	avatar = models.ImageField(upload_to='avatars', default='pong/defaultPic.png')
	bio = models.CharField(max_length=254, blank=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username