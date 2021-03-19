<template>
<div>
  <div class="row">
    <div class="col-xs-12 col-sm-auto q-gutter-md">
      <q-btn color="primary" label="Save"/>
      <q-btn color="negative" label="Cancel"/>
    </div>
  </div>
  <div class="row justify-between q-gutter-sm">
    <div class="col-xs-12 col-sm-7 col-md-6">
      <q-input outlined type="text" label="Task name"/>
    </div>
    <div class="col-xs-12 col-sm-4 col-md-grow">
      <q-input outlined label="Deadline">
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy transition-show="scale" transition-hide="scale">
              <q-date mask="YYYY-MM-DD HH:mm">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat/>
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
        <template v-slot:append>
          <q-icon name="access_time" class="cursor-pointer">
            <q-popup-proxy transition-show="scale" transition-hide="scale">
              <q-time mask="YYYY-MM-DD HH:mm" format24h>
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat/>
                </div>
              </q-time>
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
  props: {
    taskId: {
      type: Number,
      default: null
    }
  },
  data: () => ({
    task: null,
    situation: {
      options: [],
      selected: {value: 1, label: 'Parado'}
    },
    priority: {
      options: [],
      selected: {value: 1, label: 'Normal'}
    },
    category: {
      options: [],
      selected: {value: 1, label: 'Desenvolvimento'}
    }
  }),
  methods: {
    getTask() {},
    updateTask() {},
  }
}
</script>

<style scoped>

.row {
  margin-top: 0.5rem;
}
</style>
