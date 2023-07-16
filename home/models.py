from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
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

class MyDetailsPage(Page):
    title_header = models.CharField("My Details title", max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('title_header')
    ]

# class MyUser(AbstractUser):

#     username = None
#     email = models.EmailField(_("email address"), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
