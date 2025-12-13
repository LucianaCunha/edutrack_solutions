# myproject/core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet, TurmaViewSet, AlunoViewSet

router = DefaultRouter()
router.register(r'professores', ProfessorViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
