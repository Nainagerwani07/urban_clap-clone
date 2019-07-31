from django.conf.urls import url
from django.urls import include
from django.urls import path

from . import views

urlpatterns = [
	url(r'^$' , views.formView, name='formView'),
	path('login/',views.CustomerLogin,name='login'),
	path('login/<str:name>/',views.homeeee,name='homeeee'),
	path('index/',views.index, name='index'),
	path('customer/', views.CustomerRegister, name='customer' ),
	path('customer_error/<str:e>/', views.customer_error,name='customer_error'),
	path('register/',views.register,name='register'),
	path('CustomerRegister/',views.CustomerRegister,name='CustomerRegister'),
	path('service/' , views.service, name='service' ),
	path('service_error/<str:error>/' , views.service_error, name='service_error' ),
	path('service_provider_register/' , views.service_provider_register, name='service_provider_register' ),
	path('Service_provider_Login/' , views.Service_provider_Login, name='Service_provider_Login' ),
	path('logout/',views.CustomerLogout, name='logout'),
	path('add_services/' , views.add_services, name='add_services' ),
	path('add/<str:error>/' , views.add, name='add' ),
	path('deactive_account/' , views.deactive_account, name='deactive_account' ),
	path('crequest/<int:sid>/',views.Customer_Request,name='crequest'),
	path('ccancel/<int:sid>/',views.Customer_Request_delete,name='ccancel'),

	path('service_accept/<int:rid>/<int:sid>/',views.service_accept,name='service_accept'),
	path('service_complete/<int:rid>/<int:sid>/',views.service_complete,name='service_complete'),

	path('service_reject/<int:rid>/<int:sid>/',views.service_reject,name='service_reject'),

	path('review/<int:rid>/<int:sid>/',views.review,name='review'),

	path('home_error/<str:e>/',views.home_error,name='home_error'),

	
	path('home_status/<str:s>/<int:rid>/',views.home_status,name='home_status'),

	

	# path('crequest/<int:sid>/',views.Customer_Request,name='crequest'),







	# path('customer/login/logout/',views.CustomerLogout),
	# path('customer/Salon_at_Home/',views.Salon_at_home),
	# path('customer/login/Salon_at_Home/',views.Salon_at_home),
	# path('customer/login/Salon_at_Home/salon/',views.salon, name='salon-url'),
	# path('customer/login/Salon_at_Home/salon1/',views.salon1, name='salon1-url'),
	# path('customer/login/Massage_at_Home/',views.Massage_at_Home),
	# path('customer/login/Appliance_Electronic_Repair/',views.Appliance_Electronic_Repair),
	# path('customer/login/Cleaning/',views.Cleaning),
	# path('customer/login/Electrician_Plumber_Carpenter/',views.Electrician_Plumber_Carpenter),
	# path('customer/login/Fitness_Yoga/',views.Fitness_Yoga),
	# path('service_provider/logout/',views.ProviderLogout),
	# path('service_provider/login/',views.Service_provider_Login),
	# path('service_provider/login/add_service/',views.Add_Services),
	# path('customer/login/Salon_at_Home/sss/',views.sss, name='sss'),


]	