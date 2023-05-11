from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from apps.principal.views import index,inicia,next,elec,final,back,results, inicioAdmin,resultadoAdmin,empleadosAdmin, eliminarEmpleado,editarEmpleado,crearEmpleado

urlpatterns = [
    path('', inicia, name='ini'),
    path('index/', index, name="index"),
    path('salir/', LogoutView.as_view(), name='logout'),
    path('index/<RPE>/<page>', next, name="next"),
    path('index/<int:id>/<RPE>/<page>', elec , name="elejido"),
    path('final/<RPE>', final , name="final"),
    path('resultados/<RPE>', results , name="results"),
    path("index/back/<RPE>/<page>", back, name="back"),
     path('login/', LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('administracion/', inicioAdmin, name="inicioAdmin"),
    path('administracion/resultados/<centro>', resultadoAdmin, name="resultadoAdmin"),
    path('administracion/empleados', empleadosAdmin, name="empleados"), 
    path('administracion/empleados/eliminar/<RPE>', eliminarEmpleado, name="eliminarEmpleado"), 
    path('administracion/empleados/editar/<RPE>', editarEmpleado, name="editarEmpleado"), 
    path('administracion/empleados/crear', crearEmpleado, name="crearEmpleado"), 
];
