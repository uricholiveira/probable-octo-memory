<template>
  <div>
    <q-card style="padding: 0.1rem">
      <q-card-section>
        <div class="row q-gutter-sm justify-center">
          <div class="row justify-between q-gutter-xs">
            <div class="col">
              <q-input v-model="userData.name" dense outlined label="Name"/>
            </div>
            <div class="col">
              <q-input v-model="userData.lastname" dense outlined label="Lastname"/>
            </div>
          </div>
          <div class="col-12 q-gutter-sm">
            <q-input v-model="userData.username" dense outlined label="Username"/>
          </div>
          <div class="col-12 q-gutter-sm">
            <q-input v-model="userData.email" dense outlined label="Email"/>
          </div>
          <div class="col-12">
            <div class="row justify-center">
              <div class="col-6 text-center">
                <q-checkbox v-model="userData.is_admin" label="User is admin?"/>
              </div>
              <div class="col-6 text-center">
                <q-checkbox v-model="userData.is_active" label="User is active?"/>
              </div>
            </div>
          </div>
        </div>
        <div class="row" style="margin-top: 1rem">
          <q-btn color="primary" label="Update" class="full-width" @click="update"/>
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
export default {
  name: "EditUserForm",
  props: {
    user: {
      type: Object
    }
  },
  data() {
    return {
      userData: this.user,
      password: ''
    }
  },
  methods: {
    update() {
      this.$axios.patch('/user/',
        null,
        {
          params: {
            user_id: this.userData.id,
            username: this.userData.username,
            email: this.userData.email,
            name: this.userData.name,
            lastname: this.userData.lastname,
            is_admin: Boolean(this.userData.is_admin),
            is_active: Boolean(this.userData.is_active)
          }
        }
      ).then(response => {
        this.$emit('user-updated')
      })
    }
  }
}
</script>

<style scoped>
</style>
