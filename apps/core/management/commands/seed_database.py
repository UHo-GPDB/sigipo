from datetime import datetime
from random import randint

from django.core.management.base import BaseCommand
from apps.patient.factories import *
from apps.geographic_location.factories import *
from apps.employee.factories import *
from apps.classifiers.factories import *
from apps.cancer_registry.factories import *
from apps.chemotherapy.factories import *
from apps.nuclear_medicine.factories import *

class Command(BaseCommand):
    help = "Generates 5 instances of all models"

    def handle(self, *args, **options):
        
        for i in range(5):
            province = ProvinceFactory.create()
            municipality = MunicipalityFactory.create(province = province)
            patient = PatientFactory.create(residence_municipality = municipality, born_municipality = municipality)
            group = GroupFactory.create()
            doctor = DoctorFactory.create(group=group)
            topography = TopographyFactory.create()
            morphology = MorphologyFactory.create()
            study = StudyFactory.create()
            radioisotope = RadioIsotopeFactory.create()
            neoplasm = NeoplasmFactory.create(patient = patient, primary_site = topography, histologic_type = morphology, group = group, medic_that_report = doctor)
            scheme = SchemeFactory.create()
            protocol = ProtocolFactory.create(patient = patient, scheme = scheme, doctor = doctor)
            drug = DrugFactory.create()
            nuclearmedicinedrug = NuclearMedicineDrugFactory.create()
            medication = MedicationFactory.create(drug = drug, protocol = protocol)
            cycle = CycleFactory.create(protocol = protocol)
            cyclemedication = CycleMedicationFactory.create(cycle = cycle, drug = drug)
            oncologicstudy = OncologicStudyFactory.create(patient = patient)
            hormonalstudy = HormonalStudyFactory.create(patient = patient)
            oncologicresult = OncologicResultFactory.create(oncologic_study = oncologicstudy)
            hormonalresult = HormonalResultFactory.create(hormonal_study = hormonalstudy)
            iodinedetection = IodineDetectionFactory.create(patient = patient)
            serialiodinedetection = SerialIodineDetectionFactory.create(patient = patient)
            gammagraphy = GammagraphyFactory.create(patient = patient, drug = nuclearmedicinedrug, radio_isotope = radioisotope, requested_study = [study])
