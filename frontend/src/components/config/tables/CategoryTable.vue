<template>
  <div class="row">
    <q-table
      class="full-width"
      :dense="$q.screen.lt.md"
      title="Categories"
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
              <q-btn size="md" icon="refresh" :loading="table.isLoading" @click="getCategories" flat round/>
            </span>
          </div>
          <div class="col-xs-12 col-sm-4 col-md-4 col-lg-2 col-xl-2"
               :class="[$q.screen.xs ? 'text-left' : 'text-right']">
            <span class="">
              <q-btn size="md" label="New category" :loading="table.isLoading" @click="category.prompt = true"
                     color="primary"/>
            </span>
          </div>
        </div>

      </template>
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn dense round flat class="text-blue-4" @click="editRow(props.row)"
                 icon="mode_edit"/>
          <q-btn dense round flat class="text-red-4" @click="deleteRow(props.row)"
                 icon="delete"/>
        </q-td>
      </template>
    </q-table>
    <q-dialog v-model="category.prompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">New priority</div>
        </q-card-section>
        <q-card-section class="q-pt-none">
          <div class="row q-gutter-md">
            <div class="col-12">
              <q-input dense v-model="category.name" autofocus @keyup.enter="createCategory" label="Name"/>
            </div>
            <div class="col-12">
              <q-select dense :options="category.priority.options" v-model="category.priority.value"
                        label="Priority"/>
            </div>
          </div>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup/>
          <q-btn flat label="Save" @click="createCategory" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="category.editPrompt" persistent @before-hide="getCategories">
      <EditCategory :category="category.value" :priority="category.priority" @category-updated="categoryUpdated"/>
    </q-dialog>
    <q-dialog v-model="category.deletePrompt" @before-hide="getCategories">
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="negative" text-color="white"/>
          <span class="q-ml-sm text-weight-bold">Are you sure you want to delete this category?</span>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup/>
          <q-btn flat label="Yes" color="primary" @click="deleteCategory" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import EditCategory from "components/config/forms/EditCategory";
import {debounce} from "quasar";

export default {
  name: "CategoryTable",
  components: {EditCategory},
  props: {},
  data: () => ({
    category: {
      prompt: false,
      editPrompt: false,
      deletePrompt: false,
      name: '',
      value: null,
      priority: {
        options: [],
        value: null,
      },
    },
    categories: null,
    priorities: [],
    table: {
      filter: '',
      // Id, Projeto, Atividade, Hora inicial, Final, Total horas, Editar/Ver/Excluir
      columns: [
        {name: 'id', required: true, label: 'ID', align: 'left', field: row => row.id, sortable: true},
        {name: 'name', required: true, align: 'left', label: 'Name', field: row => row.name, sortable: true},
        {
          name: 'priority',
          required: true,
          align: 'center',
          label: 'Priority',
          field: row => row.priority.description,
          sortable: true
        },
        {name: 'actions', required: true, label: 'Actions', align: 'right', field: 'action', sortable: false},
      ],
      data: [],
      visibleColumns: ['id', 'name', 'priority', 'actions'],
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
    getCategories: debounce(function () {
      this.$axios.get('category/all').then(response => {
        this.table.data = []
        this.categories = response.data
        this.categories.forEach(category => {
          this.table.data.push(category)
        })
        this.getAllPriorities()
      })
    }, 300),
    getAllPriorities() {
      this.$axios.get('priority/all').then(response => {
        this.priorities = response.data
        this.category.priority.options = []
        this.category.priority.value = null
        this.priorities.forEach(priority => {
          this.category.priority.options.push({value: priority.id, label: priority.description})
        })
      })
    },
    createCategory() {
      this.$axios.post('category/', null, {
        params: {
          name: this.category.name,
          priority_id: this.category.priority.value.value
        }
      }).then(response => {
        this.category.prompt = false
        this.getCategories()
      })
    },
    editRow(row) {
      this.category.value = row
      this.priorities.forEach(priority => {
        if (priority.id === row.priority_id) {
          this.category.priority.value = {value: priority.id, label: priority.description}
        }
      })
      this.category.editPrompt = true
    },
    deleteRow(row) {
      this.category.value = row
      this.category.deletePrompt = true
    },
    deleteCategory() {
      this.$axios.delete('/category/', {params: {category_id: this.category.value.id}}
      ).then(response => {
        this.category.value = null
        this.$emit('category-deleted')
        this.getCategories()
      })
    },
    categoryUpdated() {
      this.category.value = null
      this.category.priority.value = null
      this.category.editPrompt = false
      this.getCategories()
    },
  },
  mounted() {
    this.getCategories()
  }
}
</script>

<style scoped>

</style>
