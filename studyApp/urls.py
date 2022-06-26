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
    path('showSale/<int:post_id>/', views.showSale, name="showSale"),
    path('deletePost/<int:post_id>/', views.deletePost, name="deletePost"),
    path('sold/<int:post_id>/', views.sold, name="sold"),
    path('peerRegister', views.peerRegister, name='peerRegister'),
    path('peerFinder', views.peerFinder, name='peerFinder'),
    path('buy', views.buyMaterial, name='buy'),
    path('tutorCont', views.tutorContact, name='tutorCont'),
    path('peerCont', views.peerContact, name='peerCont'),
]
