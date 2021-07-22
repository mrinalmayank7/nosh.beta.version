from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextField
from django.utils import timezone

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	#additional
	name = models.CharField(max_length= 200)
	phone = models.CharField(max_length=12,blank=True)

	def __str__(self):
		return self.user.username

class Subscriber(models.Model):
	name = models.CharField(max_length= 200)
	email=models.EmailField(max_length =200)

	def __str__(self):
		return self.name

class AutomatedEmail(models.Model):
	name = models.CharField(max_length=300 ,blank=True)
	subject = models.TextField(blank=True)
	body = models.TextField(blank=True)

	def __str__(self):
		return self.name


class HealthBlog(models.Model):
	name = models.CharField(max_length=200,blank=True,help_text="Keep name short(max 4 to 5 words)")
	caption = models.CharField(max_length=500,blank=True,help_text="Keep caption short(max 2 lines)")
	posted_on=models.DateField(blank=True,default=timezone.now,help_text="mandatory field")
	posted_by =models.CharField(max_length=200,blank=True,help_text="Add author name")
	introduction =models.TextField(blank=True,help_text="this text will be visible in flip card back")
	description =models.TextField(blank=True ,help_text="this text will be visible  in read more")
	conclusion=models.TextField(blank=True , help_text="this text will be visible in read more")
	image = models.ImageField(null=True, blank=True , help_text="crop image as square before upload to get uniform size in the page")
	add_to_home = models.BooleanField(default=False,null=True, blank=True ,help_text="Yes will enable to display it on home page (display max 6 posts in home page)")

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class statistic(models.Model):
	name = models.CharField(max_length=300 ,blank=True)
	count = models.CharField(max_length=300)
	label =models.CharField(max_length=300 ,blank=True)

	def __str__(self):
		return self.name

class UserFeedback(models.Model):
	reviewer_name = models.CharField(max_length= 200 ,blank=True)
	reviewer_email=models.EmailField(max_length =200 ,blank=True)
	reviewer_message = models.TextField(max_length=2000,blank=True)

	def __str__(self):
		return self.reviewer_name

class Program(models.Model):
	plan_name = models.CharField(max_length=300,blank=True)
	about_plan=models.TextField(blank=True,help_text="Keep it short")
	plan_introduction =models.TextField(blank=True ,help_text="mandatory field")
	plan_description_A=models.TextField(blank=True,help_text="What our plans include (mandatory field)")
	plan_description_B=models.TextField(blank=True,help_text="How our plan works (mandatory field)")
	plan_conclusion=models.TextField(blank=True ,help_text="You can also use it as end note , it appears in bold (not a mandatory field)")
	plan_image = models.ImageField(null=True, blank=True , help_text="crop image as square before upload to get uniform size in the page")
	add_plan_to_home = models.BooleanField(default=False,null=True, blank=True ,help_text="Yes will enable to display it on home page (display max 3 plans in home page)")

	def __str__(self):
		return self.plan_name

	@property
	def plan_imageURL(self):
		try:
			url = self.plan_image.url
		except:
			url = ''
		return url


class Workshop(models.Model):
	workshop_name = models.CharField(max_length= 300)
	workshop_duration = models.CharField(max_length= 300 ,blank=True,help_text="workshop duration in days")
	workshop_caption=models.TextField(blank=True ,help_text="Keep short , one to two lines")
	workshop_introduction=models.TextField(blank=True)
	sub_heading1 =models.CharField(max_length= 300 ,blank=True)
	sub_body1 =models.TextField(blank=True)
	sub_heading2 =models.CharField(max_length= 300 ,blank=True)
	sub_body2 =models.TextField(blank=True)
	workshop_end_paragraph_heading =models.CharField(max_length= 300 ,blank=True, help_text="Appers at the end")
	workshop_end_paragraph_body =models.TextField(blank=True)
	enable_home = models.BooleanField(default=False,null=True, blank=True ,help_text="Yes will enable to display it on home page")
	enable_enrollment = models.BooleanField(default=True,null=True, blank=True ,help_text="Yes will enable enrollment ,No will disable enrollment")
	def __str__(self):
		return self.workshop_name

class WorkshopEnrollment(models.Model):
	participant_name= models.CharField(max_length=300)
	participant_email= models.EmailField(max_length=300)
	participant_phone =models.CharField(max_length=12 ,blank=True )
	enrolled_on=models.DateField(blank=True,default=timezone.now)
	def __str__(self):
		return self.participant_name

class Product(models.Model):
	product_name = models.CharField(max_length= 300)
	product_caption=models.TextField(blank=True ,help_text="Keep short , one to two lines")
	product_colors_available=models.CharField(max_length= 400 ,blank=True)
	product_price=models.CharField(max_length= 400 ,blank=True)
	product_introduction=models.TextField(blank=True)
	product_sub_heading =models.CharField(max_length= 300 ,blank=True,help_text="If you have a detailed description of product with sub heading add here")
	product_sub_body =models.TextField(blank=True ,help_text="Describe product  if have a detailed description")
	product_conclusion =models.TextField(blank=True ,help_text="You can use the conclusion as end note or any important message at the end")
	product_image = models.ImageField(null=True, blank=True , help_text="crop image as square before upload to get uniform size in the page")

	def __str__(self):
		return self.product_name

	@property
	def product_imageURL(self):
		try:
			url = self.product_image.url
		except:
			url = ''
		return url
