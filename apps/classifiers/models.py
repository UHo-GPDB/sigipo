from django.db.models import CharField, Model


class Topography(Model):
    """Model representation of a topography."""

    name = CharField(verbose_name="Nombre", max_length=255)

    class Meta:
        """topography Meta class."""

        verbose_name = "Topografía"
        verbose_name_plural = "Topografías"
        ordering = ["pk"]
        default_permissions = ()

    def __str__(self):
        """topography str representation."""
        """String representation of topography."""
        return f"{self.name}"


class Morphology(Model):
    """Model representation of a morphology."""

    name = CharField(verbose_name="Nombre", max_length=255)

    class Meta:
        """morphology Meta class."""

        verbose_name = "Morfología"
        verbose_name_plural = "Morfologías"
        ordering = ["pk"]
        default_permissions = ()

    def __str__(self):
        """String representation of morphology."""
        return f"{self.name}"


class Study(Model):
    """Model representation of a Study."""

    name = CharField(max_length=500, blank=False, null=False)

    class Meta:
        """Study Meta class."""

        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"
        ordering = ["pk"]
        default_permissions = ()

    def __str__(self):
        """Study Str representation."""
        return self.name


class RadioIsotope(Model):
    """Model representation of a Radio Isotope."""

    name = CharField(max_length=500, blank=False, null=False)

    class Meta:
        """Radio Isotope Meta Class."""

        verbose_name = "Radio isótopo"
        verbose_name_plural = "Radio isótopo"
        ordering = ["pk"]
        default_permissions = ()

    def __str__(self):
        """Radio Isotope str representation."""
        return self.name
