import graphene
from graphene_django import DjangoObjectType
from .models import Payment, PaymentDetail
from core import prefix_filterset, filter_validity, ExtendedConnection


from contribution.schema import PremiumGQLType


class PaymentGQLType(DjangoObjectType):
    class Meta:
        model = Payment
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "uuid": ["exact"],
            "status": ["exact", "isnull"],
            "expected_amount": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "received_amount": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "transfer_fee": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "officer_code": ["exact", "isnull"],
            "phone_number": ["exact", "istartswith", "icontains", "iexact", "isnull"],
            "request_date": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "received_date": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "matched_date": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "payment_date": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "date_last_sms": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "transaction_no": ["exact", "istartswith", "icontains", "iexact", "isnull"],
            "origin": ["exact", "istartswith", "icontains", "iexact", "isnull"],
            "receipt_no": ["exact", "istartswith", "icontains", "iexact", "isnull"],
            "rejected_reason": ["exact", "istartswith", "icontains", "iexact", "isnull"],
            "language_name": ["exact", "istartswith", "icontains", "iexact", "isnull"],
            "type_of_payment": ["exact", "istartswith", "icontains", "iexact", "isnull"]
        }
        connection_class = ExtendedConnection


class PaymentDetailGQLType(DjangoObjectType):
    class Meta:
        model = PaymentDetail
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "product_code": ["exact", "isnull"],
            "insurance_number": ["exact", "isnull"],
            "policy_stage": ["exact", "isnull"],
            "expected_amount": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "amount": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            "enrollment_date": ["exact", "lt", "lte", "gt", "gte", "isnull"],
            **prefix_filterset("premium__", PremiumGQLType._meta.filter_fields),
            **prefix_filterset("payment__", PaymentGQLType._meta.filter_fields)
        }
        connection_class = ExtendedConnection
