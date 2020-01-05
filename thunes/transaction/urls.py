from django.urls import path
from .views import TransactionListView, TransactionCreateView, TransactionDetailRetrieveView, \
    BeneficiaryListBySenderName, TransactionConfirmView, TransactionDetailUpdateView

app_name = 'transaction'

urlpatterns = [
    # beneficiary api view
    path('<int:quotation_id>', TransactionCreateView.as_view(), name='transaction-create'),
    path('', TransactionListView.as_view(), name='transaction-list'),
    path('confirm/<int:transactionDB_id>', TransactionConfirmView.as_view(), name='transaction-entity-by-id-confirm'),
    path('detail/<int:pk>', TransactionDetailRetrieveView.as_view(), name='transaction-entity-by-id-retrieve'),
    path('update/<int:pk>', TransactionDetailUpdateView.as_view(), name='transaction-entity-by-id-update'),
    path('sender', BeneficiaryListBySenderName.as_view(), name='transaction-beneficiary-sender-list')
]