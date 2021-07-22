from django.shortcuts import render
from . import forms
from .models import *
from MAINAPP.forms import UserForm ,UserProfileInfoForm ,SubscriberForm ,UserFeedbackForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.
def home(request):
	tips = HealthBlog.objects.all()
	topics =reversed(HealthBlog.objects.all().order_by('id'))
	stats =statistic.objects.all()
	plans = Program.objects.all()
	fnps=Workshop.objects.all()

	nf_form = forms.SubscriberForm()
	if request.method =='POST':
		nf_form = forms.SubscriberForm(request.POST)
		to = request.POST['email']
		subject = AutomatedEmail.objects.values_list('subject', flat=True)[0]
		body = AutomatedEmail.objects.values_list('body', flat=True)[0]
		send_mail(subject, body,'nosh.beta.version@gmail.com',[to,],fail_silently=False)
		if nf_form.is_valid():
			nf_form.save()
			messages.info(request,"Successfully subscribed !")
			return HttpResponseRedirect(reverse('home'))
		else:
			messages.error(request,"Invalid Details")
			return HttpResponseRedirect("home")


	return render(request, 'MAINAPP/home.html',{'nf_form':nf_form,'tips':tips, 'topics':topics,'stats':stats ,'plans':plans,'fnps':fnps})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


def register(request):
	registered = False
	if request.method =='POST':
		user_form =UserForm(data = request.POST)
		profile_form =UserProfileInfoForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid() :
			 user =user_form.save()
			 user.set_password(user.password)
			 user.save()

			 profile =profile_form.save(commit=False)
			 profile.user = user
			 profile.save()

			 registered = True
			 messages.info(request,"Successfully Registered")
		else:
			print(user_form.errors ,profile_form.errors)
	else :
		user_form =UserForm
		profile_form = UserProfileInfoForm
	return render(request ,'MAINAPP/register.html',{'user_form': user_form ,'profile_form' : profile_form,'registered' : registered })



def user_login(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username , password=password )

		if user:
			if user.is_active:
				login(request , user)
				return HttpResponseRedirect(reverse('home'))

			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
		else:
			messages.error(request,"Invalid login details.")
			return HttpResponseRedirect("/user_login")
	else:
		return render(request , 'MAINAPP/login.html',{})



def health_blog(request):

	tips = HealthBlog.objects.all()
	context = {'tips':tips}
	return render(request, 'MAINAPP/healthtip.html', context)

def read_more(request ,id):
	tips = HealthBlog.objects.get(id=id)
	topics =reversed(HealthBlog.objects.all().order_by('id'))
	context = {'tips':tips ,'topics':topics}
	return render(request, 'MAINAPP/read_more.html', context)

def programs(request):

	plans = Program.objects.all()
	topics =reversed(HealthBlog.objects.all().order_by('id'))
	context = {'plans':plans ,'topics':topics}
	return render(request, 'MAINAPP/programs.html', context)

def view_program(request ,id):
	plans = Program.objects.get(id=id)
	topics =reversed(HealthBlog.objects.all().order_by('id'))
	context = {'plans':plans ,'topics':topics}
	return render(request, 'MAINAPP/view_program.html', context)

def search(request):
	query=request.GET['query']
	tips_name = HealthBlog.objects.filter(name__icontains=query)
	tips_caption = HealthBlog.objects.filter(caption__icontains=query)
	tips_posted_on = HealthBlog.objects.filter(posted_on__icontains=query)
	tips_posted_by = HealthBlog.objects.filter(posted_by__icontains=query)
	tips_introduction = HealthBlog.objects.filter(introduction__icontains=query)
	tips_description = HealthBlog.objects.filter(description__icontains=query)
	tips_conclusion = HealthBlog.objects.filter(conclusion__icontains=query)
	tips =tips_name.union(tips_caption,tips_posted_on,tips_posted_by,tips_introduction ,tips_description ,tips_conclusion)


	plans_Q1=Program.objects.filter(plan_name__icontains=query)
	plans_Q2=Program.objects.filter(about_plan__icontains=query)
	plans_Q3=Program.objects.filter(plan_introduction__icontains=query)
	plans_Q4=Program.objects.filter(plan_description_A__icontains=query)
	plans_Q5=Program.objects.filter(plan_description_B__icontains=query)
	plans_Q6=Program.objects.filter(plan_conclusion__icontains=query)
	plans =plans_Q1.union(plans_Q2,plans_Q3,plans_Q4,plans_Q5,plans_Q6)

	items_Q1=Product.objects.filter(product_name__icontains=query)
	items_Q2=Product.objects.filter(product_caption__icontains=query)
	items_Q3=Product.objects.filter(product_colors_available__icontains=query)
	items_Q4=Product.objects.filter(product_introduction__icontains=query)
	items_Q5=Product.objects.filter(product_sub_heading__icontains=query)
	items_Q6=Product.objects.filter(product_sub_body__icontains=query)
	items_Q7=Product.objects.filter(product_conclusion__icontains=query)
	items_Q8=Product.objects.filter(product_price__icontains=query)
	items =items_Q1.union(items_Q2,items_Q3,items_Q4,items_Q5,items_Q6 ,items_Q7 ,items_Q8)
	context = {'tips':tips ,'plans':plans,'query':query ,'items':items}
	return render(request, 'MAINAPP/search.html',context)

def contact(request):

	feed_form = forms.UserFeedbackForm()
	if request.method =='POST':
		feed_form = forms.UserFeedbackForm(request.POST)

		if feed_form.is_valid():
			feed_form.save()
			messages.info(request,"Successfully submitted !")
			return HttpResponseRedirect(reverse('contact'))
		else:
			messages.error(request,"Invalid Details")
			return HttpResponseRedirect("/contact")
	return render(request, 'MAINAPP/contact.html',{'feed_form':feed_form})


def about(request):
	stats =statistic.objects.all()
	context = {'stats':stats}
	return render(request, 'MAINAPP/about.html', context)

def developer(request):
	context = {}
	return render(request, 'MAINAPP/developer.html', context)

def privacy(request):
	context = {}
	return render(request, 'MAINAPP/privacy.html', context)

def  page_not_found(request ,exception=None):
	return render(request, 'MAINAPP/404.html')

def  enrollsuccess(request):
	fnps=Workshop.objects.all()
	context = {'fnps':fnps}
	return render(request, 'MAINAPP/enrollsuccess.html',context)

def  workshop(request):
	fnps=Workshop.objects.all()
	enroll_form = forms.Workshop_EnrollmentForm()
	if request.method =='POST':
		enroll_form = forms.Workshop_EnrollmentForm(request.POST)
		if enroll_form.is_valid():
			enroll_form.save()
			return HttpResponseRedirect(('/enrollsuccess'))
		else:
			messages.error(request,"Something went wrong , please try again.")
			return HttpResponseRedirect("/FNP")
	context = {'fnps':fnps ,'enroll_form':enroll_form}
	return render(request, 'MAINAPP/workshop.html' ,context)

def  product(request):
	items=Product.objects.all()
	context = {'items':items}
	return render(request, 'MAINAPP/product.html' ,context)

def  product_detail(request ,id):
	items=Product.objects.get(id=id)
	context = {'items':items}
	return render(request, 'MAINAPP/product_detail.html' ,context)
