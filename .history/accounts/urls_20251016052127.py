from django.urls import path,include



urlspatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),