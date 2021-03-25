import Vue from "vue";
import axios from "axios";
import {boot} from "quasar/wrappers"
import {Dialog, Loading, QSpinnerTail} from "quasar";
import VueRouter from "vue-router";

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

export default boot(function ({app, store, router}) {
  let config = {
    baseURL:
      process.env.NODE_ENV === "development"
        ? "http://localhost:8000/"
        : "http://54.207.137.8/",
    header: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json; multipart/form-data;'
    },
    withCredentials: false
  };

  const _axios = axios.create(config);
  let n = Loading.setDefaults({spinner: QSpinnerTail, spinnerColor: 'white'})
  _axios.interceptors.request.use(config => {
    Loading.show(n)
    let token = store.getters['user/userGetter'].access_token
    config.headers['Authorization'] = token ? 'Bearer ' + token : ''
    return config
  }, error => {
    Loading.hide()
    return Promise.reject(error)
  })
  _axios.interceptors.response.use(response => {
    Loading.hide()
    return response
  }, error => {
    Loading.hide()
    Dialog.create({
      title: 'Error',
      message: error.response.data.detail
    })
    return Promise.reject(error)
  })

  app.axios = _axios
  store.$axios = _axios
})

