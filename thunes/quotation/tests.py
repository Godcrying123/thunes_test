import json
import sys

from django.test import TestCase, Client
from django.urls import reverse

from .models import Quotation, Source, Destination

# Create your tests here.


class QuotationTestCase(TestCase):

    def setUp(self) -> None:
        """
        the setUp function to create a mock quotation, source and destination entity
        """
        self.client = Client()
        sourceEntity = Source.objects.create(country_iso_code='SDP', currency='SGD', amount=100)
        destinationEntity = Destination.objects.create(currency='GHS', amount=100)
        Quotation.objects.create(quotation_id=2982513, external_id=154730507385, payer_id=1669, mode='SOURCE_AMOUNT',
                                 source=sourceEntity, destination=destinationEntity)

    def test_quotation_ping_will_pass(self):
        """
        the unit to test ping the server entity
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('quotation:Server-Ping')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_quotation_list_validate_content_that_will_pass(self):
        """
        the unit to test the function of listing all quotation entities
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('quotation:Quotation Entities List from Database')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_quotation_list_will_pass(self):
        """
        the test to test the function of listing all quotation entities and validate its content
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('quotation:Quotation Entities List from Database')
        response = self.client.get(url)
        self.assertEqual(response.json(),
                         [{'quotaion_id': '2982513', 'external_id': '154730507385', 'mode': 'SOURCE_AMOUNT',
                           'source': {'id': 1, 'country_iso_code': 'SDP', 'currency': 'SGD', 'amount': 100},
                           'destination': {'id': 1, 'currency': 'GHS', 'amount': 100}}])
        self.assertEqual(response.status_code, 200)

    def test_quotation_detail_will_pass(self):
        """
        the unit to test the function of getting the quotation entity and validate its content
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('quotation:Quotation Entities from Database', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'quotaion_id': '2982513', 'external_id': '154730507385',
                                           'mode': 'SOURCE_AMOUNT',
                                           'source': {
                                               'id': 1, 'country_iso_code': 'SDP', 'currency': 'SGD', 'amount': 100},
                                           'destination': {'id': 1, 'currency': 'GHS', 'amount': 100}})

    def test_quotation_detail_withoutpk_that_will_fail(self):
        """
        the unit to test the function of getting the quotaton entity
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        try:
            url = reverse('quotation:Quotation Entities from Database')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {'quotaion_id': '2982513', 'external_id': '154730507385',
                                               'mode': 'SOURCE_AMOUNT',
                                               'source': {
                                                'id': 1, 'country_iso_code': 'SDP', 'currency': 'SGD', 'amount': 100},
                                               'destination': {'id': 1, 'currency': 'GHS', 'amount': 100}})
        except Exception as e:
            print("reason: ", e)

    def test_quotation_detail_will_pass(self):
        """
        the unit to test the function of getting the quotation entity
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('quotation:quotation-detail', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

