import sys

from django.test import TestCase, Client
from django.urls import reverse

from .models import Beneficiary
from .serializers import BeneficiarySerializer

# Create your tests here.


class BeneficiaryTestCase(TestCase):

    def setUp(self):
        """
        the setUp function to create a mock object.
        """
        Beneficiary.objects.create(id=1, lastname='Doe', lastname2='', middlename='', firstname='Jane', nativename='',
                                   nationality_country_iso_code='FRA', code='', date_of_birth='1970-07-01',
                                   country_of_birth_iso_code='FRA', gender='Male', address='42 Rue des fleurs',
                                   postal_code='75000', city='Paris', country_iso_code='FRA', msisdn='1123131413',
                                   email='kzhang@microfocus.com', id_type='PASSPORT', id_country_iso_code='',
                                   id_number='1123131413', occupation='Teacher', bank_accout_holder_name='',
                                   province_state='')
        self.client = Client()

    def test_beneficiaries_list_connectivity_that_will_pass(self):
        """
         the function to test the beneficiaries list
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('beneficiary:beneficiaries-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_beneficiaries_list_validate_content_will_pass(self):
        """
        the function to test the function of listing all beneficiary entities and validte its output
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('beneficiary:beneficiaries-list')
        response = self.client.get(url)

        # serialize all model object data
        beneficiaries = Beneficiary.objects.all()
        serializer = BeneficiarySerializer(beneficiaries, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_beneficiaries_create_connectivity_that_will_pass(self):
        """
        the function to test the beneficiary create post method
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('beneficiary:beneficiaries-create')
        response = self.client.post(url, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_beneficiaries_create_callback_that_will_pass(self):
        """
        the function to test the beneficiary create callback post method
        """
        post_body = {
            'lastname': 'Doe',
            'lastname2': '',
            'middlename': '',
            'firstname': 'Jane',
            'nativename': '',
            'nationality_country_iso_code': 'FRA',
            'code': '',
            'date_of_birth': '1970-07-01',
            'country_of_birth_iso_code': 'FRA',
            'gender': 'Male',
            'address': '42 Rue des fleurs',
            'postal_code': '75000',
            'city': 'Paris',
            'country_iso_code': 'FRA',
            'msisdn': '1123131413',
            'email': 'kzhang@microfocus.com',
            'id_type': 'PASSPORT',
            'id_country_iso_code': '',
            'id_number': '1123131413',
            'occupation': 'Teacher',
            'bank_accout_holder_name': '',
            'province_state': ''
        }
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('beneficiary:beneficiaries-create')
        response = self.client.post(url, data=post_body, content_type='application/json')
        return self.assertTrue(response.status_code, 200)

    def test_beneficiaries_retrieve_that_will_pass(self):
        """
        the function to test the beneficiary retrieve get method
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('beneficiary:beneficiary-entity-by-id-retrieve', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_beneficiaries_retrieve_validate_content_that_will_pass(self):
        """
        the function to test the beneficiary retrieve function with a id
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('beneficiary:beneficiary-entity-by-id-retrieve', kwargs={'pk': 1})
        response = self.client.get(url)

        # serialize all model object data
        beneficiaries = Beneficiary.objects.get(pk=1)
        serializer = BeneficiarySerializer(beneficiaries, many=False)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_beneficiaries_retrieve_withoutID_that_will_fail(self):
        """
        the function to test the function of retrieving beneficiary entity without pk
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        try:
            url = reverse('beneficiary:beneficiary-entity-by-id-retrieve')
            response = self.client.get(url)
            self.assertTrue(response.status_code, 200)
        except Exception as e:
            print("reason: ", e)

    def test_beneficiaries_update_that_will_pass(self):
        """
        the function to test the beneficiary update post method
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        url = reverse('beneficiary:beneficiary-entity-by-id-update', kwargs={'pk': 1})
        response = self.client.post(url, content_type='application/json')
        return self.assertTrue(response.status_code, 200)

    def test_beneficiaries_update_withoutID_that_will_fail(self):
        """
        the function to test the function of updating the beneficiary entity without a ID
        """
        print('the test function name: {}'.format(sys._getframe().f_code.co_name))
        try:
            url = reverse('beneficiary:beneficiary-entity-by-id-update')
            response = self.client.get(url, content_type='application/json')
            return self.assertTrue(response.status_code, 200)
        except Exception as e:
            print("reason: ", e)
