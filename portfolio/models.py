from django.db import models

# Create your models here.
class Projects(models.Model):
    domain = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
