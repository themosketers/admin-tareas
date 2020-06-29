#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('logout', views.logout),
    path('agregarActividad', views.agregarActividad),
    path('agregarActGrupoAct/<int:idGrupoActividad>', views.agregarActGrupoAct),
    path('agregarSolicitud/<int:idActividad>', views.agregarSolicitud),
    path('actividadesFinalizadas', views.actividadesFinalizadas),
    path('finalizarTarea/<int:idActividad>', views.finalizarTarea),
    path('agregarGrupoAct', views.agregarGrupoAct),
    path('editarActividad/<int:idActividad>', views.editarActividad),
    path('welcome', views.welcome),
]
