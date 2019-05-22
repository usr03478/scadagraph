from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/index.html', {})


def get_data(request, *args, **kwargs):
    data = {
        "Sales": 100,
        "Clients": 200,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = [] # check blog API, this is pretty important
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count() # actual database info instead of hard coded shit
        lables = ['Users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [qs_count, 234, 231, 532, 112, 321]
        data = {
                "lables": lables,
                "default": default_items,
        }
        return Response(data)