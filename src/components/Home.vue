<template>
  <ValidationObserver v-slot="{ handleSubmit }">
    <form @submit.prevent="handleSubmit(formSubmit)">
    <div class="home container">
      <div class="row">
          <div class="col-8">
              <Sender ref="sender"></Sender>
          </div>
          <div class="col-4">
              <UsedBeneficiary :beneficiaryList="beneficiaryList" ></UsedBeneficiary>
          </div>
      </div>
      <hr><br>
      <div class="row">
          <div class="col-8">
              <Additional ref="additional" :external_id="external_id" ></Additional>
          </div>
      </div>
      <hr><br>
      <div class="row">
          <div class="col-8">
            <Beneficiary ref="beneficiary"></Beneficiary>
          </div>
      </div>
      <div class="row">
        <div class="col-8">
          <button type="submit" class="btn btn-primary">Make a transaction</button>
        </div>
      </div>
      <br><hr><br>
    </div>
  </form>
  </ValidationObserver>
</template>

<script>
/* eslint-disable */
import UsedBeneficiary from '../components/UsedBeneficiary'
import Sender from '../components/Sender'
import Beneficiary from '../components/Beneficiary'
import Additional from '../components/Additional'
import { async } from 'q'
export default {
  name: 'home',
  components: {
    Sender,
    UsedBeneficiary,
    Beneficiary,
    Additional
  },
  data () {
    return {
      // baseURL: '',
      baseURL: 'http://localhost:8000',
      quotationCreateAPI:'/api/v1/quotation/create',
      quotationGetAPI:'/api/v1/quotation/',
      transactionCreateAPI: '/api/v1/transactions/',
      transactionGetAPI: '/api/v1/transactons/detail/',
      transactionConfirmAPI: '/api/v1/transactions/confirm/',
      beneficiaryListGetAPI: '/api/v1/transactions/sender?',
      pingStatusAPI: '/api/v1/quotation/ping',
      quotationData: {},
      transactionData: {},
      senderEntity: {},
      additionalEntity: {},
      beneficiaryEntity: {},
      quotationEntity: {},
      credit_party_identifier: {},
      quotation_id: '',
      transaction_id: '',
      external_id: '',
      beneficiaryList: [],
      senderLastName: String,
      senderFirstName: String
    }
  },
  methods: {
    // the function for submit the form
    async formSubmit() {
      await this.quotationCreate()
      await alert("Please wait transaction to finish its creation")
      await this.transactionCreate()
      // await this.transactionConfirm()
    },
    // the function for handling different errors
    errorHandle: function() {
    },
    // the function for handling different notifications
    notificationHandle: function() {
    },
    // the function for getting the service status
    serviceGet(){
      this.$axios.get(this.baseURL + this.pingStatusAPI).then((response) => {
        console.log("The Backend API Service Status Check Result: " + response.data.status)
      }).catch((function (error){
        console.log(error)
      }))
    },
    // the function for getting the quotation detail
    quotationGet(){
       this.$axios.get(this.baseURL + this.quotationGetAPI + this.quotation_id).then((response) => {
         this.quotation_id = response.data.id
        //  console.log(this.quotation_id)
         console.log(response.data)
        }).catch((function (error) {
          console.log(error);
          }))
    },
    // the function for creating the quotation entity
    async quotationCreate() {
      // console.log(JSON.stringify(this.quotationEntity))
      await this.$axios.post(this.baseURL + this.quotationCreateAPI, JSON.stringify(this.quotationEntity)).then(response => {
        // console.log(JSON.stringify(this.quotationEntity))
        console.log(response.data)
        this.quotation_id = response.data.id
        this.external_id = response.data.external_id
        }).catch((function (error){
          console.log(error)
          }))
        alert(`-----The quotation ${this.quotation_id} has been created------`)
    },
    // the function for creating the transaction entity
    async transactionCreate() {
      this.getChildValue()
      this.transactionData.sender = this.senderEntity
      this.transactionData.beneficiary = this.beneficiaryEntity
      this.credit_party_identifier.bank_account_number = this.additionalEntity.bank_account_number
      this.credit_party_identifier.msisdn = this.additionalEntity.msisdn
      this.credit_party_identifier.swift_bic_code = this.additionalEntity.swift_bic_code
      this.transactionData.credit_party_identifier = this.credit_party_identifier
      this.transactionData.external_id = this.external_id
      this.transactionData.retail_fee = this.additionalEntity.retail_fee
      this.transactionData.retail_fee_currency = this.additionalEntity.retail_fee_currency
      this.transactionData.purpose_of_remittance = this.additionalEntity.purpose_of_remittance
      this.transactionData.callback_url = null
      // console.log(JSON.stringify(this.transactionData))
      await this.$axios.post(this.baseURL + this.transactionCreateAPI + this.quotation_id, this.transactionData).then(response => {
        console.log(response.data)
        this.transaction_id = response.data.id
      }).catch((function (error){
        console.log(error)
      }))
      alert(`-----The transaction ${this.transaction_id} has been created------`)
    },
    // the function for getting the transaction detail
    transactionGet: function() {
      this.$axios.get(this.baseURL + this.transactionGetAPI + this.transaction_id).then(response => {
        console.log(response.data)
      }).catch((function (error){
        console.log(error)
      }))
    },
    // the function for confirming the transaction entity
    async transactionConfirm() {
      await this.$axios.post(this.baseURL + this.transactionConfirmAPI + this.transaction_id, ).then(response => {
        console.log(response.data)
      }).catch((function (error){
        console.log(error)
      }))
    },
    // the function for listing all beneficiary list by its sender lastname and firstname
    beneficiaryListGet: function(){
      // this.getChildValue()
      if (this.senderEntity.lastname != '' && this.senderEntity.firstname != ''){
        this.beneficiaryListGetAPI = this.beneficiaryListGetAPI + "firstname=" + this.senderEntity.firstname + "&" + "lastname=" + this.senderEntity.lastname
      } else if (this.senderEntity.lastname == '') {
        this.beneficiaryListGetAPI  = this.beneficiaryListGetAPI + "firstname=" + this.senderEntity.firstname
      } else if (this.senderEntity.firstname == '') {
        this.beneficiaryListGetAPI = this.beneficiaryListGetAPI + "lastname=" + this.senderEntity.lastname
      }
      // console.log(this.beneficiaryListGetAPI)
      this.$axios.get(this.baseURL + this.beneficiaryListGetAPI).then(response => {
        // console.log(response.data)
        this.beneficiaryList = response.data
      }).catch((function (error){
        console.log(error)
      }))
      this.beneficiaryListGetAPI = '/api/v1/transactions/sender?'
    },
    // the function for getting the sender, beneficiary, additional data from its child vue component
    getChildValue: function(){
      this.senderEntity = this.$refs.sender.SenderObject
      this.beneficiaryEntity = this.$refs.beneficiary.BeneficiaryObject
      this.additionalEntity = this.$refs.additional.AdditionalObject
      this.quotationEntity.source = this.$refs.additional.SourceObject
      this.quotationEntity.destination = this.$refs.additional.DestinationObject
    }
  },
  // montior sender two names value change behaviour
  watch: {
    'senderEntity.lastname': function(){
      if (this.senderEntity.lastname != '' && this.senderEntity.firstname != '' ) {
        this.beneficiaryListGet()
      }
    },
    'senderEntity.firstname': function(){
      if (this.senderEntity.firstname != '' && this.senderEntity.lastname != '' ) {
        this.beneficiaryListGet()
      }
    },
  },
  mounted: function() {
    this.getChildValue()
    this.serviceGet()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
