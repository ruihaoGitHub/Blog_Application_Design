from django.db import models
from django.contrib.auth.models import User
import math


class BlogPost(models.Model):
    """A model for a single blog post."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    header_image = models.ImageField(upload_to='images/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    @property
    def reading_time(self):
        """Estimate the reading time in minutes."""
        word_count = len(self.text.split())
        # Assuming average reading speed of 200 words per minute
        minutes = math.ceil(word_count / 200)
        return max(1, minutes)