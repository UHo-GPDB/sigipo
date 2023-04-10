from http import HTTPStatus

from django.contrib.messages import get_messages
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.geographic_location.factories import (
    LocationFactory,
    MunicipalityFactory,
    ProvinceFactory,
)
from apps.geographic_location.forms import LocationForm, MunicipalityForm, ProvinceForm
from apps.geographic_location.models import Location, Municipality, Province
from apps.geographic_location.views import (
    LocationCreateView,
    LocationDeleteView,
    LocationDetailView,
    LocationUpdateView,
    MunicipalityCreateView,
    MunicipalityDeleteView,
    MunicipalityDetailView,
    MunicipalityUpdateView,
    ProvinceCreateView,
    ProvinceDeleteView,
    ProvinceDetailView,
    ProvinceUpdateView,
)


class ProvinceDetailViewTestCase(TestCase):
    """Test case for ProvinceDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province = ProvinceFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for ProvinceDetailView."""
        response = self.client.get(
            reverse("geographic_location:province_detail", args=(self.province.pk,))
        )
        self.assertIn(str(self.province), response.content.decode())
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())
        self.assertIn(reverse(ProvinceDetailView.cancel_url), response.content.decode())


class ProvinceDeleteViewTestCase(TestCase):
    """Test case for ProvinceDeleteView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province = ProvinceFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_post(self):
        """Test the post method for ProvinceDeleteView."""
        self.client.post(
            reverse("geographic_location:province_delete", args=(self.province.pk,))
        )
        self.assertFalse(Province.objects.filter(pk=self.province.pk).exists())

    def test_get(self):
        """Test the get method for ProvinceDeleteView."""
        response = self.client.get(
            reverse("geographic_location:province_delete", args=(self.province.pk,))
        )
        self.assertIn(str(self.province), response.content.decode())
        self.assertIn(reverse(ProvinceDeleteView.cancel_url), response.content.decode())


class ProvinceCreateViewTestCase(TestCase):
    """Test case for ProvinceCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for ProvinceCreateView."""
        response = self.client.get(reverse("geographic_location:province_create"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], ProvinceForm))
        self.assertIn(reverse(ProvinceCreateView.cancel_url), response.content.decode())

    def test_post(self):
        """Test the post method for ProvinceCreateView."""
        count_before_test = Province.objects.count()
        response = self.client.post(
            reverse("geographic_location:province_create"), {"name": "TestProvince"}
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            ProvinceCreateView.success_message % {"name": "TestProvince"},
        )
        self.assertEqual(Province.objects.count(), count_before_test + 1)


class ProvinceUpdateViewTestCase(TestCase):
    """Test case for ProvinceUpdateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.province = ProvinceFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for ProvinceUpdateView."""
        response = self.client.get(
            reverse("geographic_location:province_update", args=(self.province.pk,))
        )
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], ProvinceForm))
        self.assertIn(reverse(ProvinceUpdateView.cancel_url), response.content.decode())

    def test_post(self):
        """Test the post method for ProvinceUpdateView."""
        response = self.client.post(
            reverse("geographic_location:province_update", args=(self.province.pk,)),
            {"name": "TestProvince"},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            ProvinceUpdateView.success_message % {"name": "TestProvince"},
        )
        self.province.refresh_from_db()
        self.assertEqual(str(self.province), "TestProvince")


class MunicipalityDetailViewTestCase(TestCase):
    """Test case for MunicipalityDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.municipality = MunicipalityFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for MunicipalityDetailView."""
        response = self.client.get(
            reverse(
                "geographic_location:municipality_detail", args=(self.municipality.pk,)
            )
        )
        self.assertIn(self.municipality.name, response.content.decode())
        self.assertIn(self.municipality.province.name, response.content.decode())
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())
        self.assertIn(
            reverse(MunicipalityDetailView.cancel_url), response.content.decode()
        )


class MunicipalityDeleteViewTestCase(TestCase):
    """Test case for MunicipalityDeleteView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.municipality = MunicipalityFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_post(self):
        """Test the post method for MunicipalityDeleteView."""
        self.client.post(
            reverse(
                "geographic_location:municipality_delete", args=(self.municipality.pk,)
            )
        )
        self.assertFalse(Municipality.objects.filter(pk=self.municipality.pk).exists())

    def test_get(self):
        """Test the get method for MunicipalityDeleteView."""
        response = self.client.get(
            reverse(
                "geographic_location:municipality_delete", args=(self.municipality.pk,)
            )
        )
        self.assertIn(str(self.municipality), response.content.decode())
        self.assertIn(
            reverse(MunicipalityDeleteView.cancel_url), response.content.decode()
        )


