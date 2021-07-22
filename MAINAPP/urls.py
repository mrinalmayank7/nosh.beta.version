from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('register/', views.register,name='register'),
	path('user_login/', views.user_login,name='user_login'),
	path('logout/', views.user_logout,name='logout'),
	path('health_blog/', views.health_blog,name='health_blog'),
	path('<int:id>/read_more/', views.read_more, name="read_more"),
	path('programs/', views.programs,name='programs'),
	path('<int:id>/view_program/', views.view_program, name="view_program"),
	path('contact/', views.contact,name='contact'),
	path('about/', views.about,name='about'),
	path('search/', views.search,name='search'),
	path('developer/', views.developer,name='developer'),
	path('FNP/', views.workshop,name='workshop'),
	path('enrollsuccess/', views.enrollsuccess,name='enrollsuccess'),
	path('product/', views.product,name='product'),
	path('<int:id>/product_detail/', views.product_detail, name="product_detail"),
	path('privacy/', views.privacy,name='privacy'),
	path('404/',views.page_not_found),

	path('reset_password/', auth_views.PasswordResetView.as_view(template_name='MAINAPP/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='MAINAPP/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='MAINAPP/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='MAINAPP/password_reset_complete.html'), name='password_reset_complete'),]
