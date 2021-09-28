from rest_framework import serializers
from .models import classroom, EBooksModel


class classroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        #  fields=('classname','creator')
        fields = '__all__'
        extra_kwargs = {
            "user_profile": {"required": False},
        }

class AccountPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        fields = '__all__'

class pdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBooksModel
        fields = '__all__'
"""""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "num_pages",
            "isbn13"
        ]
        extra_kwargs = {
            "isbn13": {"required": False},
        }
"""""