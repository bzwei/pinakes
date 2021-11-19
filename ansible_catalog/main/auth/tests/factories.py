"""Factories for auth objects"""
import uuid

import factory
from django.utils import timezone as django_tz

from ansible_catalog.main.auth.models import Group


class GroupFactory(factory.django.DjangoModelFactory):
    """Group Factory"""

    class Meta:
        model = Group

    id = factory.LazyFunction(lambda: str(uuid.uuid4()))
    name = factory.Sequence("group-{}".format)
    path = factory.Sequence("/group-{}".format)
    last_sync_time = factory.LazyFunction(django_tz.now)