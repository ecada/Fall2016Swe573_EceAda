from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.utils import timezone
import json
from fitternow import appviews
from fitternow.models import UserProfile, Activity, UserActivities, ConsumptionHistory, Meals, MealConsumption
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from django.utils import timezone
from datetime import datetime
import unittest
from rest_framework.test import APIClient


class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='milkshake', first_name='joe', last_name='doe',
                                             email='user@fitternow.com', password='pass123')


    def test_token_created(self):

        token = Token.objects.get(user_id=self.user.id)

        self.assertIsNotNone(token)
        self.assertIsNotNone(token.key)
        self.assertEqual(self.user.id, token.user_id)
