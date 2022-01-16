from dataclasses import fields
from accounts.models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    seller = serializers.SlugRelatedField(many=True, read_only=True, slug_field='seller.username')

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'seller')



class SellerSerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'products')