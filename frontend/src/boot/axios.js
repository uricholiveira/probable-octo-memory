import Vue from "vue";
import axios from "axios";
import {boot} from "quasar/wrappers"

Vue.use({
  install(Vue, options) {
    Vue.mixin({
      beforeCreate() {
        const options = this.$options
        if (options.axios) {
          this.$axios = options.axios
        } else if (options.parent) {
          this.$axios = options.parent.$axios
        }
      }
    })
  }
})

export default boot(function ({app, store}) {
  let config = {
    baseURL:
      process.env.NODE_ENV === "development"
        ? "http://localhost:8000/"
        : "http://localhost:8000/",
    header: {
      'Access-Control-Allow-Origin': '*'
    },
    withCredentials: false
  };

  const _axios = axios.create(config);
  _axios.interceptors.request.use(config => {
    let token = store.getters['user/tokenGetter']
    config.headers['Authorization'] = token ? 'Bearer ' + token : ''
    return config
  }, error => {
    return Promise.reject(error)
  })
  _axios.interceptors.response.use(response => {
    return response
  }, error => {
    return Promise.reject(error)
  })

  app.axios = _axios
  store.$axios = _axios
})

