from datetime import datetime
from random import randint
from django.core.management.base import BaseCommand
from apps.patient.models import *
from apps.geographic_location.models import *
from apps.employee.models import *
from apps.classifiers.models import *
from apps.cancer_registry.models import *
from apps.chemotherapy.models import *
from apps.nuclear_medicine.models import *

provinces = ["Pinar del Río","Artemisa","La Habana","Mayabeque","Matanzas","Cienfuegos","Villa Clara","Sacti Spíritus","Ciego de Ávila","Camagüey","Las Tunas","Granma","Holguín","Santiago de Cuba","Guantánamo","Isla de la Juventud"]

hlg_municipalities = ["Holguín","Mayarí","Moa","Rafael Freyre","Banes"]

class Command(BaseCommand):
    help = 'Generates 5 instances of all models'

    def handle(self, *args, **options):
        
        self.stdout.write("--Localización Geográfica--")
        for prov in provinces:
            try:
                provincia = Province()
                provincia.name = prov
                provincia.save()
                self.stdout.write("Provincia:" + provincia.name)
                if prov == "Holguín":
                    for mun in hlg_municipalities:
                        municipio = Municipality()
                        municipio.province = provincia
                        municipio.name = mun
                        municipio.save()
                        self.stdout.write("Municipio:" + municipio.name)
            except Exception as e:
                self.stdout.write("Error:",e)

        self.stdout.write("--Pacientes--")
        for i in range(0,20):
            try:
                p = Patient()
                p.identity_card = "0000000{0}".format(i)
                p.first_name = "Paciente-{0}".format(i+1)
                p.last_name = "Apellido-{0}".format(i+1)
                p.street = "Calle-{0}".format(i+1)
                p.number = "Numero-{0}{1}".format(i+1,i)
                p.building = "Edificio-{0}".format(i+1)
                p.sex = randint(0,2)
                p.date_of_birth = datetime(randint(1970,2002),randint(1,12),randint(1,28))
                p.race = randint(0,4)
                p.born_municipality = Municipality.objects.filter(name=hlg_municipalities[randint(0,4)])[0]
                p.residence_municipality = p.born_municipality
                p.is_oncologic = True
                p.save()
                self.stdout.write("Usuario:" + p.first_name + p.last_name)
            except Exception as e:
                self.stdout.write("Error:"+str(e))

        self.stdout.write("--Grupos de Trabajo y Doctores--")
        for i in range(5):
            try:
                group = Group()
                group.name = "Grupo-{0}".format(i+1)
                self.stdout.write("Grupo: " + group.name)
                group.save()
                doctor = Doctor()
                doctor.group = group
                doctor.first_name = "Doctor-{0}".format(i+1)
                doctor.last_name = "Apellido-{0}".format(i+1)
                doctor.personal_record_number = "00000{0}".format(i+1)
                doctor.save()
                self.stdout.write("Doctor: " + doctor.first_name)
            except Exception as e:
                self.stdout.write("Error:"+str(e))
        
        self.stdout.write("--Clasificaciones--")
        for i in range(5):
            try:
                tipografia = Topography()
                tipografia.name = "Tipografía-{0}".format(i+1)
                self.stdout.write("Tipografía: " + tipografia.name)
                tipografia.save()
                morfologia = Morphology()
                morfologia.name = "Morfología-{0}".format(i+1)
                morfologia.save()
                self.stdout.write("Morfología: " + morfologia.name)
            except Exception as e:
                self.stdout.write("Error:"+str(e))
                
        self.stdout.write("Neoplasias")
        for pat in Patient.objects.all():
            try:
                neo = Neoplasm()
                neo.patient = pat
                neo.date_of_diagnosis = datetime(randint(2007,2022),randint(1,12),randint(1,28))
                neo.age_at_diagnosis = randint(18,40)
                neo.psa = randint(0,100)
                neo.primary_site = Topography.objects.all()[randint(0,len(Topography.objects.all())-1)]
                neo.laterality = randint(1,3)
                confir = randint(1,9)
                while confir == 3 or confir == 8:
                    confir = randint(1,9)
                neo.diagnostic_confirmation = confir
                neo.histologic_type = Morphology.objects.all()[randint(0,len(Morphology.objects.all())-1)]
                neo.differentiation_grade = randint(1,9)
                neo.save()
                self.stdout.write("Neoplasia: ok")
            except Exception as e:
                self.stdout.write("Error:"+str(e))

        self.stdout.write("--Esquemas--")
        for i in range(5):
            try:
                esquema = Scheme()
                esquema.name = "Esquema-{0}".format(i+1)
                self.stdout.write("Esquema: " + esquema.name)
                esquema.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e))

        self.stdout.write("--Protocolos--")
        for i, pat in enumerate(Patient.objects.all()):
            try:
                protocolo = Protocol()
                protocolo.patient = pat
                protocolo.scheme = Scheme.objects.all()[randint(0,len(Scheme.objects.all())-1)]
                protocolo.room = randint(1,2)
                protocolo.height = randint(173,180)
                protocolo.weight = randint(60,90)
                protocolo.cycles = randint(1,5)
                protocolo.stage = randint(0,18)
                protocolo.doctor = Doctor.objects.all()[randint(0,len(Doctor.objects.all())-1)]
                protocolo.suspended = False
                self.stdout.write("Protocolo: Protocolo-{0}".format(i+1))
                protocolo.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e))
        
        self.stdout.write("--Fármacos--")
        for i in range(20):
            try:
                medicamento = Drug()
                medicamento.name = "Medicamento-{0}".format(i+1)
                medicamento.drug_type = randint(0,5)
                medicamento.presentation = randint(0,5)
                medicamento.amount = randint(1,20)
                medicamento.unit = randint(0,2)
                medicamento.out_of_stock = False
                self.stdout.write("Fármaco: {0}".format(medicamento.name))
                medicamento.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e))
        
        self.stdout.write("--Medicaciones--")
        for i, prot in enumerate(Protocol.objects.all()):
            try:
                medicacion = Medication()
                medicacion.protocol = prot
                medicacion.drug = Drug.objects.all()[randint(0,len(Drug.objects.all())-1)]
                medicacion.days = randint(7,45)
                medicacion.route = randint(0,4)
                medicacion.prescribed_dose = randint(1,4)
                medicacion.unit = randint(0,2)
                medicacion.suspended = False
                self.stdout.write("Medicación: {0}".format(i))
                medicacion.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e))
        
        self.stdout.write("--Ciclos--")
        for i, prot in enumerate(Protocol.objects.all()):
            try:
                ciclo = Cycle()
                ciclo.protocol = prot
                ciclo.next_date = datetime(datetime.now().year,randint(datetime.now().month,12),randint(1,28))
                ciclo.save()
                medicacion_ciclo = CycleMedication()
                medicacion_ciclo.cycle = ciclo
                medicacion_ciclo.drug = Drug.objects.all()[randint(0,len(Drug.objects.all())-1)]
                medicacion_ciclo.dose = randint(1,4)
                medicacion_ciclo.unit = randint(0,2)
                self.stdout.write("Ciclo: {0}".format(i))
                medicacion_ciclo.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e)) 

        self.stdout.write("--Estudios oncológico ria-irma--")

        pruebas = ["TSH","T3","T4","TG","ANTI-TG"]

        for i, pat in enumerate(Patient.objects.all()):
            try:
                estudio = OncologicStudy()
                estudio.patient = pat
                estudio.tests = pruebas
                self.stdout.write("Estudio oncológico: {0}".format(i))
                estudio.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e))
        
        self.stdout.write("--Estudios hormonal ria-irma--")

        pruebas = ["TSH","T3","T4","T3F","T4F"]

        for i, pat in enumerate(Patient.objects.all()):
            try:
                estudio = HormonalStudy()
                estudio.patient = pat
                estudio.tests = pruebas
                self.stdout.write("Estudio hormonal: {0}".format(i))
                estudio.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e)) 

        self.stdout.write("--Resultado oncología ria-irma--")

        for i, est in enumerate(OncologicStudy.objects.all()):
            try:
                resultado = OncologicResult()
                resultado.oncologic_study = est
                resultado.tsh = randint(0,100)
                resultado.t3 = randint(0,100)
                resultado.t4 = randint(0,100)
                resultado.tg = randint(0,100)
                resultado.anti_tg = randint(0,100)
                self.stdout.write("Resultado oncológico: {0}".format(i))
                resultado.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e))
        
        self.stdout.write("--Resultado hormonal ria-irma--")

        for i, est in enumerate(HormonalStudy.objects.all()):
            try:
                resultado = HormonalResult()
                resultado.hormonal_study = est
                resultado.tsh = randint(0,100)
                resultado.t3 = randint(0,100)
                resultado.t4 = randint(0,100)
                resultado.t3f = randint(0,100)
                resultado.t4f = randint(0,100)
                self.stdout.write("Resultado hormonal: {0}".format(i))
                resultado.save()
            except Exception as e:
                self.stdout.write("Error:"+str(e)) 
        
        self.stdout.write("--detección de yodo seriada--")

        for i, pat in enumerate(Patient.objects.all()):
            try:
                estudio = SerialIodineDetection()
                estudio.patient = pat
                estudio.two_hours = randint(0,100)
                estudio.four_hours = randint(0,100)
                estudio.eight_hours = randint(0,100)
                estudio.twenty_four_hours = randint(0,100)
                estudio.forty_eight_hours = randint(0,100)
                estudio.seventy_two_hours = randint(0,100)
                estudio.ninety_six_hours = randint(0,100)
                estudio.save()
                self.stdout.write("Detección de Yodo Seriada: {0}".format(i))
            except Exception as e:
                self.stdout.write("Error:"+str(e))

        self.stdout.write("--detección de yodo--")

        for i, pat in enumerate(Patient.objects.all()):
            try:
                estudio = IodineDetection()
                estudio.patient = pat
                estudio.two_hours = randint(0,100)
                estudio.twenty_four_hours = randint(0,100)
                estudio.save()
                self.stdout.write("Detección de Yodo: {0}".format(i))
            except Exception as e:
                self.stdout.write("Error:"+str(e)) 

        self.stdout.write("--Estudios y Radio isótopos--")
        for i in range(20):
            try:
                estudio = Study()
                estudio.name = "Estudio-{0}".format(i)
                estudio.save()
                self.stdout.write("Estudio: {0}".format(estudio.name))
                ri = RadioIsotope()
                ri.name = "Radio Isótopo-{0}".format(i)
                ri.save()
                self.stdout.write("Radio Isótopo: {0}".format(ri.name))
            except Exception as e:
                self.stdout.write("Error:"+str(e))

        self.stdout.write("--Fármacos de Medicina Nuclear--")
        for i in range(20):
            try:
                medicamento = NuclearMedicineDrug()
                medicamento.name = "Fármaco MN-{0}".format(i)
                medicamento.save()
                self.stdout.write("Fármaco: {0}".format(medicamento.name))
            except Exception as e:
                self.stdout.write("Error:"+str(e))


        self.stdout.write("--Gammagrafía--")
        for i, pat in enumerate(Patient.objects.all()):
            try:
                estudio = Gammagraphy()
                estudio.patient = pat
                estudio.drug = NuclearMedicineDrug.objects.all()[randint(0,len(NuclearMedicineDrug.objects.all())-1)]
                estudio.radio_isotope = RadioIsotope.objects.all()[randint(0,len(RadioIsotope.objects.all())-1)]
                estudio.dose = randint(1,4)
                estudio.report = "*Palabras de Reporte .......*"
                estudio.observation = "Observaciones Diversas ......."
                estudio.save()
                estudio.requested_study.add(Study.objects.all()[randint(0,len(Study.objects.all())-1)])
                self.stdout.write("Gammagrafía: {0}".format(i))
            except Exception as e:
                self.stdout.write("Error:"+str(e))