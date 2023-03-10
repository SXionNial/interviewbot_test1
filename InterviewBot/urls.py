"""InterviewBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .router import router
from .views import(
    LoginViewAPI, 
    LogoutViewAPI,
    UpdateAccountViewAPI,
    AccountDetailsViewAPI,
    JobOfferingsAdminListViewAPI,
    AppliedJobApplicantsListViewAPI,
    SavedJobUserViewAPI,
    AppliedJobUserViewAPI,
    JobOfferingsViewAPI,
    UnsaveJobOfferingDestroyView,
    SaveJobOfferingCreateViewAPI,
    AppliedJobListViewAPI,

    LoginView,
    password_reset_request
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrator/', include('administrator.urls', namespace='administrator')),
    path('user/', include('user.urls', namespace="user")),

    # API
    path('api/', include(router.urls)), #used - for user registration
    path('api/login/', LoginViewAPI.as_view()), #used - for login
    path('api/logout/', LogoutViewAPI.as_view()), #used - for logout
    path('api/update-account/', UpdateAccountViewAPI.as_view()), #used - to update account settings

    path('api/<user_id>/saved-jobs/details/', SavedJobUserViewAPI.as_view()), #used - for saved job viewing (USER)
    path('api/<user_id>/applied-jobs/details/', AppliedJobUserViewAPI.as_view()), #used -  for applied job viewing (USER)
    path('api/<user_id>/job-offerings/details/', JobOfferingsViewAPI.as_view()), #used - for job offerings viewing (USER)
    path('api/saved-jobs/create/', SaveJobOfferingCreateViewAPI.as_view()), #used - to SAVE job offerings (USER)
    path('api/saved-jobs/<int:pk>/delete/', UnsaveJobOfferingDestroyView.as_view()), #used - to UNSAVE job offerings (USER)

    path('api/accounts/', AccountDetailsViewAPI.as_view()), #used - to get the email of all registered accounts
    path('api/admin/<admin_id>/job-offerings/', JobOfferingsAdminListViewAPI.as_view()), # used - to get the job offerings of an admin
    path('api/applied-jobs/applicants/<job_id>/', AppliedJobApplicantsListViewAPI.as_view()), #used - can be used to check if who applied a certain job
    path('api/applied-jobs/', AppliedJobListViewAPI.as_view()), # can be used to count how many applicants have applied in a job of a certain staff


    # Login
    path('', LoginView.as_view(), name="login_view"),

    # Password Reset
    path('password_reset/', password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),  

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)