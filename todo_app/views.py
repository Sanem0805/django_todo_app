from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from  django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import ToDo
from .serializers import ToDoSerializer, UpdateToDoSerializer


@api_view(['GET'])
def get_todos(request: Request):
    queryset = ToDo.objects.all()
    # SELECT * FROM todo -> QuerySet([{title..., desc...}])
    print(queryset)
    serializer = ToDoSerializer(queryset, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='POST', request_body=ToDoSerializer)
@api_view(['POST'])
def create_todo(request: Request) -> Response:
    serializer = ToDoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    todo = ToDo.objects.create(**serializer.data)
    todo.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
    # serializer.is_valid(raise_exception=True)
    # if serializer.is_valid():
    #     todo = ToDo.objects.crete(**serializer.data)
    #     todo.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', request_body=ToDoSerializer)
@api_view(['PATCH'])
def update_todo(request: Request, pk) -> Response:
    print(pk)
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response({'detail': f'ToDo with {pk} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializser = UpdateToDoSerializer(
        instance=todo,
        data=request.data
    )
    serializser.is_valid(raise_exception=True)
    serializser.save()
    return Response(serializser.data, status=status.
    HTTP_200_OK)

@api_view(['DELETE'])
def delete_todo(request: Response, pk) -> Response:
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response({'detail': f'ToDo with {pk} does not exist'}, status=status.HTTP_404_NOT_FOUND)
    todo.delete()
    return Response({'detail': 'Successfully deleted'},
    status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_todo(requests: Request, pk) -> Response:
    todo = get_object_or_404(ToDo, pk=pk)
    serializer = ToDoSerializer(instance=todo)
    return Response(serializer.data, status=status.HTTP_200_OK)


# TODO: написать функцию для получения одного объекта
#TODO: подключить Swagger
# django rest swager df