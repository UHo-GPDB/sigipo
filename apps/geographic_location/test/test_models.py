from apps.core.test import TestCase
from apps.geographic_location.factories import MunicipalityFactory, ProvinceFactory


class ProvinceTestCase(TestCase):
    """Test case for Province model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province = ProvinceFactory.create()

    def test_province_str(self):
        """Test that province str method returns the province name."""
        self.assertEqual(
            str(self.province),
            self.province.name,
        )


class MunicipalityTestCase(TestCase):
    """Test case for Municipality model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.municipality = MunicipalityFactory.create()

    def test_municipality_str(self):
        """Test that municipality str method returns the municipality name."""
        self.assertEqual(
            str(self.municipality),
            self.municipality.name,
        )