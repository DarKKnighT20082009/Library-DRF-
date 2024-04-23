from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_img/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    published_date = models.DateField(auto_now_add=True)

    isbn = models.CharField(max_length=13)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title

