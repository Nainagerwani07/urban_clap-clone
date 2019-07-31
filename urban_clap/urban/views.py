from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.shortcuts import get_object_or_404

import hashlib
from jake import get_base64_hashed
from jake import give_back_hashed


from urban.models import UserInformation, ServiceProviderInformation, AddService , CustomerRequest 


# Create your views here.

def formView(request):

	print('formview')
	if request.session.get('username'):
		name = request.session.get('username')
		print('------')
		return redirect('homeeee', name=name)
	else:
		return redirect('index')

def index(request):
	return render(request , 'urban/base.html')


def homeeee(request , name):
	if request.session.get('username'):
   		name = request.session.get('username')
   		service = AddService.objects.all()

   		my_name = User.objects.all()

   		cus_request = CustomerRequest.objects.all()
   		spn = User.objects.get(username=name)
   		sid = spn.id
   		service_provider = False
   		try :
   			s_id = ServiceProviderInformation.objects.get(user_id=sid)
   			id_2 = s_id.user_type
   			if id_2 == 'service_provider':
	   			service_provider = True
	   		else:
	   			service_provider =False
   		except:
   			s_id = User.objects.get(id=sid)
   			print('hjkkkkkkkkkkkkkk')
   		return render(request,'urban/home.html',{'customer_name':name,'s':service_provider,'cus_request':cus_request,'service':service,'sid':sid,'my_name':my_name})
	else:
		return redirect('index')

def home_error(request,e):
	error = e		
	if request.session.get('username'):
   		name = request.session.get('username')
   		service = AddService.objects.all()
   		cus_request = CustomerRequest.objects.all()
   		spn = User.objects.get(username=name)
   		sid = spn.id
   		service_provider = False
   		try :
   			s_id = ServiceProviderInformation.objects.get(user_id=sid)
   			id_2 = s_id.user_type
   			if id_2 == 'service_provider':
	   			service_provider = True
	   		else:
	   			service_provider =False
   		except:
   			s_id = User.objects.get(id=sid)
   			# print('hjkkkkkkkkkkkkkk')
   		return render(request,'urban/home.html',{'error':error,'customer_name':name,'s':service_provider,'cus_request':cus_request,'service':service,'sid':sid})
	else:
		return redirect('index')

def customer_error(request,e):
	error=e
	return render(request,'urban/register.html', {'error':error})
	
def register(request):
	if request.session.get('username'):
   		name = request.session.get('username')
   		return render(request,'urban/home.html',{'customer_name':name})
	else:
		return render(request,'urban/register.html')

def CustomerRegister(request):
	registered = False
	if request.method == 'POST':
		print('post')
		username = request.POST.get("usernm")
		passwd = request.POST.get("passwd")
		email = request.POST.get("email")


		if username == '' or email == '' or passwd == '':
			print('empty')
			error = 'Enter valid details...!!!' 
		elif User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
			print('user_name')
			error = 'username or email Allready used..!!!'
		else:
			print('save')
			user = User.objects.create_user(username=username,password=passwd,email=email)
			rr = UserInformation.objects.create(user=user) 
		
			user.save()
			rr.save()

		
			registered = True
			return redirect('homeeee',name=username)
		return redirect('customer_error',e=error)

	else:
		print('no post')
		return redirect('register')

def CustomerLogin(request):
	print('login')
	if request.method=="POST":
		print('post')
		# token = request.POST['csrfmiddlewaretoken']
		username = request.POST['l_usernm']
		password = request.POST['l_passwd']
		user = authenticate(username=username, password=password)
		print("____________CL___________",user)
		if user is not None:
			print('login yes')

			# session
			request.session['username'] = username
			n = request.session.get('username')
			print('nnnnnnnnn',n)

			
			return redirect("homeeee",name=n)
		else:
			print('erro-----')
			error = 'Enter wrong details...!!!'
			return redirect('customer_error',e=error)
	else:
		print('no post')
		error='please register...!!!'
		return redirect('customer_error',e=error)

