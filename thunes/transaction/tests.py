import sys

from django.test import TestCase, Client
from django.urls import reverse

from quotation.models import Quotation, Source, Destination
from sender.models import Sender
from beneficiary.models import Beneficiary
from .models import Transaction

from .serializers import TransactionSerializer


# Create your tests here.


class TransactionTestCase(TestCase):

    def setUp(self) -> None:
        """
        the setUp function to create a transaction entity
        """
        senderEntity = Sender.objects.create(lastname='Doe', firstname='Joe', nationality_country_iso_code='FRA',
                                             date_of_birth='1970-07-01', country_of_birth_iso_code='FRA', gender='Male',
                                             address='42 Rue des fleurs', postal_code='75000', city='Paris',
                                             country_iso_code='FRA', msisdn='1123131413', email='kzhang@microfocus.com',
                                             id_type='PASSPORT', id_number='1123131413', id_delivery_date='2019-12-18',
                                             occupation='Support')
        beneficiaryEntity = Beneficiary.objects.create(id=1, lastname='Doe', firstname='Jane',
                                                       nationality_country_iso_code='FRA', date_of_birth='1970-07-01',
                                                       country_of_birth_iso_code='FRA', gender='Male',
                                                       address='42 Rue des fleurs', postal_code='75000', city='Paris',
                                                       country_iso_code='FRA', msisdn='1123131413',
                                                       email='kzhang@microfocus.com', id_type='PASSPORT',
                                                       id_number='1123131413', occupation='Teacher')
        sourceEntity = Source.objects.create(country_iso_code='SDP', currency='SGD', amount=100)
        sourceEntity1 = Source.objects.create(country_iso_code='SDP', currency='SGD', amount=100)
        destinationEntity = Destination.objects.create(currency='GHS', amount=100)
        destinationEntity1 = Destination.objects.create(currency='GHS', amount=100)
        quotationentity = Quotation.objects.create(quotation_id=2982513, external_id=154730507385, payer_id=1669,
                                                   mode='SOURCE_AMOUNT', source=sourceEntity,
                                                   destination=destinationEntity)
        quotationentity1 = Quotation.objects.create(quotation_id=2982513, external_id=154730507385, payer_id=1669,
                                                    mode='SOURCE_AMOUNT', source=sourceEntity1,
                                                    destination=destinationEntity1)
        Transaction.objects.create(transaction_id='931048', status='20000', status_message='20000', status_class='2',
                                   status_class_message='2', external_id='157103991034', quotation=quotationentity,
                                   creation_date='2019-12-30T07:30:35.009069Z', sender=senderEntity,
                                   beneficiary=beneficiaryEntity, retail_fee_currency='EUR',
                                   purpose_of_remittance='FAMILY_SUPPORT')
        Transaction.objects.create(transaction_id='931048', status='10000', status_message='10000', status_class='1',
                                   status_class_message='1', external_id='157103991034', quotation=quotationentity1,
                                   creation_date='2019-12-30T07:30:35.009069Z', sender=senderEntity,
                                   beneficiary=beneficiaryEntity, retail_fee_currency='EUR',
                                   purpose_of_remittance='FAMILY_SUPPORT')
        self.client = Client()

    def test_transaction_list_connectivity_will_pass(self):
        """
        the test to test the function of transaction entity listing
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('transaction:transaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_transaction_list_validate_content_that_will_pass(self):
        """
        the test to test the function of transaction entity listing and content validation
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('transaction:transaction-list')
        response = self.client.get(url)

        # get all seralize the transaction entity list
        transactionentities = Transaction.objects.all()
        serializer = TransactionSerializer(transactionentities, many=True)
        self.assertEqual(response.json(), [
            {'id': 1, 'transaction_id': '931048',
             'quotation_id': {
                 'id': 1,
                 'quotation_id': '2982513',
                 'external_id': '154730507385',
                 'payer_id': '1669',
                 'mode': 'SOURCE_AMOUNT',
                 'source_id': {'id': 1, 'country_iso_code': 'SDP', 'currency': 'SGD', 'amount': 100},
                 'destination_id': {'id': 1, 'currency': 'GHS', 'amount': 100}
             }, 'status': '20000', 'status_message': '20000', 'status_class': '2', 'status_class_message': '2',
             'external_id': '157103991034', 'external_code': '', 'payer_transaction_reference': '',
             'payer_transaction_code': '', 'creation_date': '2020-01-05T08:48:44.888833Z', 'expiration_date': None,
             'sender_id': 1, 'beneficiary_id': 1, 'callback_url': '', 'wholesale_fx_rate': None, 'retail_rate': None,
             'retail_fee': None, 'retail_fee_currency': 'EUR', 'purpose_of_remittance': 'FAMILY_SUPPORT',
             'additional_information_1': '', 'additional_information_2': '', 'additional_information_3': ''},
            {'id': 2, 'transaction_id': '931048',
             'quotation_id': {
                 'id': 2,
                 'quotation_id': '2982513',
                 'external_id': '154730507385',
                 'payer_id': '1669',
                 'mode': 'SOURCE_AMOUNT',
                 'source_id': {'id': 2, 'country_iso_code': 'SDP', 'currency': 'SGD', 'amount': 100},
                 'destination_id': {'id': 2, 'currency': 'GHS', 'amount': 100}
             }, 'status': '10000', 'status_message': '10000', 'status_class': '1', 'status_class_message': '1',
             'external_id': '157103991034', 'external_code': '',
             'payer_transaction_reference': '',
             'payer_transaction_code': '', 'creation_date': '2020-01-05T08:48:44.889863Z', 'expiration_date': None,
             'sender_id': 1, 'beneficiary_id': 1, 'callback_url': '', 'wholesale_fx_rate': None, 'retail_rate': None,
             'retail_fee': None, 'retail_fee_currency': 'EUR', 'purpose_of_remittance':'FAMILY_SUPPORT',
             'additional_information_1': '', 'additional_information_2': '', 'additional_information_3': ''}
        ])
        self.assertEqual(response.status_code, 200)

    def test_transaction_create_without_postbody_will_pass(self):
        """
        the test to test the function of creating the transaction entity with a quotation_id without post body
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('transaction:transaction-create', kwargs={'quotation_id': 1})
        response = self.client.post(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_transaction_create_with_postbody_that_will_pass(self):
        """
        the test to test the function of creating the transaction entity with a quotation_id without post body
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        post_body = {
            'sender': {
                'lastname': 'Doe',
                'firstname': 'Joe',
                'nationality_country_iso_code': 'FRA',
                'date_of_birth': '1970-07-01',
                'country_of_birth_iso_code': 'FRA',
                'gender': 'Male',
                'address': '42 Rue des fleurs',
                'postal_code': '75000',
                'city': 'Paris',
                'country_iso_code': 'FRA',
                'msisdn': '1123131413',
                'email': 'kzhang@microfocus.com',
                'id_type': 'SENIOR_CITIZEN_ID',
                'id_number': '1123131413',
                'id_delivery_date': '2019-12-18',
                'occupation': 'Support'
            },
            'beneficiary': {
                'lastname': 'Doe',
                'firstname': 'Jane',
                'nationality_country_iso_code': 'FRA',
                'date_of_birth': '1970-07-01',
                'country_of_birth_iso_code': 'FRA',
                'gender': 'Male',
                'address': '42 Rue des fleurs',
                'postal_code': '75000',
                'city': 'Paris',
                'country_iso_code': 'FRA',
                'msisdn': '1123131413',
                'email': 'kzhang@microfocus.com',
                'id_type': 'PAN_CARD',
                'id_number': '1123131413',
                'id_delivery_date': '2019-12-18',
                'occupation': 'Teacher'
            },
            'credit_party_identifier': {
                'bank_account_number': '0123456789',
                'msisdn': '+263775892100',
                'swift_bic_code': 'ABCDEFGH'
            },
            'external_id': '157821594622',
            'retail_fee': 1,
            'retail_fee_currency': 'EUR',
            'purpose_of_remittance': 'FAMILY_SUPPORT',
            'callback_url': None
        }
        url = reverse('transaction:transaction-create', kwargs={'quotation_id': 1})
        response = self.client.post(url, data=post_body, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_transaction_create_will_fail(self):
        """
        the test to test the function of creating the transaction entity without a quotation_id
        """
        try:
            url = reverse('transaction:transaction-create', kwargs={'quotation_id': None})
            response = self.client.post(url, content_type='application/json')
            return self.assertTrue(response.status_code, 200)
        except Exception as e:
            print('we are testing the creating the transaction and it failed with reason:', e)
            pass

    def test_transaction_confirm_connectivity_will_pass(self):
        """
        the test to test the function of confirming the transaction entity
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('transaction:transaction-entity-by-id-confirm', kwargs={'transactionDB_id': 1})
        response = self.client.post(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_transaction_retrieve_connectivity_will_pass(self):
        """
        the test to test the function of retriving the transaction entity
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('transaction:transaction-entity-by-id-retrieve', kwargs={'pk': 1})
        response = self.client.get(url)
        return self.assertTrue(response.json(), {'id': 1, 'status': '20000', 'status_message': '20000',
                                                 'status_class': '2', 'status_class_message': '2', 'quotation': 1,
                                                 'external_id': '157103991034', 'external_code': '',
                                                 'payer_transaction_reference': '', 'payer_transaction_code': '',
                                                 'creation_date': '2020-01-03T08:36:10.921402Z',
                                                 'expiration_date': None, 'callback_url': '', 'wholesale_fx_rate': None,
                                                 'retail_rate': None, 'sender': 1, 'beneficiary': 1, 'retail_fee': None,
                                                 'retail_fee_currency': 'EUR',
                                                 'purpose_of_remittance': 'FAMILY_SUPPORT'})

    def test_transaction_beneficiary_sender_list_connectivity_that_will_pass(self):
        """
        the test to test the function of listing the beneficiary and sender entities list
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('transaction:transaction-beneficiary-sender-list') + '?lastname=Doe&firstname=Joe'
        response = self.client.get(url)
        self.assertEqual(response.json(),
                         [{'beneficiary_id': 1, 'beneficiary_name': 'Beneficiary Name: Doe Jane', 'counter': 2}])

    def test_transaction_beneficiary_sender_list_without_input_that_will_pass(self):
        """
        the test to test the function of listing the used beneficiary and sender entities list without input
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('transaction:transaction-beneficiary-sender-list')
        response = self.client.get(url)
        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)
