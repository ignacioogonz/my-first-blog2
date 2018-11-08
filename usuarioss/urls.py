from django.conf.urls import url
from usuarioss.views import SignUpView, BienvenidaView, SignInView, SignOutView

app_name = "usuario"

urlpatterns = [
    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),

    
]