from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle' , 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak"
                }
            )
        return data
    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notogri kiritilgan"
                }
            )
class CashSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=150)
    output = serializers.CharField(max_length=120)