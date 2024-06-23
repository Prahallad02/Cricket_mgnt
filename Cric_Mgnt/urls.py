from django.urls import path
from . import views
urlpatterns =[
  path('',views.Home , name='Home'),
  path('login/',views.Login , name='login'),
  path('logout/',views.Logout , name='logout'),
  path('register/',views.Register , name='register'),
  path('getCoaches/',views.GetCoachView , name='getCoaches'),
  path('postFormCoaches/',views.PostCoachFormView , name='postFormCoaches'),
  path('postCoaches/',views.PostCoachView , name='postCoaches'),
  path('getPlayers/',views.GetPlayersView , name='getPlayers'),
  path('postFormPlayers/',views.PostFormPlayersView , name='postFormPlayers'),
  path('postPlayers/',views.PostPlayersView , name='postPlayers'),
  path('edit_coach/<int:coach_id>/', views.edit_coach, name='edit_coach'),
  path('delete_coach/<int:coach_id>/', views.delete_coach, name='delete_coach'),
]


