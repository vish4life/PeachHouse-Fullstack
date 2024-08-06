from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking
from rest_framework import viewsets,permissions
updtSuccess= "Updated successfully"
updtFailure= "Failed during updated"
deltSuccess= "Deleted successfully"
deltFailure= "Failed during delete"

# Create your views here.
def index(request):
    message="Welcome to Peach House"
    # return HttpResponse(message)
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    permission_classes=[permissions.IsAuthenticated]

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        menuid=self.kwargs['pk']
        print(menuid)
        try:
            return Menu.objects.get(pk=menuid)
        except Menu.DoesNotExist:
            raise NotFound({'message':'No Menu Item found with id: '+str(menuid)},code=status.HTTP_200_OK)
    def update(self, request, *args, **kwargs):
        try:
            super().update(request, *args, **kwargs)
            return Response({"msg":updtSuccess},status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"msg":updtFailure},status=status.HTTP_200_OK)
    def delete(self, request, *args, **kwargs):
        try:
            super().delete(request, *args, **kwargs)
            return Response({"msg":deltSuccess},status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response({"msg":deltFailure},status=status.HTTP_200_OK)

# # we can write in the following way too but for providing proper response, I prefer to use the above way
# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Menu.objects.all()
#     serializer_class=MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]
