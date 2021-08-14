from django.urls import path
from .views import *


urlpatterns = [
     path('', home , name='home'), 
     path('signin/', login_view ,name='login_view'),
     path('contact/', contact_us ,name='contact_us'),
     path('account/', account_view ,name='account_view'),
     path('add-blog/', add_blog ,name='add_blog' ),
     path('blog_detail/<slug>', blog_detail ,name='blog_detail'),
     path('blog_delete/<id>' , blog_delete ,name="blog_delete"),
     path('blog_update/<slug>' , blog_update ,name="blog_update"),
     path('logout-view/', logout_view , name="logout_view" ),
     path('edit-profile/', edit_profile , name="edit_profile" )
]
