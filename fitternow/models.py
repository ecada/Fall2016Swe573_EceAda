from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

#built in django

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class UserProfile(models.Model):
    #user_profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(default='1900-01-22')
    gender = models.CharField(max_length=1, choices=(('F','FEMALE'),('M','MALE')), default='F')
    height = models.FloatField(default=170)
    weight = models.FloatField(default=60)
    user_notes = models.TextField(blank=True,null=True)
    secure_quest = models.CharField(max_length=200)
    secure_answer = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.user,self.gender,self.height,self.weight,self.user_notes,self.secure_quest,self.secure_answer)



class ConsumptionHistory(models.Model):
    consumption_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    nbdno = models.CharField(max_length=200)
    food_name = models.CharField(max_length=200)
    food_calories = models.FloatField(default=90)
    calories_unit = models.CharField(max_length=200,default='kcal')
    water = models.FloatField(default=0.0)
    water_unit = models.CharField(max_length=200,default='g')
    protein = models.FloatField(default=0.0)
    protein_unit = models.CharField(max_length=200,default='g')
    fat = models.FloatField(default=0.0)
    fat_unit = models.CharField(max_length=200,default='g')
    carbohydrate = models.FloatField(default=0.0)
    carbohydrate_unit = models.CharField(max_length=200, default='g')
    fiber = models.FloatField(default=0.0)
    fiber_unit = models.CharField(max_length=200,default='g')
    sugars = models.FloatField(default=0.0)
    sugars_unit = models.CharField(max_length=200,default='g')
    calcium = models.FloatField(default=0.0)
    calcium_unit = models.CharField(max_length=200,default='mg')
    iron = models.FloatField(default=0.0)
    iron_unit = models.CharField(max_length=200,default='mg')
    magnesium = models.FloatField(default=0.0)
    magnesium_unit = models.CharField(max_length=200,default='mg')
    phosphorus = models.FloatField(default=0.0)
    phosphorus_unit = models.CharField(max_length=200, default='mg')
    potassium = models.FloatField(default=0.0)
    potassium_unit = models.CharField(max_length=200, default='mg')
    sodium = models.FloatField(default=0.0)
    sodium_unit = models.CharField(max_length=200,default='mg')
    zinc = models.FloatField(default=0.0)
    zinc_unit = models.CharField(max_length=200, default='mg')
    vitaminc = models.FloatField(default=0.0)
    vitaminc_unit = models.CharField(max_length=200, default='mg')
    thiamin = models.FloatField(default=0.0)
    thiamin_unit = models.CharField(max_length=200, default='mg')
    riboflavin = models.FloatField(default=0.0)
    riboflavin_unit = models.CharField(max_length=200, default='mg')
    niacin = models.FloatField(default=0.0)
    niacin_unit = models.CharField(max_length=200, default='mg')
    vitaminb12 = models.FloatField(default=0.0)
    vitaminb12_unit = models.CharField(max_length=200, default='mg')
    vitamina = models.FloatField(default=0.0)
    vitamina_unit = models.CharField(max_length=200, default='UI')
    saturated = models.FloatField(default=0.0)
    saturated_unit = models.CharField(max_length=200, default='g')
    monounsaturated = models.FloatField(default=0.0)
    monounsaturated_unit = models.CharField(max_length=200, default='g')
    polyunsaturated = models.FloatField(default=0.0)
    polyunsaturated_unit = models.CharField(max_length=200, default='g')
    trans = models.FloatField(default=0.0)
    trans_unit = models.CharField(max_length=200, default='g')
    cholesterol = models.FloatField(default=0.0)
    cholesterol_unit = models.CharField(max_length=200, default='mg')

class Meals(models.Model):
    meal_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=200)


class MealConsumption(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    consumptionhistory = models.ForeignKey(ConsumptionHistory, on_delete=models.CASCADE)

class Activity(models.Model):
    act_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=200)
    calories = models.FloatField(default=200)

    def __str__(self):
        return ' %s %s ' % (self.activity_name, self.calories)

class UserActivities(models.Model):
    user_act_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    duration = models.FloatField(default=1)
    calories_burned = models.FloatField(default=100)

    def __str__(self):
        return ' %s %s %s %s %s' % (self.user_act_id, self.user,self.activity_name,self.date_created,self.duration)




