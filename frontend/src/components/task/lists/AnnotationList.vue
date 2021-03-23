<template>
  <div>
    <div class="row justify-center">
      <div class="col-12 text-center">
        <h5>Annotations</h5>
      </div>
      <div class="col-12 text-center" style="margin-top: -2rem">
        <q-btn size="sm" color="primary" label="New" @click="annotations.newPrompt = true"/>
      </div>
    </div>
    <div class="row">
      <q-list style="width: 100%;">
        <q-item clickable v-for="(annotation, index) in annotations.value" :key="index">
          <q-item-section>
            <q-item-label>{{ annotation.description }}</q-item-label>
          </q-item-section>
          <q-item-section side top>
            <q-item-label>
              <q-btn flat dense color="negative" icon="delete" @click="annotations.deletePrompt = true"/>
            </q-item-label>
          </q-item-section>

          <q-dialog v-model="annotations.newPrompt" persistent @before-hide="getAnnotations">
            <q-card style="min-width: 350px">
              <q-card-section>
                <div class="text-h6">New annotation</div>
              </q-card-section>

              <q-card-section class="q-pt-none">
                <q-input dense v-model="annotations.description" autofocus @keyup.enter="createAnnotation"/>
              </q-card-section>

              <q-card-actions align="right" class="text-primary">
                <q-btn flat label="Cancel" v-close-popup/>
                <q-btn flat label="Add annotation" @click="createAnnotation" v-close-popup/>
              </q-card-actions>
            </q-card>
          </q-dialog>
          <q-dialog v-model="annotations.deletePrompt" persistent @before-hide="getAnnotations">
            <q-card>
              <q-card-section class="row items-center">
                <q-avatar icon="delete" color="negative" text-color="white"/>
                <span class="q-ml-sm text-weight-bold">Are you sure you want to delete this annotation?</span>
              </q-card-section>

              <q-card-actions align="right">
                <q-btn flat label="Cancel" color="primary" v-close-popup/>
                <q-btn flat label="Yes" color="primary" @click="deleteAnnotation(annotation)" v-close-popup/>
              </q-card-actions>
            </q-card>
          </q-dialog>
        </q-item>
        <q-item clickable v-if="annotations.value.length === 0">
          <q-item-section>
            <q-item-label>
              <div class="row justify-center">
                No one annotation had found
              </div>
            </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </div>
</template>

<script>
export default {
  name: "AnnotationList",
  props: {},
  data: () => ({
    annotations: {
      newPrompt: false,
      editPrompt: false,
      deletePrompt: false,
      description: '',
      value: null
    },
  }),
  methods: {
    getAnnotations() {
      this.$axios.get('annotation/task', {
        params: {task_id: this.$route.params.id}
      }).then(response => {
        this.annotations.description = ''
        this.annotations.value = response.data
      })
    },
    createAnnotation() {
      this.$axios.post('annotation', null, {
        params: {description: this.annotations.description, task_id: this.$route.params.id}
      }).then(response => {
        this.annotations.description = ''
        this.annotations.newPrompt = false
        this.getAnnotations()
      })
    },
    deleteAnnotation(annotation) {
      this.$axios.delete('annotation', {params: {
        annotation_id: annotation.id
        }}).then(response => {
        this.annotations.deletePrompt = false
          this.getAnnotations()
      })
    }
  },
  mounted() {
    this.getAnnotations()
  }
}
</script>

<style scoped>

</style>
