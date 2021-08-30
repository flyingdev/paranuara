from rest_framework import (
    decorators,
    mixins,
    response,
    viewsets,
)

from . import models
from .serializers import MutualFriendSerializer, PersonSerializer


class PersonViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    """
    Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common who have brown eyes and are still alive

    Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output:
    {
        "username": "Ahi",
        "age": "30",
        "fruits": [
            "banana",
            "apple",
        ],
        "vegetables": [
            "beetroot",
            "lettuce",
        ]
    }
    """
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_class = self.get_serializer_class()
        serializer_context = self.get_serializer_context()
        serializer = serializer_class(instance, context=serializer_context)

        return response.Response(serializer.data)

    @decorators.action(
        methods=['POST', ],
        detail=False,
        serializer_class=MutualFriendSerializer,
    )
    def mutual_friends(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data)
