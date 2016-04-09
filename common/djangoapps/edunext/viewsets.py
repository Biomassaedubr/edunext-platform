#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User

from serializers import UserSerializer
from microsite_api.authenticators import MicrositeManagerAuthentication


class UsersViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset for viewing and editing microsites.
    """
    authentication_classes = (MicrositeManagerAuthentication,)
    # permission_classes = (AccountPermission,)  # We need to authorize the request based on the microsite?

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
