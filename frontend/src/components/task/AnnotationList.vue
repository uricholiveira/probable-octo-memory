<template>
<div>
  <div class="row justify-center">
    <div class="col-12 text-center">
      <h5>Annotations</h5>
    </div>
    <div class="col-12 text-center" style="margin-top: -2rem">
      <q-btn size="sm" color="primary" label="New" @click="annotation.new.prompt = true"/>
    </div>
  </div>
  <div class="row">
    <q-list style="width: 100%;">
      <q-item clickable>
        <q-item-section>
          <q-item-label>Single line item</q-item-label>
        </q-item-section>
        <q-item-section side top>
          <q-item-label>
            <q-btn color="negative" icon="delete" @click="annotation.delete.prompt = true"/>
          </q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
  <q-dialog v-model="annotation.new.prompt" persistent>
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">New annotation</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <q-input dense v-model="annotation.new.description" autofocus @keyup.enter="annotation.new.prompt = false"/>
      </q-card-section>

      <q-card-actions align="right" class="text-primary">
        <q-btn flat label="Cancel" v-close-popup/>
        <q-btn flat label="Add annotation" v-close-popup/>
      </q-card-actions>
    </q-card>
  </q-dialog>
  <q-dialog v-model="annotation.delete.prompt" persistent>
    <q-card>
      <q-card-section class="row items-center">
        <q-avatar icon="delete" color="negative" text-color="white"/>
        <span class="q-ml-sm text-weight-bold">Are you sure you want to delete this annotation?</span>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Cancel" color="primary" v-close-popup/>
        <q-btn flat label="Yes" color="primary" v-close-popup/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</div>
</template>

<script>
export default {
  name: "AnnotationList",
  props: {
    annotations: {
      type: Array,
      default: null
    }
  },
  data: () => ({
    annotation: {
      new: {
        prompt: false,
        description: ''
      },
      delete: {
        prompt: false,
      }
    },
  }),
  methods: {
    createAnnotation() {},
    deleteAnnotation() {}
  }
}
</script>

<style scoped>

</style>
