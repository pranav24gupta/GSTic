from django.conf.urls import url
from . import views

#url mapping done here
app_name='gstic'
urlpatterns = [
	#/gstic
	url(r'^$',views.basepage,name='basepage'),
	#/gstic/StartSearch
	url(r'StartSearch/$',views.StartSearch,name="StartSearch"),
]