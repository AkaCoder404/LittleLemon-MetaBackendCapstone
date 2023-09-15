from django.shortcuts import render


# Create your views here.



from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import MenuSerializer
from .models import MenuItem

class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})
