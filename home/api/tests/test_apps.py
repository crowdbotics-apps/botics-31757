from rest_framework import status

from home.api.tests import BaseAPITestCase, AppFactory
from home.models import App


class AppsTestCase(BaseAPITestCase):

    def test_list_apps(self):
        response = self.client.get('/api/v1/apps/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_app_by_id(self):
        app = AppFactory(
            name="testlistapp",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="testlistapp",
            user=self.user_admin
        )
        response = self.client.get(f'/api/v1/apps/{app.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_app(self):
        data = {
            "name": "wade botics app",
            "description": "Backend API",
            "type": "Web",
            "framework": "Django",
            "domain_name": "Wade Botics"
        }
        response = self.client.post('/api/v1/apps/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_app(self):
        data = {
            "name": "test app-2",
            "description": "Backend API",
            "type": "Web",
            "framework": "Django",
            "domain_name": "testapp-2"
        }
        response = self.client.post('/api/v1/apps/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_app(self):
        app = AppFactory(
            name="test app-3",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="testapp-3",
            user=self.user_admin
        )
        data = {
            "name": "test application",
            "description": "Backend API",
            "type": "Web",
            "framework": "Django",
            "domain_name": "test-application"
        }
        response = self.client.put(f'/api/v1/apps/{app.id}/', data=data, format='json')
        self.assertEqual(response.data['data']['name'], 'test application')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_app_with_existing_app_name(self):
        app = AppFactory(
            name="test app-3",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="testapp-3",
            user=self.user_admin
        )
        data = {
            "name": "test app-2",
            "description": "Backend API",
            "type": "Web",
            "framework": "Django",
            "domain_name": "testapp-2"
        }
        response = self.client.put(f'/api/v1/apps/{app.id}/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_non_existing_app(self):
        data = {
            "name": "test app-2",
            "description": "Backend API",
            "type": "Web",
            "framework": "Django",
            "domain_name": "testapp-2"
        }
        response = self.client.put('/api/v1/apps/21/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_app(self):
        app = AppFactory(
            name="test app-3",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="testapp-3",
            user=self.user_admin
        )
        data = {
            "name": "test application",
            "type": "Mobile",
            "framework": "Django",
        }
        response = self.client.patch(f'/api/v1/apps/{app.id}/', data=data, format='json')
        self.assertEqual(response.data['data']['type'], 'Mobile')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_app(self):
        app = AppFactory(
            name="test app-4",
            description="Backend API",
            type="Web",
            framework="Django",
            domain_name="testapp-4",
            user=self.user_admin
        )
        response = self.client.delete(f'/api/v1/apps/{app.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_non_existing_app(self):
        response = self.client.delete('/api/v1/apps/21/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
