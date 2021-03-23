<template>
  <div class="row">
    <q-table
      class="full-width"
      :dense="$q.screen.lt.md"
      title="Priorities"
      :data="table.data"
      :columns="table.columns"
      row-key="name"
      :pagination="table.pagination"
      :filter="table.filter"
      rows-per-page-label="Data per page"
      no-data-label="No one result has found"
      :loading="table.isLoading"
    >
      <template v-slot:top>
        <div class="row wrap q-gutter-y-sm justify-start full-width">
          <div class="col-xs-8 col-sm-6 col-md-4 col-lg-4 col-xl-4">
            <q-input outlined dense debounce="300" color="primary" v-model="table.filter"
                     class="q-mr-md" placeholder="Search">
              <template v-slot:prepend>
                <q-icon name="search"/>
              </template>
            </q-input>
          </div>
          <div class="col-grow text-left">
            <span class="q-ml-md">
              <q-btn size="md" icon="refresh" :loading="table.isLoading" @click="getPriorities" flat round/>
            </span>
          </div>
          <div class="col-xs-12 col-sm-4 col-md-4 col-lg-2 col-xl-2"
               :class="[$q.screen.xs ? 'text-left' : 'text-right']">
            <span class="">
              <q-btn size="md" label="New priority" :loading="table.isLoading" @click="priority.prompt = true"
                     color="primary"/>
            </span>
          </div>
        </div>

      </template>
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn dense round flat class="text-blue-4" @click="editRow(props.row)"
                 icon="mode_edit"></q-btn>
          <q-btn dense round flat class="text-red-4" @click="deleteRow(props.row)"
                 icon="delete"></q-btn>
        </q-td>
      </template>
    </q-table>
    <q-dialog v-model="priority.prompt" persistent @before-hide="getPriorities">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">New priority</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="priority.description" autofocus @keyup.enter="createPriority"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup/>
          <q-btn flat label="Save" @click="createPriority" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="priority.editPrompt" persistent @before-hide="getPriorities">
      <EditPriority :priority="priority.value" @priority-updated="priority.editPrompt = false"/>
    </q-dialog>
    <q-dialog v-model="priority.deletePrompt" @before-hide="getPriorities">
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="negative" text-color="white"/>
          <span class="q-ml-sm text-weight-bold">Are you sure you want to delete this priority?</span>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup/>
          <q-btn flat label="Yes" color="primary" @click="deletePriority" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import EditPriority from "components/config/forms/EditPriority";
export default {
  name: "SituationTable",
  components: {EditPriority},
  data: () => ({
    priorities: null,
    priority: {
      prompt: false,
      editPrompt: false,
      deletePrompt: false,
      description: '',
      value: null
    },
    table: {
      filter: '',
      // Id, Projeto, Atividade, Hora inicial, Final, Total horas, Editar/Ver/Excluir
      columns: [
        {name: 'id', required: true, label: 'ID', align: 'left', field: row => row.id, sortable: true},
        {
          name: 'description',
          required: true,
          align: 'left',
          label: 'Description',
          field: row => row.description,
          sortable: true
        },
        {name: 'actions', required: true, label: 'Actions', align: 'right', field: 'action', sortable: false},
      ],
      data: [],
      visibleColumns: ['id', 'name', 'actions'],
      pagination: {
        sortBy: 'id',
        descending: false,
        page: 1,
        rowsPerPage: 30,
      },
      isLoading: false,
    },
  }),
  methods: {
    getPriorities() {
      this.$axios.get('/priority/all').then(response => {
        this.table.data = []
        this.priorities = response.data
        this.priorities.forEach(priority => {
          this.table.data.push(priority)
        })
      })
    },
    createPriority() {
      this.$axios.post('priority/', null, {
        params: {
          description: this.priority.description
        }
      }).then(response => {
        this.priority.description = null
        this.priority.prompt = false
        this.getPriorities()
      })
    },
    editRow(row) {
      this.priority.value = row
      this.priority.editPrompt = true
    },
    deleteRow(row) {
      this.priority.value = row
      this.priority.deletePrompt = true
    },
    deletePriority() {
      this.$axios.delete('/priority/',
        {params: {priority_id: this.priority.value.id}}).then(response => {
        this.priority.value = null
        this.priority.editPrompt = false
        this.$emit('priority-deleted')
        this.getPriorities()
      })
    },
  },
  mounted() {
    this.getPriorities()
  }
}
</script>

<style scoped>

</style>
