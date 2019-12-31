<template>
  <div class="transactionlist container">
      <h5>All Transaction List</h5>
      <div>
      <br><hr><br>
      <h5>Created Transaction List</h5><br>
      <div class="list-group" v-for="createdTransaction in createdTransactionListChild" :key="createdTransaction.id">
            <a href="#" class="list-group-item list-group-item-action" @click="chooseTransaction(createdTransaction.id, true)">
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Quotation: {{ createdTransaction.quotation_id.quotation_id }} </h5>
                <small>external ID: {{ createdTransaction.external_id }}</small>
                </div>
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Sender => Beneficiary </h5>
                <small>{{ createdTransaction.creation_date }}</small>
                </div>
                <p class="mb-1"></p>
                <small>Amount: {{ createdTransaction.quotation_id.source_id.amount }}</small>
                <small>Currency: {{ createdTransaction.quotation_id.source_id.currency }}</small>
                <small> ==>> </small>
                <small>{{ createdTransaction.quotation_id.destination_id.currency }}</small>
            </a>
        </div>
      </div>
      <div>
      <br><hr><br>
      <h5>Confirmed Transaction List</h5><br>
      <div class="list-group" v-for="confirmedTransaction in confirmedTransactionListChild" :key="confirmedTransaction.id">
            <a href="#" class="list-group-item list-group-item-action" @click="chooseTransaction(confirmedTransaction.id, false)">
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Quotation: {{ confirmedTransaction.quotation_id.quotation_id }} </h5>
                <small>external ID: {{ confirmedTransaction.external_id }}</small>
                </div>
                <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Sender => Beneficiary </h5>
                <small>{{ confirmedTransaction.creation_date }}</small>
                </div>
                <p class="mb-1"></p>
                <small>Amount: {{ confirmedTransaction.quotation_id.source_id.amount }}</small>
                <small>Currency: {{ confirmedTransaction.quotation_id.source_id.currency }}</small>
                <small> ==>> </small>
                <small>{{ confirmedTransaction.quotation_id.destination_id.currency }}</small>
            </a>
        </div>
      </div>
  </div>
</template>
<script>
/* eslint-disable */
// eslint-disable-next-line
export default {
  name: 'transactionlist',
  props: ["createdTransactionList", "confirmedTransactionList"],
  data () {
    return {
      createdTransactionListChild: [],
      confirmedTransactionListChild: [],
      TransactionId: '',
      isShow: '',
    }
  },
  methods: {
    chooseTransaction(id, boolValue){
      this.TransactionId = id
      this.isShow = boolValue
      this.$emit('translist', this.TransactionId)
      this.$emit('isShow', this.isShow)
    },
    // the function to build the relationship with the created and confirmed transaction list
    updateProps(){
      this.createdTransactionListChild = this.createdTransactionList
      this.confirmedTransactionListChild = this.confirmedTransactionList
    } 
  },
  watch: {
    createdTransactionList:function(){
      this.updateProps()
    },
    confirmedTransactionList: function(){
      this.updateProps()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
