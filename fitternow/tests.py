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

        self.assertEqual(self.user.username, 'milkshake')
        self.assertEqual(self.user.first_name, 'joe')
        self.assertEqual(self.user.last_name, 'doe')
        self.assertEqual(self.user.email, 'user@fitternow.com')

        # self.assertEqual(self.user.password, 'pbkdf2_sha256$30000$3GFPgLi8cNYw$Na5f1jfU/jw7TwhhYaGdrmZU76O2h4zIupnt/7ydvOA')
        # UserActivities.objects.perform_create(username='milkshake', activity_name='Archery', duration='2',
        #   calories_burned='300')


class ActivityTestCase(TestCase):

    def setUp(self):
        Activity.objects.create( activity_name='TestActivity', calories=400)
    def test_activity_created(self):
        obj = Activity.objects.get(activity_name='TestActivity')
        self.assertEqual(obj.calories,400)




class UserActivitiesTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='milkshake', first_name='joe', last_name='doe',
                                             email='user@fitternow.com', password='pass123')
        UserActivities.objects.create(user=self.user, activity_name='Archery',
                                                                   duration='2',
                                                                   calories_burned='300')
    def test_useractivity_created(self):
        obj = UserActivities.objects.get(user=self.user)
        self.assertEqual(obj.user,self.user)