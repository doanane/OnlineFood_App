from django.urls import path,include
from 


urlspatterns = [
    path('accounts/', include('accounts.urls')),
    # path("api/accounts/", include("accounts.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)