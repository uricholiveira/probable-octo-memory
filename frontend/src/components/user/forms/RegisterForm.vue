<template>
  <div>
    <q-card style="padding: 0.1rem">
      <q-card-section>
        <div class="row q-gutter-sm justify-center">
          <div class="row justify-between q-gutter-xs">
            <div class="col">
              <q-input v-model="name" dense outlined label="Name"/>
            </div>
            <div class="col">
              <q-input v-model="lastname" dense outlined label="Lastname"/>
            </div>
          </div>
          <div class="col-12 q-gutter-sm">
            <q-input v-model="username" dense outlined label="Username"/>
          </div>
          <div class="col-12 q-gutter-sm">
            <q-input v-model="email" dense outlined label="Email"/>
          </div>
          <div class="col-12 q-gutter-sm">
            <q-input v-model="password" clearable dense outlined type="password" label="Password"/>
          </div>
        </div>
        <div class="row" style="margin-top: 1rem">
          <q-btn color="primary" label="Register" class="full-width" @click="register"/>
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
export default {
  name: "RegisterForm",
  data: () => ({
    username: '',
    email: '',
    password: '',
    name: '',
    lastname: ''
  }),
  methods: {
    register() {
      this.$axios.post('/user/',
        {},
        {
          params: {
            username: this.username,
            email: this.email,
            password: this.password,
            name: this.name,
            lastname: this.lastname
          },
        },
      ).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
</style>
