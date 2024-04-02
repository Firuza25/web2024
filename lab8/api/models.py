from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 300)

    def __str__(self) -> str:
        return self.name


    def to_json(self) -> str:
        return {
            'name': self.name,
        }
    
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default=1)# когда мы каждый раз удаляем продукт нам нужен этот файл каскад

    def __str__(self) -> str:
        return self.name
    
    def to_json(self):
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
        }