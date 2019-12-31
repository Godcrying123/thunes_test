<template>
  <div class="transaction container">
      <div class="row">
          <div class="col-5">
              <TransactionList @translist="updateTransID($event)" @isShow="isShowEventCheck($event)" :createdTransactionList="createdTransactionList" :confirmedTransactionList="confirmedTransactionList" ></TransactionList>
          </div>
          <div class="col-7">
              <form>
                <TransactionDetail :senderEntity="senderEntity" :beneficiaryEntity="beneficiaryEntity"></TransactionDetail>
                <br><hr><br>
                <div v-if="isShow">
                  <input type="button" @click="confirmTransaction" class="btn btn-primary" value="Confirm the transaction" />
                </div>
              </form>
          </div>
      </div>
  </div>
</template>

<script>
/* eslint-disable */
import TransactionList from '../components/TransactionList'
import TransactionDetail from '../components/TransactionDetail'
import Sender from '../components/Sender'
import Beneficiary from '../components/Beneficiary'
import Additional from '../components/Additional'
import { async } from 'q'
export default {
  name: 'transaction',
  components: {
    TransactionList,
    TransactionDetail,
    Sender,
    Beneficiary,
    Additional
  },
  data () {
    return {
      baseURL: '',
      // baseURL: 'http://django-web:8877',
      // baseURL: 'http://localhost:8000',
      createdTransactionListAPI: '/api/v1/transactions?status=CREATED',
      confirmedTransactionListAPI: '/api/v1/transactions?status=CONFIRMED',
      detailTransactionAPI:"/api/v1/transactions/detail/",
      pingStatusAPI: '/api/v1/quotation/ping',
      senderGetAPI: '/api/v1/senders/',
      beneficiaryGetAPI: '/api/v1/beneficiaries/',
      confirmTransactionAPI: '/api/v1/transactions/confirm/',
      senderEntity: {},
      additionalEntity: {},
      beneficiaryEntity: {},
      quotationEntity: {},
      createdTransactionList: [],
      confirmedTransactionList: [],
      quotation_id: '',
      transactionDetail_id: '',
      external_id: '',
      sender_id: '',
      beneficiary_id: '',
      boolValue: '',
      isShow: 'false',
    }
  },
  methods: {
    // the function for listing all created transaction list
    async createdTransactionListGet(){
      await this.$axios.get(this.baseURL + this.createdTransactionListAPI).then((response) =>{
        this.createdTransactionList = response.data
      }).catch((function (error){
        console.log(error)
      }))
    },
    // the function for listing all confirmed transaction list
    async confirmedTransactionListGet(){
      await this.$axios.get(this.baseURL + this.confirmedTransactionListAPI).then((response) =>{
        this.confirmedTransactionList = response.data
      }).catch((function (error){
        console.log(error)
      }))
    },
    // the function for listing the transaction details
    async transactionDetailReview(){
      await this.$axios.get(this.baseURL + this.detailTransactionAPI + this.transactionDetail_id).then((response) => {
        this.sender_id = response.data.sender
        this.beneficiary_id = response.data.beneficiary
      }).catch((function (error){
        console.log(error)
      }))
    },
    // the function for confirming the created transaction
    confirmTransaction:async function(){
      await this.$axios.post(this.baseURL + this.confirmTransactionAPI + this.transactionDetail_id).then((response)=>{
        if (response.data.errors == undefined) {
          alert(`-----The transaction ${this.transactionDetail_id} has been confirmed------`)
          console.log(response.data)
          this.$router.go(0)
        } else {
          alert(`-----The transaction ${this.transactionDetail_id} cannot be confirmed with below errors------ (${response.data.errors[0].message})`)
        }
        this.transactionDetail_id = ""
      }).catch((function(error){
        console.log(error)
      }))
    },
    // the function to get the sender information
    senderGet(){
      this.$axios.get(this.baseURL + this.senderGetAPI + this.sender_id).then((response)=>{
        this.senderEntity = response.data
      }).catch((function(error){
        console.log(error)
      }))
    },
    // the function to get the beneficiary information
    beneficiaryGet(){
      this.$axios.get(this.baseURL + this.beneficiaryGetAPI + this.beneficiary_id).then((response)=>{
        this.beneficiaryEntity = response.data
      }).catch((function(error){
        console.log(error)
      }))
    },
    // the function for getting the selected transaction id
    updateTransID: async function(id){
      this.transactionDetail_id = id
      await this.transactionDetailReview()
      await this.senderGet()
      await this.beneficiaryGet()
    },
    // the function for controlling the make the transaction show or not
    isShowEventCheck: function(boolValue){
      this.isShow = boolValue
      return this.isShow
    }
  },
  // the function to trigger the created and confirmed transaction list
  beforeMount: async function(){
    await this.createdTransactionListGet()
    await this.confirmedTransactionListGet()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
