from django.urls import path

from package.views import PackageView, PackageListView

urlpatterns = [
    path('<int:package_pk>/<int:advertisement_pk>/', PackageView.as_view(), name='package-detail'),
    path('list/<int:advertisement_pk>/', PackageListView.as_view(), name='package-list'),
]
