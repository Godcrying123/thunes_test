from django.urls import path

from .views import BeneficiaryListView, BeneficiaryCreateView, BeneficiaryDetailRetrieveView, \
    BeneficiaryDetailUpdateView

app_name = 'beneficiary'

urlpatterns = [
    # beneficiary api view
    path('', BeneficiaryListView.as_view(), name='beneficiaries-list'),
    path('create', BeneficiaryCreateView.as_view(), name='beneficiaries-create'),
    path('<int:pk>', BeneficiaryDetailRetrieveView.as_view(), name='beneficiary-entity-by-id-retrieve'),
    path('update/<int:pk>', BeneficiaryDetailUpdateView.as_view(), name='beneficiary-entity-by-id-update'),
]
