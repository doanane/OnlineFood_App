from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlspatterns = [
    path('registerUser/', include('accounts.urls')),
    # path("api/accounts/", include("accounts.urls")),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)