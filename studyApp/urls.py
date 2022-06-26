from . import views
from django.urls import path


urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('post', views.post, name='post'),
    path('createPost', views.createPost, name='createPost'),
    path('sales', views.salePage, name='sales'),
    path('materialSearch', views.materialSearch, name='materialSearch'),
    path('practice', views.pracPage, name='practice'),
    path('subjectSearch', views.subjectSearch, name='subjectSearch'),
    path('tutor', views.tutorPage, name='tutor'),
    path('fnameSearch', views.fnameSearch, name='fnameSearch'),
    path('lnameSearch', views.lnameSearch, name='lnameSearch'),
    path('subjectsSearch', views.subjectsSearch, name='subjectsSearch'),
]
