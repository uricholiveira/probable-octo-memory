<template>
  <q-page>


    <div class="row q-gutter-x-md q-pb-lg">
      <div class="col-3">
        <q-select dense outlined :options="filter.options" v-model="filter.selected"/>
      </div>
      <div class="col">
        <q-input dense outlined type="text" placeholder="Search" v-model="filter.text"/>
      </div>
    </div>
    <div class="row" style="width: 100%">
      <TaskList style="width: 100%"/>
    </div>
  </q-page>
</template>

<script>
import TaskList from "components/TaskList";
export default {
  name: "Dashboard",
  components: {TaskList},
  data: () => ({
    filter: {
      options: [
        {value: 1, label: 'Task name'},
        {value: 2, label: 'Category'},
        {value: 3, label: 'Due date'}
      ],
      selected: {value: 1, label: 'Task name'},
      text: ''
    }
  }),
}
</script>

<style scoped>
.row {
  margin-top: 0.25rem;
}
</style>
