from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExampleModel
from .serializers import ExampleSerializer


@api_view(["GET", "POST"])
def example_view(request, id=0):
    if request.method == "GET":
        if id == 0:
            query_set = ExampleModel.objects.all()
            serializer = ExampleSerializer(query_set, many=True)
        else:
            obj = ExampleModel.objects.get(id=id)
            serializer = ExampleSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    else:
        data = request.data
        serializer = ExampleSerializer(data=data)
        if serializer.is_valid():
            name = serializer.data.get("name")
            level = serializer.data.get("level")
            degree = serializer.data.get("degree")
            place = serializer.data.get("place")
            date = serializer.data.get("date")
            row = ExampleModel(name=name, level=level, degree=degree, place=place, date=date)
            row.save()
            return JsonResponse(ExampleSerializer(row).data,status=status.HTTP_201_CREATED)

        return HttpResponse({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
