from apps.classifiers.factories import StudyFactory
from apps.core.test import TestCase
from apps.nuclear_medicine.factories import (
    GammagraphyFactory,
    HormonalResultFactory,
    HormonalStudyFactory,
    IodineDetectionFactory,
    OncologicResultFactory,
    OncologicStudyFactory,
    SerialIodineDetectionFactory,
)


class OncologicStudyTestCase(TestCase):
    """Test case for OncologicStudy model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = OncologicStudyFactory.create()

    def test_study_str(self):
        """Test that OncologicStudy str method returns the sample number and tests."""
        self.assertEqual(
            str(self.study),
            f"Muestra {str(self.study.sample_number).zfill(2)} {str(self.study.tests)}",
        )


class HormonalStudyTestCase(TestCase):
    """Test case for HormonalStudy model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = HormonalStudyFactory.create()

    def test_study_str(self):
        """Test that HormonalStudy str method returns the sample number and tests."""
        self.assertEqual(
            str(self.study),
            f"Muestra {str(self.study.sample_number).zfill(2)} {str(self.study.tests)}",
        )


class HormonalResultTestCase(TestCase):
    """Test case for HormonalResult model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.result = HormonalResultFactory.create()

    def test_study_str(self):
        """Test that HormonalResult str method returns the sample number and tests."""
        self.assertEqual(
            str(self.result),
            f"Resultado de Muestra {str(self.result.hormonal_study.sample_number).zfill(2)} {str(self.result.hormonal_study.tests)}",
        )


class OncologicResultTestCase(TestCase):
    """Test case for OncologicResult model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.result = OncologicResultFactory.create()

    def test_study_str(self):
        """Test that OncologicResult str method returns the sample number and tests."""
        self.assertEqual(
            str(self.result),
            f"Resultado de Muestra {str(self.result.oncologic_study.sample_number).zfill(2)} {str(self.result.oncologic_study.tests)}",
        )


class SerialIodineDetectionTestCase(TestCase):
    """Test case for SerialIodineDetection model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.iodine_detection = SerialIodineDetectionFactory.create()

    def test_study_str(self):
        """Test that SerialIodineDetection str method returns the patient name."""
        self.assertEqual(
            str(self.iodine_detection),
            f"Detección de yodo seriada de {str(self.iodine_detection.patient)}",
        )


class IodineDetectionTestCase(TestCase):
    """Test case for IodineDetection model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.iodine_detection = IodineDetectionFactory.create()

    def test_study_str(self):
        """Test that IodineDetection str method returns the patient name."""
        self.assertEqual(
            str(self.iodine_detection),
            f"Detección de yodo de {str(self.iodine_detection.patient)}",
        )


class GammagraphyTestCase(TestCase):
    """Test case for Gammagraphy model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.gammagraphy1 = GammagraphyFactory.create()
        cls.study = StudyFactory.create()
        cls.gammagraphy2 = GammagraphyFactory.create(requested_study=(cls.study,))

    def test_gammagraphy_str(self):
        """Test that Gammagraphy str method returns name."""
        self.assertEqual(
            str(self.gammagraphy1), f"Gammagrafía de {str(self.gammagraphy1.patient)}"
        )
