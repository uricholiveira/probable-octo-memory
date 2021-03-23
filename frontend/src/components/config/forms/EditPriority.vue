<template>
  <q-card style="min-width: 350px">
    <q-card-section>
      <div class="text-h6">Edit priority</div>
    </q-card-section>
    <q-card-section class="q-pt-none">
      <div class="row q-gutter-md">
        <div class="col-12">
          <q-input dense v-model="priorityData.description" autofocus @keyup.enter="update" label="Description"/>
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
  name: "EditPriority",
  props: {
    priority: {
      type: Object,
      default: null
    },
  },
  data() {
    return {
      priorityData: this.priority
    }
  },
  methods: {
    update() {
      this.$axios.patch('priority/',
        null,
        {
          params: {
            priority_id: this.priorityData.id,
            description: this.priorityData.description,
          }
        }
      ).then(response => {
        this.$emit('priority-updated')
      })
    }
  },
  computed: {}
}
</script>

<style scoped>

</style>
