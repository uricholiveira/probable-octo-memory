<template>
  <q-card style="min-width: 350px">
    <q-card-section>
      <div class="text-h6">Edit situation</div>
    </q-card-section>
    <q-card-section class="q-pt-none">
      <div class="row q-gutter-md">
        <div class="col-12">
          <q-input dense v-model="situationData.description" autofocus @keyup.enter="update" label="Description"/>
        </div>
      </div>
    </q-card-section>

    <q-card-actions align="right" class="text-primary">
      <q-btn flat label="Cancel" v-close-popup/>
      <q-btn flat label="Save" @click="update" v-close-popup/>
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  name: "EditSituation",
  props: {
    situation: {
      type: Object,
      default: null
    },
  },
  data() {
    return {
      situationData: this.situation
    }
  },
  methods: {
    update() {
      this.$axios.patch('situation/',
        null,
        {
          params: {
            situation_id: this.situationData.id,
            description: this.situationData.description,
          }
        }
      ).then(response => {
        this.$emit('situation-updated')
      })
    }
  },
  computed: {}
}
</script>

<style scoped>

</style>
