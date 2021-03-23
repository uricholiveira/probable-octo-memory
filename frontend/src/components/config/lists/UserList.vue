<template>
  <div class="row wrap justify-center q-gutter-sm full-width">
    <div class="col-xs-12 col-sm-5 col-md-5 col-lg-2" v-for="(user, index) in filteredUsers" :key="index">
      <q-card class="shadow-0 q-card--bordered full-width card-hover">
        <q-card-section>
          <div class="row wrap">
            <div class="col-12">
              <div class="row justify-between">
                <div>
                  {{ user.name }} {{ user.lastname }}
                </div>
                <div>
                  <q-badge color="positive" label="Active" v-if="user.is_active === true"/>
                  <q-badge color="positive" label="Not active" v-else/>
                </div>
              </div>
            </div>
            <div class="col-12 q-mt-sm">
              <div class="row justify-between">
                <div>
                  {{ user.username }}
                </div>
                <div v-if="user.is_admin === true">
                  <q-badge color="purple" label="Admin"/>
                </div>
              </div>
            </div>
            <div class="col-12 q-mt-sm">
              <div class="row justify-center">
                {{ user.email }}
              </div>
            </div>
            <div class="col-12 q-mt-sm">
              <div class="row justify-center q-gutter-md">
                <q-btn dense flat label="Edit" class="text-blue-6" size="md" @click="editUser(user)"/>
                <q-btn dense flat label="Delete" class="text-red-6" size="md" @click="deletePrompt(user)"/>
              </div>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>

  </div>
</template>

<script>

export default {
  name: "UserList",
  components: {},
  props: {
    users: {
      type: Array,
      default: null
    },
    filter: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      editUserPrompt: false,
      deleteUserPrompt: false,
      user: null
    }
  },
  methods: {
    getUsers() {
      this.user = null
      this.$emit('get-all-users')
    },
    editUser(user) {
      this.editUserPrompt = true
      this.user = user
    },
    deleteUser() {
      this.$axios.delete('/user/',
        null,
        {
          params: {
            user_id: this.user.id,
          }
        }
      ).then(response => {
        this.user = null
        this.$emit('user-deleted')
      })
    },
    deletePrompt(user) {
      this.deleteUserPrompt = true
      this.user = user
    }
  },
  computed: {
    filteredUsers() {
      return this.users.filter(user => {
        return user.name.toUpperCase().match(
          this.filter.toUpperCase()
        )
      })
    }
  }
}
</script>

<style scoped>

</style>
