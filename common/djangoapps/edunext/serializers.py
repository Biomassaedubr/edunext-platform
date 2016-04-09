#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from fields import CustomRelatedField


class UserSerializer(serializers.Serializer):
    """Serializer for the nested set of variables a user may include

    """
    # ####################################
    # From django.contrib.auth.models.User
    # ####################################

    username = serializers.CharField(max_length=200, read_only=True)
    first_name = serializers.CharField(max_length=200, read_only=True)
    last_name = serializers.CharField(max_length=200, read_only=True)
    email = serializers.CharField(max_length=200, read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    # #################################################
    # From common.djangoapps.student.models.UserProfile
    # #################################################

    name = serializers.CharField(max_length=255, source="profile.name", read_only=True)
    meta = serializers.CharField(source="profile.meta", read_only=True)  # JSON dictionary for future expansion
    # courseware = models.CharField(blank=True, max_length=255, default='course.xml')  # TODO: what is this?
    language = serializers.CharField(max_length=255, source="profile.language", read_only=True)
    location = serializers.CharField(max_length=255, source="profile.location", read_only=True)
    year_of_birth = serializers.IntegerField(source="profile.year_of_birth", read_only=True)
    # gender = models.CharField(
    #     blank=True, null=True, max_length=6, db_index=True, choices=GENDER_CHOICES
    # )
    # level_of_education = models.CharField(  # TODO: what do we do with choices?
    #     blank=True, null=True, max_length=6, db_index=True,
    #     choices=LEVEL_OF_EDUCATION_CHOICES
    # )
    mailing_address = serializers.CharField(source="profile.mailing_address", read_only=True)
    city = serializers.CharField(source="profile.city", read_only=True)
    country = serializers.CharField(source="profile.country", read_only=True)
    goals = serializers.CharField(source="profile.goals", read_only=True)
    # allow_certificate = models.BooleanField(default=1)  # TODO: what is this?
    bio = serializers.CharField(source="profile.bio", max_length=3000, read_only=True)

    # # Methods for convenience. TODO: should we add this?
    # has_profile_image
    # age
    # level_of_education_display
    # gender_display
    # get_meta

    # ######################################################
    # From common.djangoapps.student.models.UserSignupSource
    # ######################################################

    site = CustomRelatedField(source='usersignupsource_set', field='site', many=True)
