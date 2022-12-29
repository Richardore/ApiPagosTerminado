from version2.ve2.serializers import ExpiredPaymentsSerializers, PaymentUsersSerializers, ServicesSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from version2.models import Services, Expired_payments, Payment_user
from version2.ve2.pagination import SimplePagination

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser




class ServicesViewUser(ModelViewSet):
    queryset = Services.objects.all()

    throttle_scope = 'Servicio'
    

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list','retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update','partial_update','destroy','retrieve','create']:
            permission_classes = [IsAdminUser]
        return [permissions() for permissions in permission_classes]
    def get_serializer_class(self):
        return ServicesSerializers
        

class PaymentUsersViewUser(ModelViewSet):
    queryset = Payment_user.objects.all()
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['PaymentDate', 'ExpirationDate']
    
    throttle_scope = 'pagos'

    def get_permissions(self):
       
        permission_classes = []
        if self.action in  ['list','retrieve','create']:
        
            permission_classes = [IsAuthenticated]
        elif self.action in ['update','partial_update','destroy']:
            permission_classes = [IsAdminUser]
        return [permissions() for permissions in permission_classes]

    def get_serializer_class(self):
        return PaymentUsersSerializers

    def create(self, request, *args, **kwargs):
        payment_user_id = super().create(request, *args, **kwargs)
        last_pay = Payment_user.objects.order_by('id').first()
        payment = Payment_user.objects.get(id=last_pay.id)
        if payment.ExpirationDate < payment.PaymentDate:
            penalty = payment.Amount * 2.50
            expired_payment = Expired_payments(payment_user_id=payment,penalty_free_amount=penalty)
            expired_payment.save()
        return payment_user_id



class ExpiredPaymentViewUser(ModelViewSet):
    queryset = Expired_payments.objects.all()
    pagination_class = SimplePagination

    throttle_scope = 'Expirado'

    def get_permissions(self):
        permission_classes = []
        if self.action in  ['list','retrieve','create']:
            permission_classes = [IsAuthenticated]

        elif self.action in  ['update','partial_update','destroy','retrieve']:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return ExpiredPaymentsSerializers
