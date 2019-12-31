<template>
  <div class="beneficiary">
    <ValidationObserver v-slot="{ handleSubmit }">
        <form @submit.prevent="handleSubmit()">
        <div class="form-row">
            <div class="form-group col-md-4">
                <h5>Beneficiary Detail Input</h5>
            </div>
            <div class="form-group col-md-4">
                <input type="submit" class="btn btn-primary" value="Check Beneficiary Format"/>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-6">
            <label for="inputLastName4B">Last Name</label>
            <ValidationProvider rules="required" v-slot="{ errors }">
                <input type="text" class="form-control" id="inputLastName4B" v-model="BeneficiaryObject.lastname" placeholder="Please Input Your Last Name">
                <span>{{ errors[0] }}</span>
            </ValidationProvider>
            </div>
            <div class="form-group col-md-6">
            <label for="inputFirstName4B">First Name</label>
            <ValidationProvider rules="required" v-slot="{ errors }">
                <input type="text" class="form-control" id="inputFirstName4B" v-model="BeneficiaryObject.firstname" placeholder="Please Input Your First Name">
                <span>{{ errors[0] }}</span>
            </ValidationProvider>
            </div>
        </div>
        <div class="form-group">
            <label for="inputEmailB">Email</label>
            <ValidationProvider rules="required|email" v-slot="{ errors }">
                <input type="text" class="form-control" v-model="BeneficiaryObject.email" id="inputEmailB" placeholder="Please Input Your Email">
                 <span>{{ errors[0] }}</span>
            </ValidationProvider>
        </div>
        <div class="form-row">
            <div class="form-group col-md-4">
                <label for="inputGenderB">Gender</label>
                <select id="inputGenderB" v-model="BeneficiaryObject.gender" class="form-control">
                    <option>Male</option>
                    <option>Female</option>
                </select>
            </div>
            <div class="form-group col-md-4">
                <label for="inputBirthB">Your Birthday</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <DatePicker type="date" id="inputBirthB" @on-change="BeneficiaryObject.date_of_birth=$event" :value="BeneficiaryObject.date_of_birth" placeholder="Please Input Your BirthDay"></DatePicker>
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-4">
                <label for="inputBirthISOCodeB">Country of Birth ISO Code</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" v-model="BeneficiaryObject.country_of_birth_iso_code" id="inputBirthISOCodeB" placeholder="Please Input Your Country of Birth ISO Code">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-3">
            <label for="inputCityB">City</label>
            <ValidationProvider rules="required" v-slot="{ errors }">
                <input type="text" class="form-control" v-model="BeneficiaryObject.city" id="inputCityB" placeholder="Please Input Your City">
                <span>{{ errors[0] }}</span>
            </ValidationProvider>
            </div>
            <div class="form-group col-md-3">
            <label for="inputCountryISOCodeB">Country ISO Code</label>
            <ValidationProvider rules="required" v-slot="{ errors }">
                <input type="text" class="form-control" v-model="BeneficiaryObject.country_iso_code" id="inputCountryISOCodeB" placeholder="Please Input Your Country ISO Code">
                <span>{{ errors[0] }}</span>
            </ValidationProvider>
            </div>
            <div class="form-group col-md-6">
            <label for="inputAddressB">Address</label>
            <ValidationProvider rules="required" v-slot="{ errors }">
                <input type="text" class="form-control" v-model="BeneficiaryObject.address" id="inputAddressB" placeholder="Please Input Your Detail Address">
                <span>{{ errors[0] }}</span>
            </ValidationProvider>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-3">
                <label for="inputZipB">Postal Code</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" v-model="BeneficiaryObject.postal_code" id="inputZipB" placeholder="Please Input Your City Postal Code">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-3">
                <label for="inputIDTypeB">ID Type</label>
                <select id="inputIDTypeB" v-model="BeneficiaryObject.id_type" class="form-control">
                    <option selected value="PASSPORT">Passport</option>
                    <option>National Identification Card</option>
                    <option>Driving License</option>
                    <option>Social Security Card/Number</option>
                    <option>Tax Payer Identification Card/Number</option>
                    <option>Senior Citizen Identification Card</option>
                    <option>Birth Certificate</option>
                    <option>Village Elder Identification Card</option>
                    <option>Permanent Residency Identification Card</option>
                    <option>Alien Registration Certificate/Card</option>
                    <option>PAN Card</option>
                    <option>Voter’s Identification Card</option>
                    <option>Health Insurance Card/Number</option>
                    <option>Identification Card</option>
                    <option>Others not listed</option>
                </select>
            </div>
            <div class="form-group col-md-6">
                <label for="inputIDNumB">ID Number</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" v-model="BeneficiaryObject.id_number" id="inputIDNumB" placeholder="Please Input Your ID Number">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-4">
                <label for="inputIDDeliveryDateB">ID Delivery Date</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <DatePicker type="date" id="inputIDDeliveryDateB" @on-change="BeneficiaryObject.id_delivery_date=$event" :value="BeneficiaryObject.id_delivery_date" placeholder="Please Input Your ID Delivery Date"></DatePicker>
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-4">
                <label for="inputOccupationB">Occupation</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" v-model="BeneficiaryObject.occupation" id="inputOccupationB" placeholder="Please Input Your Occupation">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-4">
                <label for="inputMSISDNB">msisdn</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" v-model="BeneficiaryObject.msisdn" id="inputMSISDNB" placeholder="Please Input Your MSI SDN">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
    </form>
    </ValidationObserver>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'beneficiary',
  data () {
    return {
        BeneficiaryObject: {
            lastname: 'Doe',
            firstname: 'Jane',
            nationality_country_iso_code: 'FRA',
            date_of_birth: '1970-07-01',
            country_of_birth_iso_code: 'FRA',
            gender: 'Male',
            address: '42 Rue des fleurs',
            postal_code: '75000',
            city: 'Paris',
            country_iso_code: 'FRA',
            msisdn: '1123131413',
            email: 'kzhang@microfocus.com',
            id_type: 'PASSPORT',
            id_number: '1123131413',
            id_delivery_date: '2019-12-18',
            occupation: 'Teacher'
        }
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
