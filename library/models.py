from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=400)
    authors = models.CharField(max_length=120)
    average_rating = models.FloatField(default=0)
    isbn = models.CharField(max_length=100)
    isbn13 = models.CharField(max_length=100)
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField(default=0)
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=400)


    class Meta:
        db_table = 'library_books'