def CustomerLogout(request):
	del request.session['username']
	# login_token = request.session['login_token']
	print('logout')
	# print('----->logout_token------>',login_token)

	return redirect('formView')

def ProviderLogout(request):
	del request.session['username']
	# pass
	# login_token = request.session['login_token']
	print('logout')
	# print('----->logout_token------>',login_token)

	return redirect('formView')


def service_error(request,error):
	error = error
	return render(request,'urban/provider_register.html',{'error':error})

def service(request):
	if request.session.get('username'):
   		name = request.session.get('username')
   		return render(request,'urban/home.html',{'customer_name':name})
	else:	
		return render(request,'urban/provider_register.html')


def service_provider_register(request):
	if request.method == 'POST':
		print('post')
		user_name = request.POST.get("user_name")
		email = request.POST.get("email")
		password = request.POST.get("password")

		if user_name == '' or email == '' or password == '':
			error = 'Enter valid details...!!!' 
		elif User.objects.filter(email=email).exists():
			print('if')
			error = 'username or email already exists...!!!'
		else:
			print('else')
			user = User.objects.create(username=user_name,password=password,email=email)
			sp = ServiceProviderInformation.objects.create(user=user) 
		
			user.save()
			sp.save()
			registered = True
			return redirect('homeeee',name=user_name)
			# return render(request , 'urban/home.html',{'service_provider_name':user_name})
		return redirect('service_error',error=error)
	else:
		print('no post')

	# context = {
	# 			'registered' : registered,
	# 			'error':error
	# 		}		

	# return render(request , 'urban/provider_register.html' , context)
	# return HttpResponse("")
		return redirect('service')

def Service_provider_Login(request):
	if request.method == 'POST':
		print('sign in post--------')
		name = request.POST.get('sl_usernm')
		password = request.POST.get('sl_passwd')
		
		iter = 2000
		salt = "random_salt"
		hashed_pass = get_base64_hashed(password, salt, iter, hashlib.sha256)
		print(name)
		print(hashed_pass)
		if name=='' or password=='':
			error = 'Please Enter Details...!!!'
		elif User.objects.filter(username=name,password=password).exists():
			print('elif-----')
			request.session['username'] = name
			name = request.session.get('username')
			return redirect('homeeee', name=name)
		else:
			print('erro-----')
			error = 'Enter wrong details...!!!'
		return redirect('service_error',error=error)
	else:	
		print('e-----')
		return redirect('service')


def deactive_account(request):
	print('deactive_account')
	if request.session.get('username'):
		print('if')
		name = request.session.get('username')
		# User.objects.filter(username=username).delete()
		User.objects.filter(username=name).delete()
		del request.session['username']

		print('name')
		error = 'Account Removed successfully...!!'
		return redirect('customer_error',e=error)
	else:
		error = 'Your account does not remove Please try again..!!!'
		return redirect('customer_error',e=error)


def add(request,error):
	error=error
	s=True
	customer_name = request.session.get('username')
	return render(request,'urban/home.html',{'error':error,'customer_name':customer_name,'s':s})

def add_services(request):
	# pass
	print('dfcgvhbnj')
# 	# error = ''
	name = request.session.get('username')
	sn = User.objects.get(username=name)
	print(sn)
	sid = sn.id
	print(sid)
	v = ServiceProviderInformation.objects.get(user_id=sid)
	print('vvvvvvv',v)
	vv = v.id
	s = True	
	registered = False
	if request.method == 'POST':
		print("-------Add Service---",'post')
		add = request.POST.get("add")


		if add == '' :
			print('sdfgh')
			error = 'plzz add services correctly'
			return redirect('add',error=error)		

		else:
			AddService.objects.create(add_services=add,s_provider_id=vv,user_id=sid)
			# return HttpResponse('service added successfully')
			registered = True
	return redirect('homeeee',name=name)

	# return render(request , 'urban/home.html',{'error':error,'s':s})

