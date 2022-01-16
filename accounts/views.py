from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token

from django.urls import reverse
from django.contrib.auth.models import User

from accounts.permissions import *
from accounts.serializers import *



class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SellerList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = SellerSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsSellerOrReadOnly]



class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = SellerSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsSellerOrReadOnly]
    



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                            IsProductOwnerOrReadOnly]

    filter_fields = (
        'seller',
    )
    
    ordering_fields = (
        'name',
    )
    



class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsProductOwnerOrReadOnly]
    
    filter_fields = (
        'seller',
    )
    
    ordering_fields = (
        'name',
    )
    