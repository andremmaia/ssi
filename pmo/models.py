from django.db import models
from django.utils import timezone
from datetime import date


class Sistema(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    atividade = models.CharField(max_length=50)
    pontuacao = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.atividade

class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Projeto(models.Model):
    codigo = models.CharField(max_length = 20)
    descricao = models.TextField()
    sistemas = models.ManyToManyField(Sistema, related_name='+')
    responsavel = models.ForeignKey('auth.User')
    horas_contratadas = models.DecimalField(max_digits=10, decimal_places=2)
    horas_contabilizadas = models.DecimalField(max_digits=10, decimal_places=2)
    horas_abonadas = models.DecimalField(max_digits=10, decimal_places=2)
    horas_utilizadas = models.DecimalField(max_digits=10, decimal_places=2)
    horas_saldo = models.DecimalField(max_digits=10, decimal_places=2)
    ponto_focal = models.CharField(max_length=50)
    status = models.ForeignKey(Status, models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return self.codigo

class Os(models.Model):
    numero = models.CharField(max_length = 20)
    data = models.DateField(default = date.today)
    responsavel = models.ForeignKey('auth.User')
    projeto = models.ForeignKey(Projeto, models.SET_NULL, blank=False, null=True)
    atividade = models.ForeignKey(Atividade, models.SET_NULL, blank=True, null=True)
    hora_inicio = models.TimeField(default = timezone.now)
    hora_termino = models.TimeField(default = timezone.now)
    descricao = models.TextField()
    horas_contabilizadas = models.DecimalField(max_digits=10, decimal_places=2)
    horas_abonadas = models.DecimalField(max_digits=10, decimal_places=2)

    def registrar(self):
        self.data_registro = timezone.now()
        self.save()

    def __str__(self):
        return self.numero, self.descricao, self.responsavel
