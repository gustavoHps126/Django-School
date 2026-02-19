from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
#   def teste_falha(self):
#        self.fail('Teste falhou')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'teste de modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '68195899056',
            data_nascimento = '2003-02-02',
            celular = '86 11111-1111'
        )
    
    def test_verifica_atributos_de_estudantes(self):
        """Teste que verifica os atributos do modelo de Estudantes"""
        self.assertEqual(self.estudante.nome,'teste de modelo'),
        self.assertEqual(self.estudante.email,'testedemodelo@gmail.com'),
        self.assertEqual(self.estudante.cpf,'68195899056'),
        self.assertEqual(self.estudante.data_nascimento,'2003-02-02'),
        self.assertEqual(self.estudante.celular,'86 11111-1111')
        


class ModelCursoTestCase(TestCase):
#   def teste_falha(self):
#        self.fail('Teste falhou')
    def setUp(self):
        self.curso = Curso.objects.create(
          codigo = '1111111111',
          descricao = 'bla bla bla',
          nivel = 'A'
        )
    
    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de Estudantes"""
        self.assertEqual(self.curso.codigo,'1111111111'),
        self.assertEqual(self.curso.descricao,'bla bla bla'),
        self.assertEqual(self.curso.nivel,'A'),
       
class ModelMatriculaTestCase(TestCase):
    
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')