class MunicipalityCreateViewTestCase(TestCase):
    """Test case for MunicipalityCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.province = ProvinceFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for MunicipalityCreateView."""
        response = self.client.get(reverse("geographic_location:municipality_create"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], MunicipalityForm))
        self.assertIn(reverse(ProvinceCreateView.cancel_url), response.content.decode())

    def test_post(self):
        """Test the post method for MunicipalityCreateView."""
        count_before_test = Municipality.objects.count()
        response = self.client.post(
            reverse("geographic_location:municipality_create"),
            {"name": "TestMunicipality", "province": self.province.pk},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            MunicipalityCreateView.success_message % {"name": "TestMunicipality"},
        )
        self.assertEqual(Municipality.objects.count(), count_before_test + 1)


class MunicipalityUpdateViewTestCase(TestCase):
    """Test case for MunicipalityUpdateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.province = ProvinceFactory.create(name="TestProvince")
        cls.municipality = MunicipalityFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for MunicipalityUpdateView."""
        response = self.client.get(
            reverse(
                "geographic_location:municipality_update", args=(self.municipality.pk,)
            )
        )
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], MunicipalityForm))
        self.assertIn(
            reverse(MunicipalityUpdateView.cancel_url), response.content.decode()
        )

    def test_post(self):
        """Test the post method for MunicipalityUpdateView."""
        response = self.client.post(
            reverse(
                "geographic_location:municipality_update", args=(self.municipality.pk,)
            ),
            {"name": "TestMunicipality", "province": self.province.pk},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            MunicipalityUpdateView.success_message % {"name": "TestMunicipality"},
        )
        self.municipality.refresh_from_db()
        self.assertEqual(str(self.municipality), "TestMunicipality - TestProvince")
        self.assertEqual(self.municipality.province.pk, self.province.pk)


class LocationDetailViewTestCase(TestCase):
    """Test case for LocationDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.location = LocationFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for LocationDetailView."""
        response = self.client.get(
            reverse("geographic_location:location_detail", args=(self.location.pk,))
        )
        self.assertIn(self.location.name, response.content.decode())
        self.assertIn(
            self.location.municipality.province.name, response.content.decode()
        )
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())
        self.assertIn(reverse(LocationDetailView.cancel_url), response.content.decode())


class LocationDeleteViewTestCase(TestCase):
    """Test case for LocationDeleteView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.location = LocationFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_post(self):
        """Test the post method for LocationDeleteView."""
        self.client.post(
            reverse("geographic_location:location_delete", args=(self.location.pk,))
        )
        self.assertFalse(Location.objects.filter(pk=self.location.pk).exists())

    def test_get(self):
        """Test the get method for LocationDeleteView."""
        response = self.client.get(
            reverse("geographic_location:location_delete", args=(self.location.pk,))
        )
        self.assertIn(str(self.location), response.content.decode())
        self.assertIn(reverse(LocationDeleteView.cancel_url), response.content.decode())


class LocationCreateViewTestCase(TestCase):
    """Test case for LocationCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.municipality = MunicipalityFactory.create()
        cls.province = ProvinceFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for LocationCreateView."""
        response = self.client.get(reverse("geographic_location:location_create"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], LocationForm))
        self.assertIn(
            reverse(MunicipalityCreateView.cancel_url), response.content.decode()
        )

    def test_post(self):
        """Test the post method for LocationCreateView."""
        count_before_test = Location.objects.count()
        response = self.client.post(
            reverse("geographic_location:location_create"),
            {
                "name": "TestLocation",
                "municipality": self.municipality.pk,
                "province": self.province.pk,
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            LocationCreateView.success_message % {"name": "TestLocation"},
        )
        self.assertEqual(Location.objects.count(), count_before_test + 1)


class LocationUpdateViewTestCase(TestCase):
    """Test case for LocationUpdateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.province = ProvinceFactory.create(name="TestProvince")
        cls.municipality = MunicipalityFactory.create(name="TestMunicipality")
        cls.location = LocationFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for LocationUpdateView."""
        response = self.client.get(
            reverse("geographic_location:location_update", args=(self.location.pk,))
        )
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], LocationForm))
        self.assertIn(reverse(LocationUpdateView.cancel_url), response.content.decode())

    def test_post(self):
        """Test the post method for LocationUpdateView."""
        response = self.client.post(
            reverse("geographic_location:location_update", args=(self.location.pk,)),
            {
                "name": "TestLocation",
                "municipality": self.municipality.pk,
                "province": self.province.pk,
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            LocationUpdateView.success_message % {"name": "TestLocation"},
        )
        self.location.refresh_from_db()
        self.assertEqual(
            str(self.location), "TestLocation - TestMunicipality - TestProvince"
        )
        self.assertEqual(self.location.municipality.pk, self.municipality.pk)
        self.assertEqual(self.location.province.pk, self.province.pk)
