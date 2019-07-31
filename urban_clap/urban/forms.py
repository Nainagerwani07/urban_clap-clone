# from django import forms
# from django.contrib.auth.models import User
# from urban.models import UserInfo, C_Register

# class UserForm(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput())

# 	class Meta():
# 		model = User
# 		fields = ('password',)

# 	# def __init__(self, *args, **kwargs):
# 	# 	super(UserForm, self).__init__(*args, **kwargs)

# 	# 	for fieldname in ['password',]:
# 	# 		self.fields[fieldname].help_text = None	
# # 



# # from urban.models import C_Register

# class RegisterForm(forms.ModelForm):
# 	class Meta:
# 		# password = forms.CharField(widget=forms.PasswordInput())
# 		model = C_Register
# 		fields = ('name','email','Mobile_no')
