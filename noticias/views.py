from rest_framework import viewsets, status
from rest_framework import status
from django.shortcuts import render
from rest_framework import generics, status
from .models import Noticia
from .serializers import NoticiaSerializer


from rest_framework.response import Response
from rest_framework.views import APIView


# class NoticiaViewSet(viewsets.ModelViewSet):
#     queryset = Noticia.objects.all()
#     serializer_class = NoticiaSerializer

#     def create(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgregarNoticia(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NoticiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EliminarNoticia(APIView):
    def post(self, request, *args, **kwargs):
        try:
            noticia = Noticia.objects.get(id=request.data['id'])
            noticia.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Noticia.DoesNotExist:
            return Response({'error': 'Noticia no encontrada'}, status=status.HTTP_404_NOT_FOUND)


class ModificarNoticia(APIView):
    def post(self, request, *args, **kwargs):
        try:
            noticia = Noticia.objects.get(id=request.data['id'])
        except Noticia.DoesNotExist:
            return Response({'error': 'Noticia no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoticiaSerializer(
            noticia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListarNoticias(APIView):
    def post(self, request, *args, **kwargs):
        noticias = Noticia.objects.all()
        serializer = NoticiaSerializer(noticias, many=True)
        return Response(serializer.data)
