from django.db import models

# Create your models here.

class Members(models.Model):
    """Thi class represents the members model."""
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    interests = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)