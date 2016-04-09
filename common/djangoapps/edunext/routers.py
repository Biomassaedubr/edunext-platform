#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import routers
from viewsets import (
    UsersViewSet,
)


router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
