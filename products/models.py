from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from django.contrib.auth.models import User

# Create your models here.
class ProductPage(Page):
    title_header = models.CharField("Products page title", max_length=150)

    def get_context(self, request):
        context = super().get_context(request)
        # Only getting published products!
        context['products'] = self.get_children().live()
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel('title_header')
    ]


class ProductDetailPage(Page):
    title_header = models.CharField("Product title", max_length=150)
    body = RichTextField(blank=True)
    registered_users = models.ManyToManyField(User, related_name='products')

    search_fields = Page.search_fields + [
        index.SearchField('title_header')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('title_header'),
        FieldPanel('body')
    ]