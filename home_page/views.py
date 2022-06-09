from django.shortcuts import render
from numpy import UFUNC_PYVALS_NAME
from home_page.forms import Registration_form, Userinfo_forms, Blood_donate_forms, Order_blood_forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import pandas as pd
from home_page.models import *



# Create your views here.
def home_page_views(request):
    return render(request,"home_page/home.html")

#data extraction with pandas


@login_required()
def blood_order(request):
    usr_n = request.user
    order_blood = Order_blood_forms()
    if request.method == 'POST':
        order_blood = Order_blood_forms(request.POST)
        if order_blood.is_valid():
            receiver_name =  request.POST.get('receiver_name')
            hospital_name =  request.POST.get('hospital_name')
            unit_qty =  request.POST.get('unit_qty')
            receiver_contact_no =  request.POST.get('receiver_contact_no')
            receiver_blood_grp = request.POST.get('receiver_blood_grp')
            receiver_gender =  request.POST.get('receiver_gender')
            blood_grp =  request.POST.get('blood_grp')
            email_id = request.POST.get('email_id')
            Order_blood_model.objects.create(user_n = usr_n, receiver_name=receiver_name,hospital_name=hospital_name,
                                              unit_qty=unit_qty,receiver_contact_no=receiver_contact_no,receiver_blood_grp=receiver_blood_grp,
                                             receiver_gender=receiver_gender,blood_grp=blood_grp,email_id=email_id)
            
            return HttpResponseRedirect("after_login")
    else:
        order_blood = Order_blood_forms()
    return render(request, "home_page/order_page.html",{"order_blood":order_blood})

@login_required
def after_login_home(request):
    
    
    return render(request,"home_page/after_login.html")

@login_required
def order_details_page(request):
    order_data = Order_blood_model.objects.all()
    return render(request,"home_page/order_details.html",{'order_data':order_data})

@login_required
def user_logout(request):
    logout(request)
    return render(request,"home_page/home.html")





def compatibility(request):
    return render(request,"home_page/compatibilty.html")

def registration_page(request):
    forms_home = Registration_form()
    form_user = Userinfo_forms()
    registered = False
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        forms_home = Registration_form(request.POST)
        form_user = Userinfo_forms(request.POST)
    # check whether it's valid:
        if forms_home.is_valid() and form_user.is_valid():
            user =form_user.save()
            user.set_password(user.password) #hashing the password
            user.save()
            
            form_home=forms_home.save(commit=False)
            form_home.user = user
            form_home.save()
            registered = True
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:

# if a GET (or any other method) we'll create a blank form
    else:
        forms_home = Registration_form()
        form_user = Userinfo_forms()
    return render(request,"home_page/registrations.html", context={'forms_home':forms_home,'form_user': form_user, 'registered': registered})



# #user login
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            return render(request,"home_page/after_login.html")
        else:
            return HttpResponse("invailid user details")
    else:
        return render(request, 'home_page/home.html')
        

def blood_donate(request):
    donate_form = Blood_donate_forms()
    if request.method == 'POST':
        donate_form = Blood_donate_forms(request.POST)
        if donate_form.is_valid():
            donate_form.save()
            print(donate_form)
            return HttpResponseRedirect("/")
    else:
        donate_form = Blood_donate_forms()
    return render(request, "home_page/want_to_donate.html",{"blood_donate":donate_form})


def blood_availability(request):
    
    table_blood_transfered = Order_blood_model.objects.all().values()
    table_blood_received = Received_unit_model.objects.all().values()
    
    transfer_dataframe = pd.DataFrame(table_blood_transfered)
    received_dataframe = pd.DataFrame(table_blood_received)
    
    grp_trf_data=transfer_dataframe.groupby("blood_grp")["unit_qty"].sum()
    grp_receive_data=received_dataframe.groupby("blood_group")["unit_qty"].sum()
    perpetual_blood = grp_receive_data - grp_trf_data
    df={}
    perpetual_df = perpetual_blood.to_dict()
    for k,v in perpetual_df.items():
        df.update({k:v})
    
    
    
    return render(request,"home_page/perpetual_blood.html",{"df":df})


# This View with controll the contact page.
def contact_us(request):
    return render(request,"home_page/contact.html")

# This view wll controll the about us page on html templates

def about_us(request):
    return render(request,'home_page/about.html')