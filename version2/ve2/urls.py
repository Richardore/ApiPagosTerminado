from rest_framework.routers import DefaultRouter
from version2.ve2.api import ExpiredPaymentViewUser, PaymentUsersViewUser, ServicesViewUser

route = DefaultRouter()

route.register(r"services", ServicesViewUser, basename = "services")
route.register(r"payment-users", PaymentUsersViewUser, basename = "payment-user")
route.register(r"expired-payment", ExpiredPaymentViewUser, basename = "expired-payment")

urlpatterns = route.urls