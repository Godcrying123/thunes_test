<template>
  <div class="additional">
      <form>
          <div class="form-row">
              <div class="form-group col-md-4">
                   <h5>Additional Information</h5>
              </div>
          </div>
          <br>
          <div class="form-row">
              <div class="form-group col-md-3 ">
                  <h6>Source Info: </h6>
              </div>
              <div class="form-group col-md-3 ">
                <ValidationProvider rules="required|integer" v-slot="{ errors }">
                  <label for="AmountSource">Amount</label>
                  <input type="text" class="form-control" v-model="SourceObject.amount" id="AmountSource" placeholder="Please Input Your Source Amount">
                   <span>{{ errors[0] }}</span>
                </ValidationProvider>
              </div>
              <div class="form-group col-md-3 ">
                  <label for="CurrencySource">Currency</label>
                  <input readonly type="text" class="form-control" v-model="SourceObject.currency" id="CurrencySource" placeholder="Please Input Your Source Currency">
              </div>
              <div class="form-group col-md-3">
                  <label for="CuntryisocodeSource">Country_ISO_CODE</label>
                  <input readonly type="text" class="form-control" v-model="SourceObject.country_iso_code" id="CuntryisocodeSource" placeholder="Please Input Your Country ISO Code">
              </div>
          </div>
          <div class="form-row">
              <div class="form-group col-md-3 ">
                  <h6>Destination Info: </h6>
              </div>
              <div class="form-group col-md-3 ">
                  <label for="AmountDestination">Amount</label>
                  <input readonly type="text" class="form-control" v-model="DestinationObject.amount" id="AmountSource" placeholder="Please Input Your Source Amount">
              </div>
              <div class="form-group col-md-3 ">
                  <label for="CurrencyDestination">Currency</label>
                  <input readonly type="text" class="form-control" v-model="DestinationObject.currency" id="CurrencySource" placeholder="Please Input Your Source Currency">
              </div>
          </div>
          <div class="form-row">
              <div class="form-group col-md-4">
                  <label for="MSISDN">MSISDN</label>
                  <input readonly type="text" class="form-control" v-model="AdditionalObject.msisdn" id="MSISDN" placeholder="Please Input Your MSI SDN">
              </div>
              <div class="form-group col-md-4">
                  <label for="BankAccountNumber">Bank Account Number</label>
                  <input readonly type="text" class="form-control" v-model="AdditionalObject.bank_account_number" id="BankAccountNumber" placeholder="Please Input Your Bank Account Number">
              </div>
              <div class="form-group col-md-4">
                  <label for="SwiftBicCode">Swift Bic Code</label>
                  <input readonly type="text" class="form-control" v-model="AdditionalObject.swift_bic_code" id="SwiftBicCode" placeholder="Please Input Your Swift Bic Code">
              </div>
          </div>
          <div class="form-row">
              <div class="form-group col-md-3">
                  <label for="ExternalID">External ID</label>
                  <input readonly type="text" class="form-control" v-model="external_id" id="ExternalID" placeholder="Your External ID will be generated later" >
              </div>
              <div class="form-group col-md-4">
                  <label for="PurposeOfRemittance">Purpose Of Remittance</label>
                  <input readonly type="text" class="form-control" v-model="AdditionalObject.purpose_of_remittance" id="PurposeOfRemittance" placeholder="Please Input Your Purpose Of Remittance">
              </div>
              <div class="form-group col-md-3">
                  <label for="RetailFeeCurrency">Retail Fee Currency</label>
                  <input readonly type="text" class="form-control" v-model="AdditionalObject.retail_fee_currency" id="RetailFeeCurrency" placeholder="Please Input Your Retail Fee Currency">
              </div>
              <div class="form-group col-md-2">
                  <label for="RetailFee">Retail Fee</label>
                  <input readonly type="text" class="form-control" v-model="AdditionalObject.retail_fee" id="RetailFee" placeholder="Please Input Your Retail Fee">
              </div>
          </div>
      </form>
  </div>
</template>
<script>
/* eslint-disable */
export default {
  name: 'additional',
  props: ['external_id'],
  data () {
    return {
        AdditionalObject: {
            msisdn: '+263775892100',
            bank_account_number: '0123456789',
            swift_bic_code: 'ABCDEFGH',
            external_id: '1478078339357',
            retail_fee: 1,
            retail_fee_currency: 'EUR',
            purpose_of_remittance: 'FAMILY_SUPPORT'
        },
        SourceObject:{
            amount: '',
            country_iso_code: 'SGP',
            currency: 'SGD'
        },
        DestinationObject: {
            amount: null,
            currency: 'GHS'
        }
    }
  },
  watch: {
      external_id: function() {
          this.AdditionalObject.external_id = this.external_id
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
