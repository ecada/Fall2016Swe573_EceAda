from django.contrib import admin
#from .models import UserActivities

#admin.site.register(UserActivities)
from fitternow.models import UserProfile,Activity,UserActivities,ConsumptionHistory, Meals, MealConsumption

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(UserActivities)
admin.site.register(ConsumptionHistory)
admin.site.register(Meals)
admin.site.register(MealConsumption)




# Register your models here.
