<template>
  <div class="row">
    <q-table
      class="full-width"
      :dense="$q.screen.lt.md"
      title="Users"
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
              <q-btn size="md" icon="refresh" :loading="table.isLoading" @click="getAllUsers" flat round/>
            </span>
          </div>
          <div class="col-xs-12 col-sm-4 col-md-4 col-lg-2 col-xl-2"
               :class="[$q.screen.xs ? 'text-left' : 'text-right']">
            <span class="">
              <q-btn size="md" label="New user" :loading="table.isLoading" @click="user.prompt = true"
                     color="primary"/>
            </span>
          </div>
        </div>

      </template>
      <template v-slot:body-cell-is_active="props">
        <q-td :props="props">
          <q-badge :class="[props.value === true ? 'bg-positive' : 'bg-negative']">
            {{ props.value }}
          </q-badge>
        </q-td>
      </template>
      <template v-slot:body-cell-is_admin="props">
        <q-td :props="props">
          <q-badge :class="[props.value === true ? 'bg-purple-6' : 'bg-blue-grey-6']">
            {{ props.value }}
          </q-badge>
        </q-td>
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
    <q-dialog v-model="user.prompt" @before-hide="getAllUsers">
      <RegisterUserForm @user-registered="user.prompt = false"/>
    </q-dialog>
    <q-dialog v-model="user.editPrompt" @before-hide="getAllUsers">
      <EditUserForm :user="user.value" @user-updated="userUpdated"/>
    </q-dialog>
    <q-dialog v-model="user.deleteUserPrompt" @before-hide="getAllUsers">
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="negative" text-color="white"/>
          <span class="q-ml-sm text-weight-bold">Are you sure you want to delete this user?</span>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup/>
          <q-btn flat label="Yes" color="primary" @click="deleteUser" v-close-popup/>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import RegisterUserForm from "components/config/forms/RegisterUserForm";
import EditUserForm from "components/config/forms/EditUserForm";

export default {
  name: "UserTable",
  components: {RegisterUserForm, EditUserForm},
  props: {},
  data() {
    return {
      users: null,
      user: {
        prompt: false,
        editPrompt: false,
        deleteUserPrompt: false,
        value: {},
      },
      table: {
        filter: '',
        // Id, Projeto, Atividade, Hora inicial, Final, Total horas, Editar/Ver/Excluir
        columns: [
          {name: 'id', required: true, label: 'ID', align: 'left', field: row => row.id, sortable: true},
          {name: 'name', required: true, align: 'left', label: 'Name', field: row => row.name, sortable: true},
          {
            name: 'lastname',
            required: true,
            align: 'left',
            label: 'Lastname',
            field: row => row.lastname,
            sortable: true
          },
          {name: 'email', required: true, align: 'left', label: 'Email', field: row => row.email, sortable: true},
          {
            name: 'username',
            required: true,
            align: 'left',
            label: 'Username',
            field: row => row.username,
            sortable: true
          },
          {
            name: 'is_active',
            required: true,
            align: 'left',
            label: 'Active',
            field: row => row.is_active,
            sortable: true
          },
          {name: 'is_admin', required: true, align: 'left', label: 'Admin', field: row => row.is_admin, sortable: true},
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
    }
  },
  methods: {
    getAllUsers() {
      this.$axios.get('user/all').then(response => {
        this.table.data = []
        this.users = response.data
        this.users.forEach(user => {
          this.table.data.push(user)
        })
      })
    },
    editRow(row) {
      this.user.value = row
      this.user.editPrompt = true
    },
    deleteRow(row) {
      this.user.value = row
      this.user.deleteUserPrompt = true
    },
    deleteUser() {
      this.$axios.delete('/user/', {params: {user_id: this.user.value.id}}
      ).then(response => {
        this.user.value = null
        this.$emit('user-deleted')
      })
    },
    userUpdated() {
      this.user.value = null
      this.user.editPrompt = false
    }
  },
  mounted() {
    this.getAllUsers()
  }
}
</script>

<style scoped>

</style>
