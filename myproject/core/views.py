# myproject/core/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Professor, Turma, Aluno
from .serializers import ProfessorSerializer, TurmaSerializer, AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # GET liberado, POST/PUT/DELETE restrito

    # Exemplo de rota de relacionamento: GET /api/professores/{id}/turmas/
    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def turmas(self, request, pk=None):
        professor = self.get_object()
        turmas = professor.turmas.all() # related_name='turmas' no modelo Turma
        serializer = TurmaSerializer(turmas, many=True)
        return Response(serializer.data)

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Exemplo de rota de relacionamento: GET /api/alunos/{id}/turmas/
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def turmas(self, request, pk=None):
        aluno = self.get_object()
        turmas = aluno.turmas.all()
        serializer = TurmaSerializer(turmas, many=True)
        return Response(serializer.data)

    # Rota para matricular um aluno em uma turma
    # POST /api/alunos/{id}/matricular/
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def matricular(self, request, pk=None):
        aluno = self.get_object()
        turma_id = request.data.get('turma_id')

        if not turma_id:
            return Response({"detail": "turma_id é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            turma = Turma.objects.get(id=turma_id)
        except Turma.DoesNotExist:
            return Response({"detail": "Turma não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        if turma in aluno.turmas.all():
            return Response({"detail": "Aluno já matriculado nesta turma."}, status=status.HTTP_409_CONFLICT)

        aluno.turmas.add(turma)
        aluno.save()
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Rota para desmatricular um aluno de uma turma
    # POST /api/alunos/{id}/desmatricular/
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def desmatricular(self, request, pk=None):
        aluno = self.get_object()
        turma_id = request.data.get('turma_id')

        if not turma_id:
            return Response({"detail": "turma_id é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            turma = Turma.objects.get(id=turma_id)
        except Turma.DoesNotExist:
            return Response({"detail": "Turma não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        if turma not in aluno.turmas.all():
            return Response({"detail": "Aluno não está matriculado nesta turma."}, status=status.HTTP_409_CONFLICT)

        aluno.turmas.remove(turma)
        aluno.save()
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Rota de relacionamento: GET /api/turmas/{id}/alunos/
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def alunos(self, request, pk=None):
        turma = self.get_object()
        alunos_matriculados = turma.alunos.all()
        serializer = AlunoSerializer(alunos_matriculados, many=True)
        return Response(serializer.data)

    # Rota para matricular um aluno em uma turma (alternativa à rota do Aluno)
    # POST /api/turmas/{id}/matricular-aluno/
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def matricular_aluno(self, request, pk=None):
        turma = self.get_object()
        aluno_id = request.data.get('aluno_id')
        if not aluno_id:
            return Response({"detail": "aluno_id é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            aluno = Aluno.objects.get(id=aluno_id)
        except Aluno.DoesNotExist:
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        if aluno in turma.alunos.all():
            return Response({"detail": "Aluno já matriculado nesta turma."}, status=status.HTTP_409_CONFLICT)

        turma.alunos.add(aluno)
        turma.save()
        serializer = TurmaSerializer(turma)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Rota para desmatricular um aluno de uma turma (alternativa à rota do Aluno)
    # POST /api/turmas/{id}/desmatricular-aluno/
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def desmatricular_aluno(self, request, pk=None):
        turma = self.get_object()
        aluno_id = request.data.get('aluno_id')
        if not aluno_id:
            return Response({"detail": "aluno_id é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            aluno = Aluno.objects.get(id=aluno_id)
        except Aluno.DoesNotExist:
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        if aluno not in turma.alunos.all():
            return Response({"detail": "Aluno não está matriculado nesta turma."}, status=status.HTTP_409_CONFLICT)

        turma.alunos.remove(aluno)
        turma.save()
        serializer = TurmaSerializer(turma)
        return Response(serializer.data, status=status.HTTP_200_OK)
