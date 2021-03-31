from django.urls import path
from . import views

app_name = 'todo_app'
urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('signup', views.signup_user, name='signup_user'),
    path('profile/', views.profile, name='profile'),
    path('add', views.add, name='add'),
    path('about', views.about, name='about'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    # path('confirm_delete/<int:todo_id>', views.confirm_delete, name='confirm_delete'),


]