def Customer_Request(request,sid):
	name = request.session.get('username')
	crn = User.objects.get(username=name)
	cid = crn.id
	print(cid)
	sid = sid
	print(sid)
	if CustomerRequest.objects.filter(addservice_id=sid,user_id=cid,status='pending').exists():
		error = "you cannot request more than once wait for reply"
		return redirect('home_error',e=error)
	elif CustomerRequest.objects.filter(addservice_id=sid,user_id=cid,status='Accepted').exists():
		error = "request is already  Accepted by ServiceProvider you cannot request again"	
		return redirect('home_error',e=error)
	elif CustomerRequest.objects.filter(addservice_id=sid,user_id=cid,status='Completed', review='').exists():
		error = "you need to review first then only you can request the service again"	
		return redirect('home_error',e=error)
	else:	
		CustomerRequest.objects.create(status='pending',addservice_id=sid,user_id=cid)

	# return HttpResponse('heyy')
	return redirect('homeeee',name=name)

def Customer_Request_delete(request,sid):
	name = request.session.get('username')
	crn = User.objects.get(username=name)
	cid = crn.id
	print(cid)
	sid = sid
	print(sid)
	if CustomerRequest.objects.filter(addservice_id=sid,user_id=cid,status='Accepted').exists():
		error = "you cannot cancel the request as it is already Accepted by ServiceProvider"
		return redirect('home_error',e=error)
	else:	
		CustomerRequest.objects.filter(addservice_id=sid,user_id=cid,status='pending').delete()
	# CustomerRequest.objects.filter(status='delete',addservice_id=sid,user_id=cid).delete()

	# return HttpResponse('heyy')
	return redirect('homeeee',name=name)


def home_status(request,s,rid):
	# pass
	status = s	
	rid = rid
	if request.session.get('username'):
   		name = request.session.get('username')
   		service = AddService.objects.all()
   		cus_request = CustomerRequest.objects.all()
   		spn = User.objects.get(username=name)
   		sid = spn.id
   		service_provider = False
   		try :
   			s_id = ServiceProviderInformation.objects.get(user_id=sid)
   			id_2 = s_id.user_type
   			if id_2 == 'service_provider':
	   			service_provider = True
	   		else:
	   			service_provider =False
   		except:
   			s_id = User.objects.get(id=sid)
   			print('hjkkkkkkkkkkkkkk')
   		return render(request,'urban/home.html',{'customer_name':name,'s':service_provider,'cus_request':cus_request,'service':service,'sid':sid,'rid':rid,'status':status})
	else:
		return redirect('index')


 #   	return render(request,'urban/home.html',{'rid':rid,'status':s})



def service_accept(request,rid,sid):
	# pass
	sid=sid
	rid = rid
	print(rid)
	print(sid)
	accept = True
	CustomerRequest.objects.filter(user_id=rid , addservice_id=sid).update(status='Accepted')
	return redirect('home_status',s=accept,rid=rid)		


def service_complete(request,rid,sid):
	# pass
	rid = rid
	sid = sid
	complete = True

	CustomerRequest.objects.filter(user_id=rid, addservice_id=sid).update(status='Completed')
	return redirect('home_status',s=complete,rid=rid)		

def service_reject(request,rid,sid):
	# pass
	sid = sid
	rid = rid
	accept = False
	CustomerRequest.objects.filter(user_id=rid, addservice_id=sid).delete()
	return redirect('home_status',s=accept,rid=rid)	

def review(request,rid,sid):
	sid = sid
	rid = rid
	name = request.session.get('username')
	if request.method == 'POST':
		c_review = request.POST.get('review')
		if c_review == "":
			error = 'Kindly Enter Review'
			return redirect('home_error',e=error)
		else:
			CustomerRequest.objects.filter(user_id=rid , addservice_id=sid).update(review=c_review)
	return redirect('homeeee', name=name)
	


