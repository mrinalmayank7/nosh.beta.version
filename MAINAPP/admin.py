
from django.contrib import admin
from MAINAPP.models import UserProfileInfo , Subscriber ,AutomatedEmail,HealthBlog ,statistic ,UserFeedback ,Program ,Workshop ,WorkshopEnrollment ,Product
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(AutomatedEmail)
admin.site.register(Subscriber)
admin.site.register(HealthBlog)
admin.site.register(statistic)
admin.site.register(UserFeedback)
admin.site.register(Program)
admin.site.register(Workshop)
admin.site.register(WorkshopEnrollment)
admin.site.register(Product)
