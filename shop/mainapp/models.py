from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='category')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='slug')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True, verbose_name='name')
    description = models.TextField(verbose_name='description')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='slug')
    image = models.ImageField(upload_to='products/%d/%m/%Y', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

