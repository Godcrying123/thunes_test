<template>
    <div class="sender">
        <ValidationObserver v-slot="{ handleSubmit }" >
            <form @submit.prevent="handleSubmit()">
            <div class="form-row">
            <div class="form-group col-md-4">
                <h5>Sender Detail Input</h5>
            </div>
            <div class="form-group col-md-4">
                <input type="submit" class="btn btn-primary" value="Check Sender Format"/>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-6">
                <label for="inputLastName4">Last Name</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputLastName4" v-model="SenderObject.lastname" placeholder="Please Input Your Last Name">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-6">
                <label for="inputFirstName4">First Name</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" v-model="SenderObject.firstname" id="inputFirstName4" placeholder="Please Input Your First Name">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
        <div class="form-group">
            <label for="inputEmail">Email</label>
                <ValidationProvider rules="required|email" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputEmail" v-model="SenderObject.email" placeholder="Please Input Your Email">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
        </div>
        <div class="form-row">
            <div class="form-group col-md-4">
                <label for="inputGender">Gender</label>
                <select id="inputGender" v-model="SenderObject.gender" class="form-control">
                    <option selected>Male</option>
                    <option>Female</option>
                </select>
            </div>
            <div class="form-group col-md-4">
                <label for="inputBirth">Your Birthday</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <DatePicker type="date" @on-change="SenderObject.date_of_birth=$event" :value="SenderObject.date_of_birth" format="yyyy-MM-dd" id="inputBirth" placeholder="Please Input Your BirthDay"></DatePicker>
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-4">
                <label for="inputBirthISOCode">Country of Birth ISO Code</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputBirthISOCode" v-model="SenderObject.country_of_birth_iso_code" placeholder="Please Input Your Country of Birth ISO Code">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-3">
                <label for="inputCity">City</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputCity" v-model="SenderObject.city" placeholder="Please Input Your City">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-3">
                <label for="inputCountryISOCode">Country ISO Code</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" v-model="SenderObject.country_iso_code" id="inputCountryISOCode" placeholder="Please Input Your Country ISO Code">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-6">
            <label for="inputAddress">Address</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputAddress" v-model="SenderObject.address" placeholder="Please Input Your Detail Address">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-3">
                <label for="inputZip">Postal Code</label>
                    <ValidationProvider rules="required" v-slot="{ errors }">
                        <input type="text" class="form-control" id="inputZip" v-model="SenderObject.postal_code" placeholder="Please Input Your City Postal Code">
                        <span>{{ errors[0] }}</span>
                    </ValidationProvider>
            </div>
            <div class="form-group col-md-3">
                <label for="inputIDType">ID Type</label>
                <select id="inputIDType" v-model="SenderObject.id_type" class="form-control">
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
                <label for="inputIDNum">ID Number</label>
                <ValidationProvider rules="required|digits:10" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputIDNum" v-model="SenderObject.id_number" placeholder="Please Input Your ID Number">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-md-4">
                <label for="inputIDDeliveryDate">ID Delivery Date</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <DatePicker type="date" @on-change="SenderObject.id_delivery_date=$event" :value="SenderObject.id_delivery_date" format="yyyy-MM-dd" id="inputIDDeliveryDate" placeholder="Please Input Your ID Delivery Date"></DatePicker>
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-4">
                <label for="inputOccupation">Occupation</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputOccupation" v-model="SenderObject.occupation" placeholder="Please Input Your Occupation">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
            <div class="form-group col-md-4">
                <label for="inputMSISDN">msisdn</label>
                <ValidationProvider rules="required" v-slot="{ errors }">
                    <input type="text" class="form-control" id="inputMSISDN" v-model="SenderObject.msisdn" placeholder="Please Input Your MSI SDN">
                    <span>{{ errors[0] }}</span>
                </ValidationProvider>
            </div>
        </div>
                <!-- <button type="submit" class="btn btn-primary">Sign in</button> -->
            </form>
        </ValidationObserver>
    </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'sender',
  data () {
    return {
        SenderObject: {
            lastname: 'Doe',
            firstname: 'Joe',
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
            occupation: 'Support'
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
