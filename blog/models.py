from datetime import date
from turtle import title
from django.db import models

class Blog(models.Model):
	"""Model definition for Blog."""
	""" Modelo para los blog con que se trabajaran en el proyecto de portafolio. """

	title = models.CharField(max_length=50)
	contentBlog = models.TextField()
	crateDate = models.DateField(default=date.today)
	autor = models.CharField(max_length=50)

	def __str__(self):
		"""Unicode representation of MODELNAME."""

		return self.title
		pass
