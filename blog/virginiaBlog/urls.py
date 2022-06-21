from django.urls import path
from virginiaBlog import views

urlpatterns = [
    path("", views.BlogCreate.as_view(), name="virginiaBlog_create"),
    path('listar/', views.BlogList.as_view(), name = "virginiaBlog_list"),
    path("<pk>/", views.BlogDetail.as_view(), name ="virginiaBlog_detail"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="virginiaBlog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="virginiaBlog_delete"),
    
]