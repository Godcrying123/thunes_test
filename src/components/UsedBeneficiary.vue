<template>
  <div class="usedbeneficiary">
      <h5>Used Beneficiaries</h5>
        <small>{{ beneList_len }} records showing</small>
      <div>
          <ul v-for="beneficiaryEntity in beneficiaryList" :key="beneficiaryEntity.beneficiary_id" class="list-group list-group-flush">
              <li class="list-group-item d-flex justify-content-between align-items-center">{{ beneficiaryEntity.beneficiary_name }}
                  <span class="badge badge-primary badge-pill">{{ beneficiaryEntity.counter }}</span>
              </li>
            </ul>
      </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'usedbeneficiary',
  props: ['beneficiaryList'],
  data () {
    return {
      beneList_len: 0
    }
  },
  methods: {
    calBeneLength(){
      this.beneList_len = this.beneficiaryList.length
    }
  },
  watch: {
    beneficiaryList: function(newVal, oldVal) {
      this.calBeneLength()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
