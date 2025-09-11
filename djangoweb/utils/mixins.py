from django.urls import reverse


# CBVs
class BreadcrumbsMixin:

    breadcrumbs = []

    def get_breadcrumbs(self):
        return self.breadcrumbs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = self.get_breadcrumbs()

        return context


# Function view
def get_website_breadcrumbs(extra=None):

    breadcrumbs = [
        {"name": "Home", "url": reverse("website:home")},
    ]
    if extra:
        breadcrumbs.extend(extra)

    return breadcrumbs
