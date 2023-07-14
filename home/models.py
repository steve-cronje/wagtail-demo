from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    title_header = models.CharField("Homepage Title", default="This is the homepage!", max_length=150)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title_header'),
        FieldPanel('body')
    ]
