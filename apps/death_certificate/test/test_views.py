from http import HTTPStatus

from django.contrib.messages import get_messages
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.death_certificate.factories import DeathCertificateFactory
from apps.death_certificate.forms import DeathCertificateForm
from apps.death_certificate.models import DeathCertificate
from apps.death_certificate.views import (
    DeathCertificateCreateView,
    DeathCertificateDeleteView,
    DeathCertificateDetailView,
    DeathCertificateUpdateView,
)


class DeathCertificateDetailViewTestCase(TestCase):
    """Test case for DeathCertificateDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.death = DeathCertificateFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for DeathCertificateDetailView."""
        response = self.client.get(
            reverse("death_certificate:death_certificate_list", args=(self.death.pk,))
        )
        self.assertIn(str(self.death), response.content.decode())
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())
        self.assertIn(
            reverse(DeathCertificateDetailView.cancel_url), response.content.decode()
        )


class DeathCertificateDeleteViewTestCase(TestCase):
    """Test case for DeathCertificateDeleteView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.death = DeathCertificateFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_post(self):
        """Test the post method for DeathCertificateDeleteView."""
        self.client.post(
            reverse("death_certificate:death_certificate_list", args=(self.death.pk,))
        )
        self.assertFalse(DeathCertificate.objects.filter(pk=self.death.pk).exists())

    def test_get(self):
        """Test the get method for DeathCertificateDeleteView."""
        response = self.client.get(
            reverse("death_certificate:death_certificate_list", args=(self.death.pk,))
        )
        self.assertIn(str(self.death), response.content.decode())
        self.assertIn(
            reverse(DeathCertificateDeleteView.cancel_url), response.content.decode()
        )


class DeathCertificateCreateViewTestCase(TestCase):
    """Test case for DeathCertificateCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for DeathCertificateCreateView."""
        response = self.client.get(
            reverse("death_certificate:death_certificate_list")
        )
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], DeathCertificateForm))
        self.assertIn(
            reverse(DeathCertificateCreateView.cancel_url), response.content.decode()
        )

    def test_post(self):
        """Test the post method for DeathCertificateCreateView."""
        count_before_test = DeathCertificate.objects.count()
        response = self.client.post(
            reverse("death_certificate:death_certificate_list"),
            {"name": "Test_Death_Certificate"},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            DeathCertificateCreateView.success_message
            % {"name": "Test_Death_Certificate"},
        )
        self.assertEqual(DeathCertificate.objects.count(), count_before_test + 1)


class DeathCertificateUpdateViewTestCase(TestCase):
    """Test case for DeathCertificateUpdateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.death = DeathCertificateFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for DeathCertificateUpdateView."""
        response = self.client.get(
            reverse("death_certificate:death_certificate_list", args=(self.death.pk,))
        )
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], DeathCertificateForm))
        self.assertIn(
            reverse(DeathCertificateUpdateView.cancel_url), response.content.decode()
        )

    def test_post(self):
        """Test the post method for DeathCertificateUpdateView."""
        response = self.client.post(
            reverse(
                "death_certificate:death_certificate_list", args=(self.death.pk,)
            ),
            {"name": "TestDeathCertificate"},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            DeathCertificateUpdateView.success_message
            % {"name": "TestDeathCertificate"},
        )
        self.death.refresh_from_db()
        self.assertEqual(str(self.death), "TestDeathCertificate")
