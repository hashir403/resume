from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    email_title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto timestamp

    def __str__(self):
        return f"{self.name} - {self.email_title}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    link = models.URLField(blank=True, null=True)  # optional project link

    def __str__(self):
        return self.title