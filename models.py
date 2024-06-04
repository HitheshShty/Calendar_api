from django.db import models
from django.utils.translation import gettext_lazy as _
class Application(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=250,
        unique=True,
    )
    type = models.CharField(
        max_length=32,
        verbose_name=_("Type"),
    )
    sub_type = models.CharField(
        max_length=32,
        verbose_name=_("Sub Type"),
    )

    description = models.TextField(
        _("Description"),
        blank=True,
        null=True,
    )
    configuration_template = models.TextField(
        _("Configuration Template"),
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    

class ApplicationInstance(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=250,
        unique=True,
    )
    application = models.ForeignKey(
        Application,
        on_delete=models.PROTECT,
        verbose_name=_("Application"),
    )
    configuration_data = models.TextField(
        _("Configuration Data"),
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    last_connected_at = models.DateTimeField(
        _("Last Connected"),
        blank=True,
        null=True,
        editable=False,

    )
    log_message = models.TextField(
        _("Log message"),
        blank=True,
        null=True,
    )

