<template>
  <q-card style="min-width: 350px">
    <q-card-section>
      <div class="text-h6">Edit priority</div>
    </q-card-section>
    <q-card-section class="q-pt-none">
      <div class="row q-gutter-md">
        <div class="col-12">
          <q-input dense v-model="categoryData.name" autofocus @keyup.enter="update" label="Name"/>
        </div>
        <div class="col-12">
          <q-select dense :options="priorityData.options" v-model="priorityData.value"
                    label="Priority"/>
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
  name: "EditCategory",
  props: {
    category: {
      type: Object,
      default: null
    },
    priority: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      categoryData: this.category,
      priorityData: this.priority
    }
  },
  methods: {
    update() {
      this.$axios.patch('/category',
        null,
        {
          params: {
            category_id: this.categoryData.id,
            name: this.categoryData.name.toString(),
            priority_id: this.priorityData.value.value
          }
        }
      ).then(response => {
        this.$emit('category-updated')
      })
    }
  },
  computed: {}
}
</script>

<style scoped>

</style>
