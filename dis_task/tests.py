from django.test import TestCase
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from .models import Task

# Create your tests here.

class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test1',
            password='123456'
        )

    def test_create_task(self):
        task = Task.objects.create(
            title='Test Task',
            owner=self.user
        )

        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.owner, self.user)


class AuthenticationTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        User.objects.create_user(
            username='cedric',
            password='cedric'
        )

    def test_login_returns_tokens(self):

        response = self.client.post(
            '/api/auth/login/',
            {
                'username': 'cedric',
                'password': 'cedric'
            },
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class RBACPermissionTest(TestCase):

    def setUp(self):

        self.client = APIClient()

        self.admin_group = Group.objects.create(name='Admin')

        self.admin = User.objects.create_user(
            username='admin',
            password='admin'
        )

        self.admin.groups.add(self.admin_group)

        self.user = User.objects.create_user(
            username='user1',
            password='123456'
        )

        self.task = Task.objects.create(
            title='Admin Task',
            owner=self.admin
        )

    def test_admin_can_view_all_tasks(self):

        response = self.client.post(
            '/api/auth/login/',
            {
                'username': 'admin',
                'password': 'admin'
            }
        )

        token = response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        response = self.client.get('/api/tasks/')

        self.assertEqual(response.status_code, 200)