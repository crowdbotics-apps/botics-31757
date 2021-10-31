from rest_framework import status

from home.api.tests import BaseAPITestCase, SubscriptionFactory


class SunscriptionTestCase(BaseAPITestCase):

    def test_list_subscriptions(self):
        response = self.client.get('/api/v1/subscriptions/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list_subscription_by_id(self):
        response = self.client.get(f'/api/v1/subscriptions/{self.sub1.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_subscription_by_non_existing_id(self):
        response = self.client.get(f'/api/v1/subscriptions/23/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_subscription(self):
        data = {
            "plan": self.plan2.id,
            "app": self.app2.id,
            "active": True
        }
        response = self.client.post('/api/v1/subscriptions/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_duplicate_subscription(self):
        data = {
            "plan": self.plan1.id,
            "app": self.app1.id,
            "active": True
        }
        response = self.client.post('/api/v1/subscriptions/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_subscription(self):
        data = {
            "plan": self.plan3.id,
            "app": self.app1.id,
            "active": True
        }
        response = self.client.put(f'/api/v1/subscriptions/{self.sub1.id}/', data=data, format='json')
        self.assertEqual(response.data['data']['plan'], self.plan3.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_non_existing_subscription(self):
        data = {
            "plan": self.plan3.id,
            "app": self.app1.id,
            "active": True
        }
        response = self.client.put(f'/api/v1/subscriptions/34/', data=data, format='json')
        self.assertEqual(response.data['data'], 'Subscription not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update_subscription(self):
        data = {
            "plan": self.plan2.id,
            "app": self.app1.id,
            "active": True
        }
        response = self.client.patch(f'/api/v1/subscriptions/{self.sub1.id}/', data=data, format='json')
        self.assertEqual(response.data['data']['plan'], self.plan2.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_non_existing_subscription(self):
        data = {
            "plan": self.plan3.id,
            "app": self.app1.id,
            "active": True
        }
        response = self.client.patch(f'/api/v1/subscriptions/34/', data=data, format='json')
        self.assertEqual(response.data['data'], 'Subscription not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
