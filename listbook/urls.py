from django.urls import path 
from .views import IndexPageView, menuView, mostrar, datosform_view, widget_view, boardsform_view, registro_view 
urlpatterns = [ 
path('', IndexPageView.as_view(), name='index'), 
path('menu/',  menuView, name='menu'),     
path('listbook/', mostrar, name='listbook'),

path('mostrar/',  mostrar, name='mostrar'), 
path('datosform/',  datosform_view, name='datos_form'), 
path('widgetform/',  widget_view, name='widgetform'), 
path('boardsform/',  boardsform_view, name='boardsform'),  
path('registro/', registro_view, name="registro"),    
path('inputbook/', widget_view, name='widgetform'), 

]




# from django.urls import path 
# from .views import IndexPageView,  menuView, mostrar, datosform_view, widget_view, boardsform_view 

# urlpatterns = [ 
#     path('', IndexPageView.as_view(), name='index'), 
#     path('menu/', menuView, name='menu'), 
#     path('listbook/', mostrar, name='listbook'),
#     path('mostrar/', mostrar, name='mostrar'), 
#     path('datosform/', datosform_view, name='datos_form'), 
#     path('inputbook/', widget_view, name='widgetform'), 
#     path('boardsform/', boardsform_view, name='boardsform'),  ]