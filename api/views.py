from django.shortcuts import render
from .models import New
from .serializers import NewSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiView(request):
        queryset=New.objects.all()
        serializer_class=NewSerializer(queryset,many=True)
       
        return Response({'status':200,'payload':serializer_class.data})

@api_view(['POST'])
def post_data(request):
        data=request.data
        serializer=NewSerializer(data=data)
        if not serializer.is_valid():
            Response({'status':200,'payload':serializer.error})
        serializer.save()
        return Response({'status':200,'payload':data})



# class apiView(generics.ListAPIView):
#         queryset=New.objects.all()
#         serializer_class=NewSerializer()
       


# class post_data(generics.RetrieveAPIView):
#         data=request.data
#         serializer=NewSerializer(data=data)
#         if not serializer.is_valid():
#             Response({'status':200,'payload':serializer.error})
#         serializer.save()
#         return Response({'status':200,'payload':data})

        

def index(request):
    return render(request,"index.html")
