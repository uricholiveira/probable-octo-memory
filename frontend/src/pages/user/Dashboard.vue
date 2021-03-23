<template>
  <q-page>
    <div class="row justify-center" style="margin-top: -1.5rem">
      <h4 style="font-weight: bold">Dashboard</h4>
    </div>
    <div class="row q-gutter-x-md q-pb-lg">
      <div class="col-xs-12 col-sm-3">
        <q-select dense outlined :options="filter.options" v-model="filter.selected"/>
      </div>
      <div class="col-xs-9 col-sm-6">
        <q-input dense outlined type="text" placeholder="Search" v-model="filter.text"/>
      </div>
      <div class="col-xs-1 col-sm-1" style="margin-top: 0.37rem">
        <q-btn color="dark" icon="refresh" @click="getTasks" />
      </div>
    </div>
    <div class="row" style="width: 100%">
      <TaskList :tasks="tasks" :filter="filter" style="width: 100%" @get-tasks="getTasks" v-if="tasks"/>
    </div>
  </q-page>
</template>

<script>
import TaskList from "components/TaskList";
export default {
  name: "Dashboard",
  components: {TaskList},
  data() {
    return {
      tasks: null,
      filter: {
        options: [
          {value: 1, label: 'Task name'},
          {value: 2, label: 'Priority'},
          {value: 3, label: 'Situation'}
        ],
        selected: {value: 1, label: 'Task name'},
        text: ''
      }
    }
  },
  methods: {
    getTasks() {
      this.$axios.get('task/all').then(response => {
        this.tasks = []
        this.tasks = response.data
      })
    }
  },
  mounted() {
    this.getTasks()
  }
}
</script>

<style scoped>
.row {
  margin-top: 0.25rem;
}
</style>
