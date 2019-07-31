from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInformation(models.Model):
	user_type = models.CharField(max_length=30, default='customer')
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = 'UserInformation'  

class ServiceProviderInformation(models.Model):
	user_type = models.CharField(max_length=30, default='service_provider')
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, unique=False)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = 'ServiceProviderInformation' 

class AddService(models.Model):
	add_services = models.CharField(max_length=200)	
	s_provider = models.ForeignKey(UserInformation,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.add_services

	class Meta:
		verbose_name_plural = 'AddService'	

class CustomerRequest(models.Model):
	status = models.CharField(max_length=20)
	addservice = models.ForeignKey(AddService,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	review = models.CharField(max_length=100 , default='')


	def __str__(self):
		return self.status

	class Meta:
		verbose_name_plural = 'CustomerRequest'








        
        
