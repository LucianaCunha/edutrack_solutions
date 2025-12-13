# myproject/core/models.py

from django.db import models

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    departamento = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    STATUS_CHOICES = [
        ('Ativa', 'Ativa'),
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
    ]

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, related_name='turmas', null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Ativa')

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro'),
        ('Não Informado', 'Não Informado'),
    ]

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES, default='Não Informado')

    # Relacionamento N:N com Turma
    # O Django criará automaticamente uma tabela intermediária (ex: core_aluno_turmas)
    # para gerenciar este relacionamento, sem que precisemos defini-la explicitamente.
    turmas = models.ManyToManyField(Turma, related_name='alunos')

    def __str__(self):
        return self.nome
