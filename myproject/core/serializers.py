# myproject/core/serializers.py

from rest_framework import serializers
from .models import Professor, Turma, Aluno

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    # Para o relacionamento 1:N Professor ↔ Turma, podemos exibir o nome do professor
    professor_nome = serializers.ReadOnlyField(source='professor.nome')

    class Meta:
        model = Turma
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    # Para o relacionamento N:N Aluno ↔ Turma, podemos exibir os IDs das turmas
    # ou uma representação mais detalhada se necessário.
    # Por enquanto, vamos manter simples para focar nas 3 tabelas.
    turmas_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Turma.objects.all(), source='turmas')

    class Meta:
        model = Aluno
        fields = '__all__'
        # Se você quiser incluir os nomes das turmas ao invés dos IDs (somente leitura)
        # fields = ['id', 'nome', 'matricula', 'email', 'curso', 'data_nascimento', 'genero', 'turmas_ids']
        # read_only_fields = ('turmas_nomes',) # Se você adicionar um campo para nomes das turmas
# myproject/core/serializers.py

from rest_framework import serializers
from .models import Professor, Turma, Aluno

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    professor_nome = serializers.ReadOnlyField(source='professor.nome')

    class Meta:
        model = Turma
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    # Para o relacionamento N:N Aluno ↔ Turma, podemos exibir os IDs das turmas
    # que o aluno está matriculado.
    turmas_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Turma.objects.all(), source='turmas')

    class Meta:
        model = Aluno
        fields = '__all__'
