from django.urls import path 

from . import views 

urlpatterns = [
    path("",views.home,name="homepage"),

    path("employee",views.employee,name='employee'),
    path("manager",views.manager,name='manager'),
    path("manager1",views.manager,name='manager1'),
    path("adminpage",views.admin,name='admin'),
    path('login/',views.user_login,name="logpage"),

    path('products',views.products,name='products'),
    path('application',views.application,name='application'),
    path('booking',views.booking,name='booking'),
    path('stationary',views.stationary,name='stationary'),

    path('sign/',views.signup,name="signup"),
    path('logout/',views.ulogout,name="logout"),
    path('accept/<int:model>/<int:id>',views.accept,name='accept'),
    path('reject/<int:model>/<int:id>',views.reject,name='reject'),
    path('complete/<int:model>/<int:id>',views.complete,name='complete'),

    path('tdelete/<int:id>/<int:model>',views.tdelete,name='delete'),

]




