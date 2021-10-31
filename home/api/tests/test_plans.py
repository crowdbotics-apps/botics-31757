from rest_framework import status

from home.api.tests import BaseAPITestCase, PlanFactory


class PlansTestCase(BaseAPITestCase):

    def test_list_plan(self):
        response = self.client.get('/api/v1/plans/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_plan_by_id(self):
        app = PlanFactory(
            name="free tier",
            description="free-tier",
            price=0.00
        )
        response = self.client.get(f'/api/v1/plans/{app.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_plan_by_non_existant_id(self):
        response = self.client.get(f'/api/v1/plans/23/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    