from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import reverse_lazy
from .views import (
    SeekerRegistrationView,
    SeekerLoginView,
    SeekerDashboardView,
    SeekerLogoutView,
    SeekerCsvUploadView,
    SeekerTargetRolesTagsView,
    clear_tags,
    AddSeekerCSVContactInformationView
)

urlpatterns = [
    path('register/', SeekerRegistrationView.as_view(), name='seeker_registration'),
    path('dashboard/', SeekerDashboardView.as_view(), name='seeker_dashboard'),
    path('login/', SeekerLoginView.as_view(), name='seeker_login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('seeker_logout')), name='seeker_logout'),
    path('logout-page/', SeekerLogoutView.as_view(), name='seeker_logout'),
    path('csv-upload/', SeekerCsvUploadView.as_view(), name='seeker_csv_upload'),
    path('tags/', SeekerTargetRolesTagsView.as_view(), name='seeker_roles_tags'),
    path('tags/<str:search_query>/', SeekerTargetRolesTagsView.as_view(), name='seeker_roles_tags'),
    path('clear-tags/', clear_tags, name='clear_tags'),
    path('add_contact_info/<int:cv_entry_id>/', AddSeekerCSVContactInformationView.as_view(), name='add_contact_info')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
