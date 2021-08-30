from django.shortcuts import render
from rest_framework import (
    decorators,
    mixins,
    response,
    viewsets,
)

from . import models, serializers


# Create your views here.
class CompanyViewSet(
    viewsets.GenericViewSet,
):
    """
    Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    @decorators.action(
        methods=['GET'],
        detail=True,
    )
    def employees(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_class = self.get_serializer_class()
        serializer_context = self.get_serializer_context()
        serializer = serializer_class(instance, context=serializer_context)

        return response.Response(serializer.data)
