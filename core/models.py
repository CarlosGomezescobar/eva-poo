from urllib import request
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Connection:
    
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def establish_connection(self):
        try:
            self.connection = requests.get(self.url, headers=self.headers)
            if self.connection.status_code == 200:
                return True
            else:
                return False
        except request.exceptions.ConnectionError:
            return False

    def verify_connection(self):
        return self.connection.status_code == 200
class CategoryList:
    
    def __init__(self, connection):
        self.connection = connection

    def get_categories(self):
        response = self.connection.json()
        categories = []
        for category in response:
            categories.append(category)
        return categories

    def show_categories(self):
        for category in self.get_categories():
            print(category['name'])
            
class CategoryDetail:
    
    def __init__(self, connection, category_id):
        self.connection = connection
        self.category_id = category_id

    def get_detail(self):
        response = self.connection.get(f'{self.connection.url}/{self.category_id}')
        category = response.json()
        return category

    def show_detail(self):
        category = self.get_detail()
        print(category['name'])
        print(category['description'])
        
class Menu:
    
    def __init__(self):
        self.options = ['Ver listado de categorías', 'Ver detalle de una categoría']

    def show_options(self):
        for option in self.options:
            print(option)

    def execute_option(self, option):
        if option == 'Ver listado de categorías':
            print('Listado de categorías:')
            CategoryList(Connection(API_URL, API_HEADERS)).show_categories()
        elif option == 'Ver detalle de una categoría':
            print('Elija una categoría:')
            category_id = input()
            CategoryDetail(Connection(API_URL, API_HEADERS), category