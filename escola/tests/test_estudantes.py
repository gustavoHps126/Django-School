from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome = 'Teste estudante 1',
            email = 'Teste@teste01.com.br',
            cpf = '19528631045',
            data_nascimento = '2024-01-02',
            celular = '55 11111-1111'
        )

        self.estudante_02 = Estudante.objects.create(
            nome = 'Teste estudant3 2',
            email = 'Teste@teste02.com.br',
            cpf = '82307983031',
            data_nascimento = '2024-01-02',
            celular = '55 11121-1111'
        )

    def test_requisicao_get_listar_estudantes(self):
        """Teste de requisição get"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_listar_estudante(self):
        """Teste de requisição get para um estudante"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data,dados_estudante_serializados)

    def test_requisicao_post_criar_um_estudante(self):
        '''Teste para criar um usuario'''
        dados = {
            'nome':'teste',
            'email':'teste1@teste.com.br',
            'cpf':'80440038006',
            'data_nascimento':'2003-12-02',
            'celular':'11 11111 1111 '
        }
        response=self.client.post(self.url,dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_requisicao_post_delete_um_estudante(self):
        '''Teste para delete um usuario'''
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):
        """Teste de requisição PUT para um estudante"""
        dados = {
            'nome':'teste',
            'email':'testeput@gmail.com',
            'cpf':'42370866071',
            'data_nascimento':'2003-05-09',
            'celular':'11 88888-6666'
        }
        response = self.client.put(f'{self.url}1/',data=dados)
        self.assertEqual(response.status_code,status.HTTP_200_OK)