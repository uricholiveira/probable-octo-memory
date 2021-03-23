<template>
  <q-page>
    <div class="row justify-center" style="margin-top: -1.5rem">
      <h4 style="font-weight: bold">Editing task</h4>
    </div>
    <div class=" q-pa-lg q-card--bordered">
      <TaskForm />
      <hr class="q-mt-lg" width="70%">
      <AnnotationList />
    </div>
  </q-page>
</template>

<script>
import TaskForm from "components/task/forms/TaskForm";
import AnnotationList from "components/task/lists/AnnotationList";
export default {
  name: "Edit",
  components: {AnnotationList, TaskForm},
  props: {},
  data: () => ({}),
  methods: {
  }
}
</script>

<style scoped>
.row {
  margin-top: 1rem;
}
</style>
