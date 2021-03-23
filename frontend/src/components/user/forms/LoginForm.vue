<template>
<div>
  <q-card style="padding: 0.1rem">
    <q-card-section>
      <div class="row q-gutter-sm">
        <div class="col-12">
          <q-input v-model="username" dense outlined placeholder="Username" />
        </div>
        <div class="col-12">
          <q-input v-model="password" clearable dense outlined type="password" placeholder="Password" />
        </div>
      </div>
      <div class="row" style="margin-top: 1rem">
        <q-btn color="primary" label="Sign in" class="full-width" @click="login"/>
      </div>
    </q-card-section>
  </q-card>
</div>
</template>

<script>
export default {
  name: "LoginForm",
  data: () => ({
    username: '',
    password: ''
  }),
  methods: {
    login() {
      this.$axios.post('/user/login',
        null,
        {
          params: {
            username: this.username,
            password: this.password,
          },
        },
        ).then(response => {
          this.$store.dispatch("user/setUser", response.data)
          this.$router.push({name: 'Dashboard'})
      })
    }
  }
}
</script>

<style scoped>

</style>
