from django.test import TestCase

# from django.utils.timezone import datetime
from rest_framework.test import APIClient
from sinp_nomenclatures.models import Nomenclature

from cables.models import Diagnosis, Line, Point
from commons.tests.tests_commons import createTestUser, logTestUser


class DiagnosiAnonymousAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Diagnosis and anonymous user.

    Include tests for user trying to log-in with wrong password
    """

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = [
        "commons/tests/fixtures/test_nomenclatures.xml",
        "commons/tests/fixtures/test_cables.xml",
    ]

    def setUp(self):
        self.anonymous_client = APIClient()
        # create user trying to log-in with wrong password
        self.user = createTestUser("user", "password")
        self.unauthentified_client = logTestUser("user", "wrong-password")
        # get pk from the first diagnosis
        self.pk = Diagnosis.objects.all()[0].id

    def test_get_list_with_anonymous_user(self):
        resp = self.anonymous_client.get("/api/v1/cables/diagnosis/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get("/api/v1/cables/diagnosis/")
        self.assertEquals(resp.status_code, 401)

    def test_get_detail_with_anonymous_user(self):
        resp = self.anonymous_client.get(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.get(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_create_with_anonymous_user(self):
        resp = self.anonymous_client.post("/api/v1/cables/diagnosis/")
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.post("/api/v1/cables/diagnosis/")
        self.assertEquals(resp.status_code, 401)

    def test_update_with_anonymous_user(self):
        resp = self.anonymous_client.put(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.put(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_partial_update_with_anonymous_user(self):
        resp = self.anonymous_client.patch(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.patch(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)

    def test_partial_delete_with_anonymous_user(self):
        resp = self.anonymous_client.delete(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)
        resp = self.unauthentified_client.delete(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 401)


class DiagnosisUnauthorizedAuthenticationTestCase(TestCase):
    """Class to test authentication/permission scheme for Diagnosis and unauthorized user."""

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = [
        "commons/tests/fixtures/test_nomenclatures.xml",
        "commons/tests/fixtures/test_cables.xml",
    ]

    def setUp(self):
        self.user = createTestUser("user", "password")
        self.unauthorized_client = logTestUser("user", "password")
        # get pk from the first diagnosis
        self.pk = Diagnosis.objects.all()[0].id

    # no restriction for read only by default with Django
    def test_get_list_with_unauthorized_user(self):
        resp = self.unauthorized_client.get("/api/v1/cables/diagnosis/")
        self.assertEquals(resp.status_code, 200)

    # no restriction for read only by default with Django
    def test_get_detail_with_unauthorized_user(self):
        resp = self.unauthorized_client.get(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 200)

    def test_create_with_unauthorized_user(self):
        resp = self.unauthorized_client.post(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.put(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_partial_update_with_unauthorized_user(self):
        resp = self.unauthorized_client.patch(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)

    def test_partial_delete_with_unauthorized_user(self):
        resp = self.unauthorized_client.delete(
            f"/api/v1/cables/diagnosis/{self.pk}/"
        )
        self.assertEquals(resp.status_code, 403)


class CreatePointDiagnosisTestCase(TestCase):
    """Class to test creation of Diagnosis related to Point infrastructure.
    This test case mainly focuses on automatic following specific function:
    When first Diagnosis is created from an infrastructure, it has last=True.
    When another one is created for this same infrastructure, the old one is set with last=False and the new one with last=True

    Require creation and consultation of various elements
    """

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["commons/tests/fixtures/test_nomenclatures.xml"]

    def setUp(self):
        # create client with authentified user
        self.user = createTestUser(
            "user", "password", "add_point", "add_diagnosis"
        )
        self.authentified_client = logTestUser("user", "password")
        # create new Point

        owner_id = Nomenclature.objects.filter(type__mnemonic="owner")[0].id
        self.infCond = Nomenclature.objects.filter(
            type__mnemonic="infrastr_condition"
        )[0].id
        self.risk_id = Nomenclature.objects.filter(
            type__mnemonic="risk_level"
        )[0].id
        data = {
            "owner_id": owner_id,
            "geom": {"type": "Point", "coordinates": [0.5, 0.5]},
        }
        resp = self.authentified_client.post(
            "/api/v1/cables/points/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)

    def test_create_first_Diag_with_last_TRUE(self):
        point_id = Point.objects.all()[0].id  # get Point id
        # create Diagnosis
        data = {
            "infrastructure": point_id,
            "date": "2022-01-01",
            "neutralized": False,
            "sgmt_build_integr_risk": self.risk_id,
            "sgmt_moving_risk": self.risk_id,
            "sgmt_topo_integr_risk": self.risk_id,
        }
        resp = self.authentified_client.post(
            "/api/v1/cables/diagnosis/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        # check value
        diag = resp.json()
        self.assertTrue(diag["last"])

    def test_create_third_Diag_and_2_first_with_last_TRUE___should_not_occur___(
        self,
    ):
        point_id = Point.objects.all()[0].id  # get Point id
        data = {
            "infrastructure": point_id,
            "date": "2022-01-01",
            "neutralized": False,
            "condition_id": self.infCond,
            "isolation_advice": False,
            "dissuasion_advice": False,
            "attraction_advice": False,
            "pole_attractivity_id": self.risk_id,
            "pole_dangerousness_id": self.risk_id,
        }
        # create 2 Diagnosis on same infrastructure
        diags = []
        for i in range(0, 2):
            resp = self.authentified_client.post(
                "/api/v1/cables/diagnosis/", data, format="json"
            )
            self.assertEquals(resp.status_code, 201)
            # check value
            diag = resp.json()
            self.assertEquals(diag["last"], True)
        # set last=True for last Diagnosis
        Diagnosis.objects.update(infrastructure=point_id, last=True)
        # check both Diagnosis with last=True
        diags = Diagnosis.objects.filter(infrastructure=point_id, last=True)
        self.assertEquals(len(diags), 2)
        # create third diagnosis on same infrastructure
        resp = self.authentified_client.post(
            "/api/v1/cables/diagnosis/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)  # check success
        # check last one created with lat=True
        new = resp.json()
        self.assertTrue(new["last"])
        # check only one is last=True, 2 have last=False
        diags = Diagnosis.objects.filter(infrastructure=point_id, last=False)
        self.assertEquals(len(diags), 2)
        diags = Diagnosis.objects.filter(infrastructure=point_id, last=True)
        self.assertEquals(len(diags), 1)


class CreateLineDiagnosisTestCase(TestCase):
    """Class to test creation of Diagnosis related to Line infrastructure.
    This test case mainly focuses on automatic following specific function:
    When first Diagnosis is created from an infrastructure, it has last=True.
    When another one is created for this same infrastructure, the old one is set with last=False and the new one with last=True

    Require creation and consultation of various elements
    """

    # fixture includes:
    # - at least 2 points, 2 lines, 3 diagnosis, 3 operations, 2 GeoAreas, 2 SensitiveAreas, 2 media
    # (pictures), 2 mortality cases
    # - It contains needed sinp_nomenclature items (stand for dictionanry for specific data)
    fixtures = ["commons/tests/fixtures/test_nomenclatures.xml"]

    def setUp(self):
        # create client with authentified user
        self.user = createTestUser(
            "user", "password", "add_line", "add_diagnosis"
        )
        self.authentified_client = logTestUser("user", "password")
        # create new Point
        owner_id = Nomenclature.objects.filter(type__mnemonic="owner")[0].id
        self.risk_id = Nomenclature.objects.filter(
            type__mnemonic="risk_level"
        )[0].id
        data = {
            "owner_id": owner_id,
            "geom": {"type": "LineString", "coordinates": [[2, 6], [2, 4]]},
        }

        resp = self.authentified_client.post(
            "/api/v1/cables/lines/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)

    def test_create_first_Diag_with_last_TRUE(self):
        line_id = Line.objects.all()[0].id  # get Point id
        # create Diagnosis
        data = {
            "infrastructure": line_id,
            "date": "2022-01-01",
            "neutralized": False,
            "sgmt_build_integr_risk": self.risk_id,
            "sgmt_moving_risk": self.risk_id,
            "sgmt_topo_integr_risk": self.risk_id,
            "sgmt_veget_integr_risk": self.risk_id,
        }

        resp = self.authentified_client.post(
            "/api/v1/cables/diagnosis/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)
        # check value
        diag = resp.json()
        self.assertTrue(diag["last"])

    def test_create_third_Diag_and_2_first_with_last_TRUE___should_not_occur___(
        self,
    ):
        line_id = Line.objects.all()[0].id  # get Point id
        data = {
            "infrastructure": line_id,
            "date": "2022-01-01",
            "neutralized": False,
            "sgmt_build_integr_risk": self.risk_id,
            "sgmt_moving_risk": self.risk_id,
            "sgmt_topo_integr_risk": self.risk_id,
            "sgmt_veget_integr_risk": self.risk_id,
        }

        # create 2 Diagnosis on same infrastructure
        diags = []
        for i in range(0, 2):
            resp = self.authentified_client.post(
                "/api/v1/cables/diagnosis/", data, format="json"
            )
            self.assertEquals(resp.status_code, 201)
            # check value
            diag = resp.json()
            self.assertEquals(diag["last"], True)
        # set last=True for last Diagnosis
        Diagnosis.objects.update(infrastructure=line_id, last=True)
        # check both Diagnosis with last=True
        diags = Diagnosis.objects.filter(infrastructure=line_id, last=True)
        self.assertEquals(len(diags), 2)
        # create third diagnosis on same infrastructure
        resp = self.authentified_client.post(
            "/api/v1/cables/diagnosis/", data, format="json"
        )
        self.assertEquals(resp.status_code, 201)  # check success
        # check last one created with lat=True
        new = resp.json()
        self.assertTrue(new["last"])
        # check only one is last=True, 2 have last=False
        diags = Diagnosis.objects.filter(infrastructure=line_id, last=False)
        self.assertEquals(len(diags), 2)
        diags = Diagnosis.objects.filter(infrastructure=line_id, last=True)
        self.assertEquals(len(diags), 1)
