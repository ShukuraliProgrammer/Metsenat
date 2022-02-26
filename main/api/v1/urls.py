from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    # login with JWT authenticted
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # login with private function
    # path('login/', views.loginView),
    # path('logout/', views.logout),
    # dashboard
    path('dashboard/',views.DashboardView.as_view()),
    # path('<int:pk>/',views.StudentSponsor.as_view()),
    # sponsors
    path('sponsors/', views.SponsorView.as_view()),
    path('sponsors/<int:pk>/', views.SponsorDetailView.as_view()),

    # university
    path('university/', views.UniversityView.as_view()),

    # students
    path('students/', views.StudentView.as_view()),
    path('students/<int:pk>/', views.StudentDetailView.as_view()),

    # sponsorships
    path('sponsorships/', views.SponsorshipView.as_view()),
    path('sponsorships/<int:pk>/', views.SponsorshipDetailView.as_view()),
]