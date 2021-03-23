<template>
  <div>
    <div class="row">
      <div class="col-xs-12 col-sm-auto q-gutter-md">
        <q-btn color="primary" label="Save" @click="updateTask"/>
        <q-btn color="negative" label="Cancel" @click="goBack"/>
      </div>
    </div>
    <div class="row justify-between q-gutter-sm">
      <div class="col-xs-12 col-sm-7 col-md-6">
        <q-input outlined type="text" label="Task name" v-model="task.name"/>
      </div>
      <div class="col-xs-12 col-sm-4 col-md-grow">
        <q-input outlined label="Deadline" v-model="task.deadline">
          <template v-slot:prepend>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy transition-show="scale" transition-hide="scale">
                <q-date mask="YYYY-MM-DD HH:mm" v-model="task.deadline">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat/>
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </div>
    </div>
    <div class="row justify-between q-gutter-sm">
      <div class="col-xs-12 col-sm-grow">
        <q-select outlined :options="category.options" v-model="category.selected" label="Category"/>
      </div>
      <div class="col-xs-12 col-sm-grow">
        <q-select outlined :options="situation.options" v-model="situation.selected" label="Situation"/>
      </div>
      <div class="col-xs-12 col-sm-grow">
        <q-select outlined :options="priority.options" v-model="priority.selected" label="Priority"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TaskForm",
  props: {},
  data: () => ({
    task: null,
    category: {
      options: [],
      selected: null
    },
    priority: {
      options: [],
      selected: null
    },
    situation: {
      options: [],
      selected: null
    },
  }),
  methods: {
    getTask() {
      this.$axios.get('task', {params: {task_id: this.$route.params.id}}).then(response => {
        this.task = response.data
      })
    },
    getCategories() {
      this.$axios.get('category/all').then(response => {
        this.category.options = []
        response.data.forEach(category => {
          this.category.options.push({value: category.id, label: category.name})
          if (this.task.category.id === category.id) {
            this.category.selected = {value: category.id, label: category.name}
          }
        })
      })
    },
    getAllPriorities() {
      this.$axios.get('priority/all').then(response => {
        this.priority.options = []
        response.data.forEach(priority => {
          this.priority.options.push({value: priority.id, label: priority.description})
          if (this.task.priority.id === priority.id) {
            this.priority.selected = {value: priority.id, label: priority.description}
          }
        })
      })
    },
    getSituations() {
      this.$axios.get('/situation/all').then(response => {
        this.situation.options = []
        response.data.forEach(situation => {
          this.situation.options.push({value: situation.id, label: situation.description})
          if (this.task.situation.id === situation.id) {
            this.situation.selected = {value: situation.id, label: situation.description}
          }
        })
      })
    },
    updateTask() {
      this.$axios.patch('task', null, {
        params: {
          task_id: this.task.id,
          name: this.task.name,
          user_owner_id: this.task.user_owner_id,
          deadline: this.task.deadline,
          situation_id: this.situation.selected.value,
          priority_id: this.priority.selected.value,
          category_id: this.category.selected.value,
        }
      }).then(response => {
        this.getTask()
        this.$router.back()
      })
    },
    goBack() {
      this.$emit('get-tasks')
      this.$router.push({name: 'Dashboard'})
    }
  },
  mounted() {
    this.getTask()
    setTimeout(() => {
      this.getCategories()
      this.getAllPriorities()
      this.getSituations()
    }, 400)
  }
}
</script>

<style scoped>

.row {
  margin-top: 0.5rem;
}
</style>
