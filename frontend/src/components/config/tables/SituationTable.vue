<template>
  <div class="row">
    <q-table
      class="full-width"
      :dense="$q.screen.lt.md"
      title="Situations"
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
              <q-btn size="md" icon="refresh" :loading="table.isLoading" @click="getSituations" flat round/>
            </span>
          </div>
          <div class="col-xs-12 col-sm-4 col-md-4 col-lg-2 col-xl-2"
               :class="[$q.screen.xs ? 'text-left' : 'text-right']">
            <span class="">
              <q-btn size="md" label="New situation" :loading="table.isLoading" @click="situation.prompt = true"
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
    <q-dialog v-model="situation.prompt" persistent @before-hide="getSituations">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">New situation</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="situation.description" autofocus @keyup.enter="createSituation"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup/>
          <q-btn flat label="Save" @click="createSituation" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="situation.editPrompt" persistent @before-hide="getSituations">
      <EditSituation :situation="situation.value" @situation-updated="situation.editPrompt = false"/>
    </q-dialog>
    <q-dialog v-model="situation.deletePrompt" @before-hide="getSituations">
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="negative" text-color="white"/>
          <span class="q-ml-sm text-weight-bold">Are you sure you want to delete this situation?</span>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup/>
          <q-btn flat label="Yes" color="primary" @click="deleteSituation" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import EditSituation from "components/config/forms/EditSituation";
export default {
  name: "SituationTable",
  components: {EditSituation},
  props: {EditSituation},
  data: () => ({
    situations: null,
    situation: {
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
    getSituations() {
      this.$axios.get('/situation/all').then(response => {
        this.table.data = []
        this.situations = response.data
        this.situations.forEach(situation => {
          this.table.data.push(situation)
        })
      })
    },
    createSituation() {
      this.$axios.post('situation/', null, {
        params: {
          description: this.situation.description
        }
      }).then(response => {
        this.situation.description = null
        this.situation.prompt = false
        this.getSituations()
      })
    },
    editRow(row) {
      this.situation.value = row
      this.situation.editPrompt = true
    },
    deleteRow(row) {
      this.situation.value = row
      this.situation.deletePrompt = true
    },
    deleteSituation() {
      this.$axios.delete('/situation/',
        {params: {situation_id: this.situation.value.id}}).then(response => {
        this.situation.value = null
        this.situation.editPrompt = false
        this.$emit('situation-deleted')
        this.getSituations()
      })
    },
  },
  mounted() {
    this.getSituations()
  }
}
</script>

<style scoped>

</style>
