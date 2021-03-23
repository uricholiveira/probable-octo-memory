<template>
<div>
  <q-list bordered class="rounded-borders">
    <q-expansion-item
      expand-separator
      default-opened
      icon="perm_identity"
      label="Today"
      caption="Activities due today"
      v-if="todayTasks.length > 0"
    >
      <q-card v-for="(task, index) in todayTasks" :key="index">
        <q-card-section>
          <div class="row justify-around q-gutter-sm">
            <div class="col-xs-12 col-sm-10 col-md-6 col-lg-4">
              <q-card>
                <q-card-section class="q-gutter-y-sm" style="min-height: 160px; max-height: 160px">
                  <div class="row justify-start" style="font-weight: bold">
                    <div class="col-8">
                      {{task.name}}
                    </div>
                    <div class="col-4 text-right">
                      <q-badge :label="task.situation.description" color="primary" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col-8">
                      {{task.category.name}}
                    </div>
                    <div class="col-4 text-right">
                      <q-badge :label="task.priority.description" color="positive" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col">
                      <q-badge :label="task.deadline" color="negative" />
                    </div>
                  </div>
                  <hr>
                  <div class="row justify-center">
                    <div class="col q-gutter-md text-center">
                      <q-btn dense padding="8px" unelevated label="Start" size="sm" color="primary" @click="startTask(task)" v-if="task.situation.description != 'Parado'"/>
                      <q-btn dense padding="8px" unelevated label="Pause" size="sm" color="warning" @click="pauseTask(task)" v-if="task.situation.description === 'Iniciado'"/>
                      <q-btn dense padding="8px" unelevated label="Edit" size="sm" color="info" @click="$router.push({name: 'TaskDetail', params: {id: task.id}})"/>
                      <q-btn dense padding="8px" unelevated label="Deliver" size="sm" color="secondary" @click="deliverTask(task)"/>
                    </div>
                  </div>
                </q-card-section>
              </q-card>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>
    <q-expansion-item
      expand-separator
      default-opened
      icon="perm_identity"
      label="Tasks"
      caption="All task list"
    >
      <q-card v-for="(task, index) in filteredTasks" :key="index">
        <q-card-section>
          <div class="row justify-around q-gutter-sm">
            <div class="col-xs-12 col-sm-10 col-md-6 col-lg-4">
              <q-card>
                <q-card-section class="q-gutter-y-sm" style="min-height: 160px; max-height: 160px">
                  <div class="row justify-start" style="font-weight: bold">
                    <div class="col-8">
                      {{task.name}}
                    </div>
                    <div class="col-4 text-right">
                      <q-badge :label="task.situation.description" color="primary" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col-8">
                      {{task.category.name}}
                    </div>
                    <div class="col-4 text-right">
                      <q-badge :label="task.priority.description" color="positive" />
                    </div>
                  </div>
                  <div class="row justify-center">
                    <div class="col">
                      <q-badge :label="task.deadline" color="negative" />
                    </div>
                  </div>
                  <hr>
                  <div class="row justify-center">
                    <div class="col q-gutter-md text-center">
                      <q-btn dense padding="8px" unelevated label="Start" size="sm" color="primary" @click="startTask(task)" v-if="task.situation.description !== 'Iniciado'"/>
                      <q-btn dense padding="8px" unelevated label="Pause" size="sm" color="warning" @click="pauseTask(task)" v-if="task.situation.description === 'Iniciado'"/>
                      <q-btn dense padding="8px" unelevated label="Edit" size="sm" color="info" @click="$router.push({name: 'TaskDetail', params: {id: task.id}})"/>
                      <q-btn dense padding="8px" unelevated label="Deliver" size="sm" color="secondary" @click="deliverTask(task)" v-if="task.situation.description !== 'Concluido'"/>
                    </div>
                  </div>
                </q-card-section>
              </q-card>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>
  </q-list>
</div>
</template>

<script>
import moment from 'moment';
export default {
  name: "TaskList",
  props: {
    tasks: {
      type: Array
    },
    filter: {
      type: Object
    }
  },
  data() {
    return {}
  },
  methods: {
    startTask(task) {
      this.$axios.post('task/start', null, {params: {task_id: task.id}}).then(response => {
        this.$emit('get-tasks')
      })
    },
    pauseTask(task) {
      this.$axios.post('task/pause', null, {params: {task_id: task.id}}).then(response => {
        this.$emit('get-tasks')
      })
    },
    deliverTask(task) {
      this.$axios.post('task/deliver', null, {params: {task_id: task.id}}).then(response => {
        this.$emit('get-tasks')
      })
    },
  },
  computed: {
    filteredTasks() {
      return this.tasks.filter(task => {
        if (this.filter.selected.value === 1) {
          return task.name.toUpperCase().match(
            this.filter.text.toUpperCase()
          )
        } else if (this.filter.selected.value === 2) {
          return task.priority.description.toUpperCase().match(
            this.filter.text.toUpperCase()
          )
        } else if (this.filter.selected.value === 3) {
          return task.situation.description.toUpperCase().match(
            this.filter.text.toUpperCase()
          )
        }
      })
    },
    todayTasks() {
      return this.tasks.filter(task => {
        return moment(task.deadline).format('YYYY-MM-DD') === moment().format('YYYY-MM-DD');
      })
    }
  }
}
</script>

<style scoped>

</style>
