from rest_framework import serializers
from .models import Users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # or specify fields like ['productid', 'productname', 'productprice', 'productquantity']