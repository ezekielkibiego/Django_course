from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from django.urls import reverse

from cloudinary.models import CloudinaryField


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Blog(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    content = models.TextField()
    
    image = CloudinaryField("image",null=True)

    date_posted = models.DateTimeField(default=timezone.now)

    last_updated = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    slug = models.SlugField(unique=True)

    

    class Meta:

        ordering = ['-date_posted']

    

    def __str__(self):

        return self.title

    

    def get_absolute_url(self):

        return reverse('blog-post-detail', kwargs={'slug': self.slug})

    

    @classmethod

    def published(cls):

        return cls.objects.filter(is_published=True)

