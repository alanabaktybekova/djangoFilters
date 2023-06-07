from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150)
    article = models.CharField(max_length=40, unique=True)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    expiring_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f'Продукты - {self.title}'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_date']
