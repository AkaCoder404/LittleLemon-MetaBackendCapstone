from rest_framework.serializers import ModelSerializer
from .models import MenuItem

class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        