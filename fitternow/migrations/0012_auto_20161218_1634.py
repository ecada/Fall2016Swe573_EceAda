# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitternow', '0011_auto_20161213_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumptionHistory',
            fields=[
                ('consumption_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('nbdno', models.CharField(max_length=200)),
                ('food_name', models.CharField(max_length=200)),
                ('food_calories', models.FloatField(default=90)),
                ('calories_unit', models.CharField(default='kcal', max_length=200)),
                ('water', models.FloatField(default=0.0)),
                ('water_unit', models.CharField(default='g', max_length=200)),
                ('protein', models.FloatField(default=0.0)),
                ('protein_unit', models.CharField(default='g', max_length=200)),
                ('fat', models.FloatField(default=0.0)),
                ('fat_unit', models.CharField(default='g', max_length=200)),
                ('carbohydrate', models.FloatField(default=0.0)),
                ('carbohydrate_unit', models.CharField(default='g', max_length=200)),
                ('fiber', models.FloatField(default=0.0)),
                ('fiber_unit', models.CharField(default='g', max_length=200)),
                ('sugars', models.FloatField(default=0.0)),
                ('sugars_unit', models.CharField(default='g', max_length=200)),
                ('calcium', models.FloatField(default=0.0)),
                ('calcium_unit', models.CharField(default='mg', max_length=200)),
                ('iron', models.FloatField(default=0.0)),
                ('iron_unit', models.CharField(default='mg', max_length=200)),
                ('magnesium', models.FloatField(default=0.0)),
                ('magnesium_unit', models.CharField(default='mg', max_length=200)),
                ('phosphorus', models.FloatField(default=0.0)),
                ('phosphorus_unit', models.CharField(default='mg', max_length=200)),
                ('potassium', models.FloatField(default=0.0)),
                ('potassium_unit', models.CharField(default='mg', max_length=200)),
                ('sodium', models.FloatField(default=0.0)),
                ('sodium_unit', models.CharField(default='mg', max_length=200)),
                ('zinc', models.FloatField(default=0.0)),
                ('zinc_unit', models.CharField(default='mg', max_length=200)),
                ('vitaminc', models.FloatField(default=0.0)),
                ('vitaminc_unit', models.CharField(default='mg', max_length=200)),
                ('thiamin', models.FloatField(default=0.0)),
                ('thiamin_unit', models.CharField(default='mg', max_length=200)),
                ('riboflavin', models.FloatField(default=0.0)),
                ('riboflavin_unit', models.CharField(default='mg', max_length=200)),
                ('niacin', models.FloatField(default=0.0)),
                ('niacin_unit', models.CharField(default='mg', max_length=200)),
                ('vitaminb12', models.FloatField(default=0.0)),
                ('vitaminb12_unit', models.CharField(default='mg', max_length=200)),
                ('vitamina', models.FloatField(default=0.0)),
                ('vitamina_unit', models.CharField(default='UI', max_length=200)),
                ('saturated', models.FloatField(default=0.0)),
                ('saturated_unit', models.CharField(default='g', max_length=200)),
                ('monounsaturated', models.FloatField(default=0.0)),
                ('monounsaturated_unit', models.CharField(default='g', max_length=200)),
                ('polyunsaturated', models.FloatField(default=0.0)),
                ('polyunsaturated_unit', models.CharField(default='g', max_length=200)),
                ('trans', models.FloatField(default=0.0)),
                ('trans_unit', models.CharField(default='g', max_length=200)),
                ('cholesterol', models.FloatField(default=0.0)),
                ('cholesterol_unit', models.CharField(default='mg', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MealConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitternow.ConsumptionHistory')),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('meal_id', models.AutoField(primary_key=True, serialize=False)),
                ('meal_name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mealconsumption',
            name='meal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitternow.Meals'),
        ),
    ]
