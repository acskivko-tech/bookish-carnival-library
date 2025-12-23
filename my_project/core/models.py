from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Author(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES, default='other')
    country_of_birth = models.CharField(max_length=100, default='world')
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    """Db validation methods"""
    def clean_first_name(self):
        if self.first_name is None or self.first_name.strip() =='':
            raise ValidationError("Please enter a valid first name.")
        return self.first_name

    def clean_last_name(self):
        if self.last_name is None or self.last_name.strip() == '':
            raise ValidationError("Please enter a valid last name.")
        return self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('draft', 'Draft'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    year_published = models.DateField(null=True)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f'{self.title} by {self.author}, year published: {self.year_published}'

    """Db validation"""
    def clean_title(self):
        if not self.title:
            raise ValidationError('Title cannot be empty')
        return self.title

    def clean_pages(self):
        if not self.pages or self.pages < 0:
            raise ValidationError('Pages cannot be negative or empty')
        return self.pages

    """Actions for db status"""
    def set_status_available(self):
        if self.status == 'available' or self.status == 'unavailable':
            raise ValidationError('Book is unavailable or already available ')
        self.status = 'available'
        self.full_clean()
        self.save()


    def set_status_unavailable(self):
        if self.status == 'unavailable':
            raise ValidationError('Book is unavailable to take')
        self.status = 'unavailable'
        self.full_clean()
        self.save()


    def set_status_draft(self):
        if self.status == 'draft':
            raise ValidationError('Book is already draft')
        self.status = 'draft'
        self.full_clean()
        self.save()
