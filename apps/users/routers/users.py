from rest_framework import routers
from apps.users.viewsets import (
    UserViewSet,
    EmployeeProfileViewset,
    EmployeeProfileAvatarModelViewSet,
    JobTitleModelViewSet,
)

router = routers.DefaultRouter()

# router.register(r"", UserViewSet)
# router.register(r"job_title", JobTitleModelViewSet)
router.register(r"profile", EmployeeProfileViewset)
