import datetime as dt

from django.http import FileResponse
from django.template.response import TemplateResponse
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.cancer_registry.factories import NeoplasmFactory
from apps.cancer_registry.forms import NeoplasmForm
from apps.cancer_registry.views import NeoplasmCreateView
from apps.core.test import TestCase


class NeoplasmCreateViewTestCase(TestCase):
    """Test case for NeoplasmCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.neoplasm = NeoplasmFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for NeoplasmCreateView."""
        response = self.client.get(reverse("cancer_registry:neoplasm_create"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], NeoplasmForm))
        self.assertIn(
            "(None, '----------')",
            str(response.context["form"].fields["laterality"]._choices),
        )
        self.assertIn(reverse(NeoplasmCreateView.cancel_url), response.content.decode())
        self.assertIn("related-model-add", response.content.decode())

    def test_related_model_in_detail_view(self):
        """Test that related model view button is not shown in detail view"""
        response = self.client.get(
            reverse("cancer_registry:neoplasm_detail", args=(self.neoplasm.pk,))
        )
        self.assertIn("related-model-view", response.content.decode())
        self.assertNotIn("related-model-add", response.content.decode())


class ReportsTestCase(TestCase):
    """Test case for Reports."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.neoplasm = NeoplasmFactory.create(date_of_report=dt.date(2001, 12, 1))

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_group(self):
        """Test the group report response."""
        response = self.client.post(
            reverse("cancer_registry:group_report"),
            {"initial_date": "1/1/2001", "final_date": "01/01/2222"},
        )
        self.assertIsInstance(response, FileResponse)
        response = self.client.post(
            reverse("cancer_registry:group_report"),
            {"initial_date": "20/20/2001", "final_date": "01/01/2222"},
        )
        self.assertIsInstance(response, TemplateResponse)

    def test_morphology(self):
        """Test the morphology report response."""
        response = self.client.post(
            reverse("cancer_registry:morphology_report"),
            {"initial_date": "1/1/2001", "final_date": "01/01/2222"},
        )
        self.assertIsInstance(response, FileResponse)
        response = self.client.post(
            reverse("cancer_registry:morphology_report"),
            {"initial_date": "20/20/2001", "final_date": "01/01/2222"},
        )
        self.assertIsInstance(response, TemplateResponse)

    def test_topography(self):
        """Test the topography report response."""
        response = self.client.post(
            reverse("cancer_registry:topography_report"),
            {"initial_date": "1/1/2001", "final_date": "01/01/2222"},
        )
        self.assertIsInstance(response, FileResponse)
        response = self.client.post(
            reverse("cancer_registry:topography_report"),
            {"initial_date": "20/20/2001", "final_date": "01/01/2222"},
        )
        self.assertIsInstance(response, TemplateResponse)


class ExportTestCase(TestCase):
    """Test case for Neoplasm Export."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.neoplasm = NeoplasmFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_export(self):
        """Test the neoplasm export response."""
        response = self.client.post(
            reverse("cancer_registry:neoplasm_list"),
        )
        self.assertIsInstance(response, FileResponse)
