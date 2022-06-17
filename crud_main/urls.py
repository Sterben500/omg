from django.urls import path
from . import views

app_name = 'crud_main'
urlpatterns = [

    path('', views.getData, name = "dataView"),

    path('create_server', views.create_server, name="create_server"),
    path('create_type_of_server', views.itype_of_server, name="type_of_server"),
    path('users', views.iusers, name='users'),
    path('servers', views.iservices, name='servers'),
    path('applications', views.iapplications, name="applications"),
    path('apphasservices', views.iapphasservices, name= "apphasservices"),
    path('overall', views.ioverall, name = "overall"),


    path('update_server/<server_id>', views.update_server, name = "update_server"),
    path('update_type_of_server/<type_of_server_id>', views.update_type_of_server, name = "update_type_of_server"),
    path('update_users/<users_id>', views.update_users, name = "update_users"),
    path('update_services/<services_id>', views.update_services, name = "update_servers"),
    path('update_applications/<applications_id>', views.update_applications, name = "update_applications"),
    path('update_app_has_services/<apphasservices_id>', views.updateapphasservices, name= "update_app_has_services" ),
    path('update_overall/<overall_id>', views.update_overall, name = "update_overall"),


    path('delete_server/<str:pk>', views.deleteServer, name="delete_server"),
    path('delete_type_of_server/<str:pk>', views.deleteTypeofserver, name="delete_type_of_server"),
    path('delete_users/<str:pk>', views.deleteUsers, name="delete_users"),
    path('delete_services/<str:pk>', views.deleteServices, name="delete_servers"),
    path('delete_applications/<str:pk>', views.deleteApplications, name="delete_applications"),
    path('delete_app_has_services/<str:pk>', views.deleteapphasservices, name = "delete_app_has_services"),
    path('delete_overall/<str:pk>', views.deleteOverall, name="delete_overall"),


    path('list/', views.list, name = "list"),

    path('search/', views.search, name="Search"),

    path('show_server/<server_id>', views.show_server, name="show_server"),
    ]
