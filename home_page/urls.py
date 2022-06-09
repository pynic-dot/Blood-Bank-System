from django.urls import path
from home_page import views 

app_name = "home_page"


urlpatterns = [
    path("",views.home_page_views,name="home_page"),
    path("registration",views.registration_page, name='registration'),
    path("compatibility",views.compatibility, name='compatibility'),
    path('login',views.user_login,name='user_login'),
    path('donate',views.blood_donate, name='donate'),
    path('B_available',views.blood_availability, name='B_available'),
    path('contact',views.contact_us, name='contact'),
    path('about',views.about_us, name='about'),
    

    
]

