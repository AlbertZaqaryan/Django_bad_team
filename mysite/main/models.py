from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=50)
    slug = models.SlugField('Slug name', unique=True)

    def __str__(self):
        return self.name

class Notebook(models.Model):
    
    COLOR_CHOICES = (
        ('Gray', 'gray'),
        ('Purple', 'purple'),
        ('Black', 'black'),
        ('Red', 'red'),
        ('Yellow', 'yellow'),
        ('White', 'white')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Notebook name', max_length=50)
    price = models.PositiveIntegerField('Notebook price')
    img = models.ImageField('Notebook image', upload_to='media/notebooks/')
    color = models.CharField(choices=COLOR_CHOICES, max_length=80)

    def __str__(self):
        return f'{self.name} - {self.price}(dram)'