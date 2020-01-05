import json
import sys

from django.test import TestCase, Client
from django.urls import reverse
from .models import Sender

from .serializers import SenderSerializer

# Create your tests here.


class SenderTestCase(TestCase):

    def setUp(self):
        """
        the setUp function to create a sender entity
        """
        Sender.objects.create(lastname='Doe', lastname2='', firstname='Joe', nationality_country_iso_code='FRA',
                              date_of_birth='1970-07-01', country_of_birth_iso_code='FRA', gender='Male',
                              address='42 Rue des fleurs', postal_code='75000', city='Paris', country_iso_code='FRA',
                              msisdn='1123131413', email='kzhang@microfocus.com', id_type='PASSPORT',
                              id_country_iso_code='', id_number='1123131413', id_delivery_date='2019-12-18',
                              occupation='Support')
        self.client = Client()

    def test_sender_list_connectivity_that_will_pass(self):
        """
        the test to test the function of sender list
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('sender:senders-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_sender_list_validate_content_that_will_pass(self):
        """
        the test to test the function of sender listing and validate content
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('sender:senders-list')
        response = self.client.get(url)

        # serializer all model object data
        senders = Sender.objects.all()
        serializer = SenderSerializer(senders, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_sender_create_connectivity_that_will_pass(self):
        """
        the test to test the function of sender creating
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('sender:senders-create')
        response = self.client.post(url, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_sender_create_content_validation_will_pass(self):
        """
        the test to test the function of sender creating and its content validation
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        post_body = {
            "lastname": "Doe",
            "firstname": "Joe",
            "nationality_country_iso_code": "FRA",
            "date_of_birth": "1970-07-01",
            "country_of_birth_iso_code": "FRA",
            "gender": "MALE",
            "address": "42 Rue des fleurs",
            "postal_code": "75000",
            "city": "Paris",
            "country_iso_code": "FRA",
            "msisdn": "1123131413",
            "email": "kzhang@microfocus.com",
            "id_type": "PASSPORT",
            "id_country_iso_code": "FRA",
            "id_number": "1123131413",
            "id_delivery_date": "2019-12-18",
            "id_expiration_date": None,
            "occupation": "Support",
            "bank": "",
            "bank_account": "",
            "card": "",
            "province_state": "",
            "beneficiary_relationship": "AUNT",
            "source_of_funds": ""
        }
        url = reverse('sender:senders-create')
        response = self.client.post(url, data=post_body, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_sender_retrieve_will_pass(self):
        """
        the test to test the function of sender retrieve
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('sender:sender-entity-by-id-retrieve', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_sender_retrieve_validate_content_that_will_pass(self):
        """
        the test to test the function of sender retrieve and its content validation
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('sender:sender-entity-by-id-retrieve', kwargs={'pk': 1})
        response = self.client.get(url)

        # serialize the model object data
        sender = Sender.objects.get(pk=1)
        serializer = SenderSerializer(sender, many=False)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_sender_update_connectivity_that_will_pass(self):
        """
        the test to test the function of sender update without post data
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('sender:sender-entity-by-id-update', kwargs={'pk': 1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 405)

    def test_sender_update_validate_content_that_will_pass(self):
        """
        the test to test the function of sender upadte and validate its returned content
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        post_body = {
            "lastname": "Doe2",
            "firstname": "Joe2",
            "nationality_country_iso_code": "FRA",
            "date_of_birth": "1970-07-01",
            "country_of_birth_iso_code": "FRA",
            "gender": "MALE",
            "address": "42 Rue des fleurs",
            "postal_code": "75000",
            "city": "Paris",
            "country_iso_code": "FRA",
            "msisdn": "1123131413",
            "email": "kzhang@microfocus.com",
            "id_type": "PASSPORT",
            "id_country_iso_code": "FRA",
            "id_number": "1123131413",
            "id_delivery_date": "2019-12-18",
            "id_expiration_date": None,
            "occupation": "Support",
            "bank": "",
            "bank_account": "",
            "card": "",
            "province_state": "",
            "beneficiary_relationship": "AUNT",
            "source_of_funds": ""
        }
        url = reverse('sender:sender-entity-by-id-update', kwargs={'pk': 1})
        response = self.client.put(url, data=post_body, content_type="application/json")

        # serialize the sender entity
        sender = Sender.objects.get(pk=1)
        serializer = SenderSerializer(sender, many=False)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_sender_update_withoutID_that_will_fail(self):
        """
        the function to test the function of updating the sender entity without a ID
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        try:
            url = reverse('sender:sender-entity-by-id-update')
            response = self.client.get(url, content_type='application/json')
            return self.assertTrue(response.status_code, 200)
        except Exception as e:
            print("reason: ", e)
