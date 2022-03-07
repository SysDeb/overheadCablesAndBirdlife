from django.test import TestCase

# from django.utils.timezone import datetime
from rest_framework.test import APIClient

from cables.models import Infrastructure
from commons.tests.tests_commons import createTestUser, logTestUser

# from sinp_nomenclatures.models import Item, Type


class InfrastructureAnonymousAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Infrastructure and anonymous user.

    Include tests for user trying to log-in with wrong password
    """

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml", "test_cables.xml"]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create user trying to log-in with wrong password
        self.user = createTestUser("user", "password")
        self.unauthentified_client = logTestUser("user", "wrong-password")
        # get pk from the first infrastructure
        self.pk = Infrastructure.objects.all()[0].id

    def test_get_list_with_anonymous_user(self):
        resp = self.anonymous_client.get("/api/v1/cables/infrastructures/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get(
            "/api/v1/cables/infrastructures/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_get_detail_with_anonymous_user(self):
        resp = self.anonymous_client.get(
            f"/api/v1/cables/infrastructures/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get(
            f"/api/v1/cables/infrastructures/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)


class InfrastructureUnauthorizedAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Infrastructure and unauthorized user."""

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["test_nomenclatures.xml", "test_cables.xml"]

    def setUp(self):
        self.user = createTestUser("user", "password")
        self.unauthorized_client = logTestUser("user", "password")
        # get pk from the first nnfrastructure
        self.pk = Infrastructure.objects.all()[0].id

    # no restriction for read only by default with Django
    def test_get_list_with_unauthorized_user(self):
        resp = self.unauthorized_client.get("/api/v1/cables/infrastructures/")
        self.assertEquals(resp.status_code, 200)

    # no restriction for read only by default with Django
    def test_get_detail_with_unauthorized_user(self):
        resp = self.unauthorized_client.get(
            f"/api/v1/cables/infrastructures/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 200)
