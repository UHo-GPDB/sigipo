# Generated by Django 3.2.16 on 2023-11-16 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "pathologic_anathomy",
            "0052_alter_linfomabiopsydiagnostic_especimen_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="linfomabiopsydiagnostic",
            name="biopsy",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="linfoma_byopsy_diagnostic",
                to="pathologic_anathomy.biopsyrequest",
            ),
        ),
        migrations.AlterField(
            model_name="neckbiopsydiagnostic",
            name="biopsy",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="neck_biopsy_diagnostic",
                to="pathologic_anathomy.biopsyrequest",
            ),
        ),
        migrations.AlterField(
            model_name="neckbiopsydiagnostic",
            name="estructuras_adyacentes_invadidas",
            field=models.CharField(
                blank=True,
                max_length=5000,
                null=True,
                verbose_name="El tumor invade a estructuras/órganos adyacentes(especifique). Las estructuras adyacentes del estómago incluyen\n            la pleura, el pericardio, la vena ácigos, el diafragma, el peritoneo, la aorta, cuerpo vertebral y la vía aérea.",
            ),
        ),
        migrations.AlterField(
            model_name="stomacbiopsydiagnostic",
            name="biopsy",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stomac_biopsy_diagnostic",
                to="pathologic_anathomy.biopsyrequest",
            ),
        ),
        migrations.AlterField(
            model_name="stomacbiopsydiagnostic",
            name="estructuras_adyacentes_invadidas",
            field=models.CharField(
                blank=True,
                max_length=5000,
                null=True,
                verbose_name="El tumor invade a estructuras/órganos adyacentes(especifique). Las estructuras adyacentes del estómago incluyen el bazo, el colon\n            transverso, el hígado, el diafragma, el páncreas, la pared abdominal, la glándula suprarrenal, renale intestino delgado, y el retroperitoneo.\n            La extensión intramural del duodeno o el esófago no es considerado invasión de una estructura adyacente, pero está clasificado usa la profundidad de la máxima invasión en cualquier\n            de estos sitios.",
            ),
        ),
        migrations.CreateModel(
            name="GynecologyBiopsyDiagnostic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "procedimiento",
                    models.IntegerField(
                        choices=[
                            (1, "ponche"),
                            (2, "cono por asa"),
                            (3, "otro (especifique)"),
                            (4, "no especificado"),
                        ],
                        verbose_name="El Procedimiento",
                    ),
                ),
                (
                    "procedimiento_otro",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Otro procedimiento(especifique): ",
                    ),
                ),
                (
                    "sitio_tumor",
                    models.CharField(
                        max_length=100,
                        verbose_name="El sitio del Tumor (seleccione todo lo que aplique)",
                    ),
                ),
                (
                    "sitio_no_determinado",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El sitio del tumor no puede ser determinado(explique): ",
                    ),
                ),
                (
                    "tumor_max_size",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="La máxima dimensión del tumor(centímetros)",
                    ),
                ),
                (
                    "additional_tumor_size",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Las dimensiones adicionales del tumor(centímetros)",
                    ),
                ),
                (
                    "size_no_determinado",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Las dimensiones no pueden ser determinadas(explique): ",
                    ),
                ),
                (
                    "tipo_histologico",
                    models.IntegerField(
                        choices=[
                            (1, "carcinoma de células escamosas"),
                            (2, "carcinoma de células escamosas, queratinizante"),
                            (3, "carcinoma de células escamosas, no queratinizante"),
                            (4, "carcinoma de células escamosas, basaloide"),
                            (5, "carcinoma de células escamosas, verrucoso"),
                            (6, "carcinoma de células escamosas, papilar"),
                            (
                                7,
                                "carcinoma de célula escamosas, lymphoepithelioma-like",
                            ),
                            (8, "carcinoma de células escamosas, escamotransicional"),
                            (9, "Adenocarcionoma endocervical, tipo usual"),
                            (10, "Carcinoma mucinous"),
                            (11, "Carcinoma mucinous, tipo intestinal"),
                            (12, "Carcinoma mucinous, tipo células en anillo de sello"),
                            (13, "Carcinoma mucinous, tipo gástrico"),
                            (14, "Carcinoma Villoglandular"),
                            (15, "Carcinoma Endometrioide"),
                            (16, "Carcinoma de células claras"),
                            (17, "Carcinoma seroso"),
                            (18, "Carcinoma Mesonefrico"),
                            (
                                19,
                                "Adenocarcinoma mezclado con carcinoma neuroendocrino",
                            ),
                            (20, "Carcinoma Adenosquamous"),
                            (
                                21,
                                "Carcinoma Adenosquamous, variante de la célula vidriosa",
                            ),
                            (22, "Carcinoma adenoideo quistico"),
                            (23, "Carcinoma basal adenóideo"),
                            (24, "Carcinoma neuroendocrino de células pequeñas"),
                            (25, "Carcinoma neuroendocrine de células grandes"),
                            (26, "Carcinoma indiferenciado"),
                            (27, "Carcinosarcoma"),
                            (
                                28,
                                "otro tipo histologico que no figura en la lista (especifique)",
                            ),
                            (29, "Carcinoma de tipo que no puede ser determinado"),
                        ],
                        verbose_name="El Tipo del Histológico",
                    ),
                ),
                (
                    "tipo_histologico_otro",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Otro tipo histologico que no figura en la lista (especifique): ",
                    ),
                ),
                (
                    "grado_histologico",
                    models.IntegerField(
                        choices=[
                            (1, "Poco diferenciado"),
                            (2, "Moderadamente diferenciado"),
                            (3, "Pobremente diferenciado"),
                            (4, "No puede ser evaluado"),
                            (5, "No se aplica"),
                        ],
                        verbose_name="El Grado del Histológico",
                    ),
                ),
                (
                    "mm_invasion_en_profundidad",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="mm de invasión en profundidad",
                    ),
                ),
                (
                    "invasion_en_profundidad",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Invasión en profundidad: ",
                    ),
                ),
                (
                    "profundidad_no_determinada",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="La profundidad no puede ser determinada(explique):",
                    ),
                ),
                (
                    "longitud_longitudinal",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Longitud longitudinal(mm)"
                    ),
                ),
                (
                    "extension_longitud_no_determinada",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="La extensión no puede ser determinada(explique):",
                    ),
                ),
                (
                    "extensio_horizontal",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Extensión horizontal(mm)"
                    ),
                ),
                (
                    "anchura_circunferencial",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Anchura circunferencial(mm)",
                    ),
                ),
                (
                    "extension_anchura_no_determinada",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="La extensión no puede ser determinada (explique):",
                    ),
                ),
                (
                    "margen_endocervical_no_puede_evaluarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="Margen Endocervical no puede ser evaluado",
                    ),
                ),
                (
                    "margen_endocervical_no_evaluado_explique",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Margen Endocervical no puede ser evaluado (explique):",
                    ),
                ),
                (
                    "margen_endocervical_no_afectado",
                    models.BooleanField(
                        default=False, verbose_name="Margen Endocervical no afectado"
                    ),
                ),
                (
                    "margen_endocervical_distancia_carcinoma",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="La distancia del carcinoma al margen(mm)",
                    ),
                ),
                (
                    "margen_endocervical_afectado_por",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Afectado por:",
                    ),
                ),
                (
                    "margen_endocervical_posicion_especifica",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="La posición especifica(si es posible):",
                    ),
                ),
                (
                    "margen_ectocervical_no_puede_evaluarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="Margen Ectocervical no puede ser evaluado",
                    ),
                ),
                (
                    "margen_ectocervical_no_evaluado_explique",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Margen Ectocervical no puede ser evaluado (explique):",
                    ),
                ),
                (
                    "margen_ectocervical_no_afectado",
                    models.BooleanField(
                        default=False, verbose_name="Margen Ectocervical no afectado"
                    ),
                ),
                (
                    "margen_ectocervical_distancia_carcinoma",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="La distancia del carcinoma al margen ectocervical(mm)",
                    ),
                ),
                (
                    "margen_ectocervical_afectado_por",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Afectado por:",
                    ),
                ),
                (
                    "margen_ectocervical_posicion_especifica",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="La posición especifica(si es posible):",
                    ),
                ),
                (
                    "margen_profundo_no_puede_evaluarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="Margen Profundo no puede ser evaluado",
                    ),
                ),
                (
                    "margen_profundo_no_evaluado_explique",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Margen Profundo no puede ser evaluado (explique):",
                    ),
                ),
                (
                    "margen_profundo_no_afectado",
                    models.BooleanField(
                        default=False, verbose_name="Margen Profundo no afectado"
                    ),
                ),
                (
                    "margen_profundo_distancia_carcinoma",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="La distancia del carcinoma al margen profundo(mm)",
                    ),
                ),
                (
                    "margen_profundo_afectado_por",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Afectado por:",
                    ),
                ),
                (
                    "margen_profundo_posicion_especifica",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="La posición especifica(si es posible):",
                    ),
                ),
                (
                    "invasion_limphovascular",
                    models.IntegerField(
                        choices=[
                            (1, "ausente"),
                            (2, "presente"),
                            (3, "no determinado"),
                        ],
                        verbose_name="La Invasión del Lymphovascular",
                    ),
                ),
                (
                    "otra_patologia_asociada",
                    models.CharField(
                        max_length=100,
                        verbose_name="Otra patología asociada(seleccione todo lo que aplique)",
                    ),
                ),
                (
                    "otra_patologia_asociada_especifique",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El otro del + (especifique): ",
                    ),
                ),
                (
                    "reseccion",
                    models.IntegerField(
                        choices=[
                            (1, "Amputación"),
                            (2, "Histerectomía radical"),
                            (3, "Histerectomía simple"),
                            (4, "Exenteración pélvica (especifique órganos incluidos)"),
                            (5, "Salpingo-oophorectomy bilateral"),
                            (6, "Salpingo-oophorectomy derecha"),
                            (7, "Salpingo-oophorectomy izquierdo"),
                            (8, "Salpingo-oophorectomy, lado no especificado"),
                            (9, "Oophorectomía derecha"),
                            (10, "Oophorectomía izquierdo"),
                            (11, "Oophorectomía, no tome partido especificado"),
                            (12, "Salpingectomía bilateral"),
                            (13, "Salpingectomía derecha"),
                            (14, "Salpingectomía izquierda"),
                            (15, "Salpingectomíaespecificado"),
                            (16, "Resección vaginal del muñón"),
                            (17, "Omentectomía"),
                            (18, "Otro (especifique)"),
                        ],
                        verbose_name="La resección",
                    ),
                ),
                (
                    "exenteracion_pelvica_especifique",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Exenteración pélvica(especifique órganos incluidos): ",
                    ),
                ),
                (
                    "otra_reseccion_especifique",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Otra Resección(especifique):",
                    ),
                ),
                (
                    "tipo_hysterectomy",
                    models.IntegerField(
                        choices=[
                            (1, "Abdominal"),
                            (2, "Vaginal"),
                            (3, "Vaginal, de asistencia laparoscópico"),
                            (4, "Laparoscopic"),
                            (5, "Laparoscopic, de asistencia robótico"),
                            (6, "Otro del + (especifique)"),
                            (7, "No especificado"),
                        ],
                        verbose_name="Tipo Hysterectomy",
                    ),
                ),
                (
                    "otro_tipo_hysterectomy",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Otro del + (especifique): ",
                    ),
                ),
                (
                    "afectacion_otros_organos",
                    models.IntegerField(
                        choices=[
                            (1, "no se aplica"),
                            (2, "no identificado"),
                            (3, "parametrio derecho"),
                            (4, "parametrio izquierdo"),
                            (5, "parametrio (no especificado)"),
                            (6, "vagina"),
                            (7, "vagina, 1/3 inferior"),
                            (8, "vagina (la posición no especificada)"),
                            (9, "ovario derecho"),
                            (10, "ovario izquierdo"),
                            (11, "ovario (no especificado)"),
                            (12, "trompa uterina derecha"),
                            (13, "trompa uterina izquierda"),
                            (14, "trompa uterina (no especificado)"),
                            (15, "pared pélvica"),
                            (16, "pared de la vejiga"),
                            (17, "mucosa de la vejiga"),
                            (18, "pared rectal"),
                            (19, "mucosa del intestino"),
                            (20, "Omentum"),
                            (21, "otro órgano (especifique)"),
                            (22, "no puede ser determinado (explique)"),
                        ],
                        verbose_name="Afectación de otros órganos",
                    ),
                ),
                (
                    "afectacion_otro_organo",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Afectación de otro órgano(especifique):",
                    ),
                ),
                (
                    "afectacion_no_determinada",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Afectación no puede ser determinada(explique):",
                    ),
                ),
                (
                    "ectocervical_margin_no_puede_evaluarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="Ectocervical Margin no puede ser evaluado",
                    ),
                ),
                (
                    "ectocervical_margin_no_evaluado_especif",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Ectocervical Margin no puede ser evaluado (explique)",
                    ),
                ),
                (
                    "ectocervical_uninvol_carci_invasive",
                    models.BooleanField(
                        default=False,
                        verbose_name="Uninvolved por carcinoma del invasive",
                    ),
                ),
                (
                    "ectocervical_margin_distancia_carcinoma",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="La distancia del + de carcinoma del invasive de margen(los milímetros):",
                    ),
                ),
                (
                    "ectocervical_margin_posicion_specify1",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El + la posición(especificar):",
                    ),
                ),
                (
                    "ectocervical_involucrado_carcinoma_invasive",
                    models.BooleanField(
                        default=False,
                        verbose_name="Involucrado por carcinoma del invasive",
                    ),
                ),
                (
                    "ectocervical_especifique_posicion",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Especifique posición(si es posible)",
                    ),
                ),
                (
                    "ectocervical_uninvolved_intra_neop",
                    models.BooleanField(
                        default=False,
                        verbose_name="Uninvolved por intraepithelial neoplasia",
                    ),
                ),
                (
                    "ectocervical_invol_lesion_escam",
                    models.BooleanField(
                        default=False,
                        verbose_name="Involucrado por lesión escamosa (CIN 2-3) del intraepithelial de calidad superior",
                    ),
                ),
                (
                    "ectocervical_margin_posicion_specify2",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El + la posición(especificar):",
                    ),
                ),
                (
                    "ectocervical_invol_adenocarcinoma",
                    models.BooleanField(
                        default=False,
                        verbose_name="Involucrado por adenocarcinoma en situ(las IAs)",
                    ),
                ),
                (
                    "ectocervical_margin_posicion_specify3",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El + la posición(especificar):",
                    ),
                ),
                (
                    "radial_margin_no_puede_evaluarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="Radial Margin no puede ser evaluado",
                    ),
                ),
                (
                    "radial_margin_no_evaluado_especif",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Radial Margin no puede ser evaluado (explique)",
                    ),
                ),
                (
                    "radial_uninvol_carci_invasive",
                    models.BooleanField(
                        default=False,
                        verbose_name="Uninvolved por carcinoma del invasive",
                    ),
                ),
                (
                    "radial_margin_distancia_carcinoma",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="La distancia del + de carcinoma del invasive de margen(los milímetros):",
                    ),
                ),
                (
                    "radial_margin_posicion_specify",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El + la posición(especificar):",
                    ),
                ),
                (
                    "radial_involucrado_carcinoma_invasive",
                    models.BooleanField(
                        default=False,
                        verbose_name="Involucrado por carcinoma del invasive",
                    ),
                ),
                (
                    "radial_especifique_posicion",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Especifique posición(si es posible)",
                    ),
                ),
                (
                    "invasion_limphovascular_notaG",
                    models.IntegerField(
                        choices=[
                            (1, "no identificado"),
                            (2, "presente"),
                            (3, "no puede estar resuelto"),
                        ],
                        verbose_name="La Invasión del Lymphovascular(la Nota G)",
                    ),
                ),
                (
                    "ganglios_linfaticos_encontrados",
                    models.BooleanField(
                        default=False,
                        verbose_name="Ninguno de los ganglios linfáticos se sometieron o encontraron",
                    ),
                ),
                (
                    "num_nodos_con_metastasis",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="El número de Nodos con Metástasis (excluye a ITCs):",
                    ),
                ),
                (
                    "num_no_puede_determinarce",
                    models.BooleanField(
                        default=False, verbose_name="El número no puede ser determinado"
                    ),
                ),
                (
                    "num_no_determinado_especif",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El número no puede ser determinado (explique):",
                    ),
                ),
                (
                    "num_nodos_celdas_aisladas",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="El número de Nodos con Celdas Aisladas (ITCs) del Tumor (0.2 mm o menos) (si aplicable)",
                    ),
                ),
                (
                    "num_nodos_no_puede_determinarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="El número no puede ser determinado ",
                    ),
                ),
                (
                    "num_nodos_no_determinado_especif",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El número de nodos no puede ser determinado (explique):",
                    ),
                ),
                (
                    "num_ganglios_con_tumor",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Especifique el número de Ganglio Linfático(s) con Tumor (si aplicable)",
                    ),
                ),
                (
                    "total_num_nodos_examinados",
                    models.IntegerField(
                        verbose_name="Número total de Nodo Examinado (el señalizador y el poco señalizador)"
                    ),
                ),
                (
                    "num_total_no_puede_determinarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="El número no puede ser determinado ",
                    ),
                ),
                (
                    "num_total_no_determinado_especif",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El número no puede ser determinado (explique):",
                    ),
                ),
                (
                    "sitios_especif",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="Especifique Sitio(s) ",
                    ),
                ),
                (
                    "num_nodos_senalizador_exami",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Numere de Nodos del Señalizador Examinados:",
                    ),
                ),
                (
                    "num_serial_no_puede_determinarce",
                    models.BooleanField(
                        default=False,
                        verbose_name="El número no puede ser determinado ",
                    ),
                ),
                (
                    "num_serial_no_determinado_especif",
                    models.CharField(
                        blank=True,
                        max_length=5000,
                        null=True,
                        verbose_name="El número no puede ser determinado (explique):",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "biopsy",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="biopsy_diagnostic_gynecology",
                        to="pathologic_anathomy.biopsyrequest",
                    ),
                ),
            ],
            options={
                "verbose_name": "Diagnostico Biopcia de Ginecología(Cervix)",
                "verbose_name_plural": "Diagnosticos Biopcias de Ginecología(Cervix)",
                "ordering": ["id"],
            },
        ),
    ]
