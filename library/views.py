from django.shortcuts import render
from django.views import View
from .models import Book
import urllib.request
import json
import datetime


class BookView(View):

    def get(self, request):
        url_api = 'https://silabuzinc.github.io/books/books.json'

        response = urllib.request.urlopen(url_api)
        books = json.loads(response.read())
        # lista de objectos (lista de diccionarios)
        print(len(books))
        for book in books:
            book.pop('FIELD13')
            book.pop('bookID')
            book["authors"] = book["authors"][:100]
            array_dates = book["publication_date"].split("/")
            if len(book["publication_date"]) == 3:
                date_str = ''
                date_str += array_dates[2] + '-'
                date_str += array_dates[0] + '-'
                date_str += array_dates[1]
                book["publication_date"] = date_str
            else:
                book["publication_date"] = datetime.date(2000, 8, 10)
            if len(book["language_code"]) > 10:
                book["language_code"] = 'eng' 
            try:
                book["average_rating"] = float(book["average_rating"])
                book["num_pages"] = int(book["num_pages"])
               
                Book.objects.create(**book)
            except ValueError:
                book["num_pages"] = 0
                book["average_rating"] = 3.5
                Book.objects.create(**book)
            
        return render(request, 'library/index.html')

    def post(self, request):
        pass