from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from wagtail import hooks
from wagtail.admin.site_summary import SummaryItem


class MyProjectNameSummaryItem(SummaryItem):
    order = 50
    template_name = "my_project_name/admin/my_project_name_summary.html"


@hooks.register("construct_homepage_summary_items")
def register_my_project_name_summary_item(request, summary_items):
    summary_items.append(MyProjectNameSummaryItem(request))


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path(
            "jsi18n/",
            JavaScriptCatalog.as_view(packages=["my_project_name"]),
            name="javascript_catalog",
        ),
        # Add other package-scoped URLs here so they are access-restricted to the admin.
    ]

    return [
        path(
            "my_project_name/",
            include(
                (urls, "my_project_name"),
                namespace="my_project_name",
            ),
        )
    ]
