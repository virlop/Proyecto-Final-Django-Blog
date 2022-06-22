from django.urls import path
from virginiaBlog import views


urlpatterns = [
    path("", views.BlogList.as_view(), name = "virginiaBlog_list"),
    path("crear/",views.BlogCreate.as_view(), name = "virginiaBlog_create"),
    path("detalle/<pk>/", views.BlogDetail.as_view(), name ="virginiaBlog_detail"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="virginiaBlog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="virginiaBlog_delete"),
    path("entrar/", views.BlogLogin.as_view(), name="virginiaBlog_login"),
    path("salir/", views.BlogLogout.as_view(), name="virginiaBlog_logout"),
    path("crear-cuenta/", views.SignUpView.as_view(), name ="virginiaBlog_signup"),
]