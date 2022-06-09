from secrets import choice
from django import forms
from home_page.models import Registration_models, Blood_donate_model, Order_blood_model
from django.contrib.auth.models import User




class Registration_form(forms.ModelForm):
    MALE='Male'
    FEMALE='Female'
    GENDER_CHOICE = [(MALE,'Male'), (FEMALE,'Female')]
    BLOOD_GR= [ ('A+','A+'),
               ('O+','O+'),
               ('B+','B+'),
               ('AB+','AB+'),
               ('A-','A-'),
               ('B-','B-'),
               ('O-','O-'),
               ('AB-','AB-')]
    name = forms.CharField(max_length=100, label="Full Name", required=True)
    blood_Group = forms.ChoiceField(choices=BLOOD_GR, label="Blood Group")
    address = forms.CharField(max_length=50, required=False)
    mobile_No = forms.CharField(max_length=10, min_length=10,widget=forms.NumberInput(attrs={'type':'number'}), label="Contact No.", required=True)
    email_Id = forms.CharField(widget=forms.EmailInput(), label="Email Id", required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    
    def __init__(self, *args, **kwargs):
        super(Registration_form,self).__init__(*args, **kwargs)
        self.fields['mobile_No'].widget.attrs.update({'class': 'mobileno'})
        self.fields['email_Id'].widget.attrs.update({'class': 'emailid'})
    
    class Meta:
        model = Registration_models
        fields = ('name', 'blood_Group','address','mobile_No','email_Id','gender')
        


class Userinfo_forms(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(Userinfo_forms,self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
            'username':None,
        }
        


class Order_blood_forms(forms.ModelForm):
    MALE='Male'
    FEMALE='Female'
    GENDER_CHOICE = [(MALE,'Male'), (FEMALE,'Female')]
    BLOOD_GR= [ ('A+','A+'),
               ('O+','O+'),
               ('B+','B+'),
               ('AB+','AB+'),
               ('A-','A-'),
               ('B-','B-'),
               ('O-','O-'),
               ('AB-','AB-')]
    
    receiver_name = forms.CharField(max_length=100, label="Receiver Name", required=True )
    hospital_name = forms.CharField(max_length=300, label="Hospital Name", required=True)
    unit_qty = forms.DecimalField(label="Unit Quntity", required=True)
    receiver_contact_no = forms.CharField(max_length=10, min_length=10,widget=forms.NumberInput(attrs={'type':'number'}), label="Contact No.", required=True)
    receiver_blood_grp = forms.ChoiceField(choices=BLOOD_GR,label="Receiver Blood Group", required=True)
    receiver_gender = forms.ChoiceField(choices=GENDER_CHOICE, label="Gender", required=True)
    blood_grp = forms.ChoiceField(choices=BLOOD_GR,label="Received Blood Group", required=True)
    email_id = forms.EmailField(max_length=50, label="Email Id", required=True)
    
    def __init__(self, *args, **kwargs):
        super(Order_blood_forms,self).__init__(*args, **kwargs)
        self.fields['receiver_contact_no'].widget.attrs.update({'class': 'mobileno'})
        self.fields['email_id'].widget.attrs.update({'class': 'emailid'})
        self.fields['unit_qty'].widget.attrs.update({'class': 'unit_qty'})
        
    class Meta:
        model = Order_blood_model
        fields = ('receiver_name', 'hospital_name', 'unit_qty', 'receiver_contact_no',
                  'receiver_blood_grp', 'receiver_gender', 'blood_grp', 'email_id')



class Blood_donate_forms(forms.ModelForm):
    MALE='Male'
    FEMALE='Female'
    GENDER_CHOICE = [(MALE,'Male'), (FEMALE,'Female')]
    BLOOD_GR= [ ('A+','A+'),
               ('O+','O+'),
               ('B+','B+'),
               ('AB+','AB+'),
               ('A-','A-'),
               ('B-','B-'),
               ('O-','O-'),
               ('AB-','AB-')]

    name = forms.CharField(max_length=100,label="Name", required=True)
    blood_grp = forms.ChoiceField(choices=BLOOD_GR, label="Blood Group", required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICE, label="Gender", required=True)
    mobile_no = forms.CharField(max_length=10, min_length=10,widget=forms.NumberInput(attrs={'type':'number'}), label="Contact No.", required=True)
   
    def __init__(self, *args, **kwargs):
        super(Blood_donate_forms,self).__init__(*args, **kwargs)
        self.fields['mobile_no'].widget.attrs.update({'class': 'mobileno'})
        
    class Meta:
        model = Blood_donate_model
        fields = "__all__"
