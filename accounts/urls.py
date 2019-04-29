from django.conf.urls import url
from .import views
from django.urls import path

app_name='accounts'


urlpatterns = [
    url('signup', views.signup_view, name="signup"),
    url('login', views.login_view, name="login"),
    url('logout', views.logout_view, name="logout"),

]