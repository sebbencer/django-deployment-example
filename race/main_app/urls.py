from django.conf.urls import url
from main_app import views

#TEMPLATE TAGGING
app_name =  'main_app'


urlpatterns = [
    url(r'^about/$',views.about_view,name='about'),
    url(r'^register/$',views.register_view,name='register'),
    url(r'^results/$',views.results_view,name='results'),
    url(r'^route/$',views.route_view,name='route'),


]
