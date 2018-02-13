from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Discussion(models.Model):

	d_type = (
			('article', 'Article'),
			('blog', 'Blog'), 
			('question', 'Question'),
			('post','Post'),
		)


	title = models.CharField(max_length=200)
	text = models.TextField()
	d_type = models.CharField(choices=d_type, max_length=10)
	added_by = models.ForeignKey(User)
    is_published = models.BooleanField(default = True)
	created_date = models.DateTimeField(default=timezone.now)
	modified_date = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	image = models.ImageField(upload_to='post_images/', null=True, blank=True)


	def __str__(self):
		return self.title


class Comment(models.Model):
	discussion = models.ForeignKey(Discussion)
	text = models.TextField()
	added_by = models.ForeignKey(User)
    created_date = models.DateTimeField(default = timezone.now)
    modified_date = models.DateTimeField(default = timezone.now)



	def __str__(self):
		return self.discussion.title + '-' + self.text