from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from api.views import EvenementViewSet, RapportPerformanceViewSet, UtilisateurViewSet, EleveViewSet, EnseignantViewSet, ClasseViewSet, CoursViewSet, NoteViewSet, AbsenceViewSet,TrimestreViewSet,BulletinViewSet,FichierViewSet,PresenceViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/', include('userapp.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



