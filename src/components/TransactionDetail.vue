<template>
  <div class="transactiondetail container">
      <h5>Transaction Detail Page</h5>
    <br><hr><br>
    <!-- <div class="row">
      <div class="col-6">
        <table class="table table-borderless">
          <thead>
            <th colspan="2">Transaction Info</th>
          </thead>
          <tbody>
            <tr>
              <td>lastname</td>
              <td>Doe</td>
            </tr>
            <tr>
              <td>firstname</td>
              <td>John</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div> -->
    <div class="row">
      <div class="col-6">
        <table class="table table-borderless">
          <thead>
            <th colspan="2">Sender Info</th>
          </thead>
          <tbody>
            <tr>
              <td>lastname</td>
              <td>{{ senderEntity.lastname }}</td>
            </tr>
            <tr>
              <td>firstname</td>
              <td>{{ senderEntity.firstname }}</td>
            </tr>
            <tr>
               <td>gender</td>
               <td>{{ senderEntity.gender }}</td>
            </tr>
            <tr>
              <td>occupation</td>
              <td>{{ senderEntity.occupation }}</td>
            </tr>
             <tr>
               <td>birthday</td>
               <td>{{ senderEntity.date_of_birth }}</td>
            </tr>
            <tr>
               <td>city</td>
               <td>{{ senderEntity.city }}</td>
            </tr>
            <tr>
               <td>address</td>
               <td>{{ senderEntity.address }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-6">
        <table class="table table-borderless">
          <thead>
            <th colspan="2">Beneficiary Info</th>
          </thead>
          <tbody>
            <tr>
              <td>lastname</td>
              <td>{{ beneficiaryEntity.lastname }}</td>
            </tr>
            <tr>
              <td>firstname</td>
              <td>{{ beneficiaryEntity.firstname }}</td>
            </tr>
            <tr>
               <td>gender</td>
               <td>{{ beneficiaryEntity.gender }}</td>
            </tr>
            <tr>
              <td>occupation</td>
              <td>{{ beneficiaryEntity.occupation }}</td>
            </tr>
             <tr>
               <td>birthday</td>
               <td>{{ beneficiaryEntity.date_of_birth }}</td>
            </tr>
            <tr>
               <td>city</td>
               <td>{{ beneficiaryEntity.city }}</td>
            </tr>
            <tr>
               <td>address</td>
               <td>{{ beneficiaryEntity.address }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
// eslint-disable-next-line
export default {
  name: 'transactiondetail',
  props: ['senderEntity', 'beneficiaryEntity'],
  data () {
    return {
    }
  },
  methods: {
  },
  watch: {
    senderEntity: function(){

    },
    beneficiaryEntity: function(){
      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
