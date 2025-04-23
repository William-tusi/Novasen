from .rol_urls import urlpatterns as rol_urls
from .usuario_urls import urlpatterns as usuario_urls
from .provivencia_urls import urlpatterns as provivencia_urls
from .ciudad_urls import urlpatterns as ciudad_urls
from .regional_urls import urlpatterns as regional_urls
from .sedes_urls import urlpatterns as sedes_urls
from .ambiente_urls import urlpatterns as ambiente_urls
from .fichas_urls import urlpatterns as fichas_urls
from .programas_urls import urlpatterns as programas_urls
from .auth_urls import urlpatterns as auth_urls

from django.urls import include, path

urlpatterns = [
    path('rol/', include(rol_urls)),
    path('usuario/', include(usuario_urls)),
    path('provivencia/', include(provivencia_urls)),
    path('ciudad/', include(ciudad_urls)),
    path('regional/', include(regional_urls)),
    path('sedes/', include(sedes_urls)),
    path('ambiente/', include(ambiente_urls)),
    path('fichas/', include(fichas_urls)),
    path('programas/', include(programas_urls)),
    path('auth/', include(auth_urls)),  # Asegúrate de incluir auth_urls también
]
