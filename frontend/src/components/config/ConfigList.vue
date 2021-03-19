<template>
  <div class="row">
    <div class="row justify-center full-width">
      <q-input dense outlined label="Search" v-model="filter.text"/>
    </div>
    <hr class="q-mt-lg" width="70%">
    <div class="row wrap justify-center q-gutter-sm full-width">
      <div class="col-xs-12 col-sm-4 col-md-3 col-lg-2" v-for="(config, index) in configs" :key="index">
        <q-btn dense round flat stretch class="full-width" :to="config.to">
          <q-card bordered class="shadow-12 q-pa-lg full-width card-hover" :class="config.customClass">
            <q-card-section class="text-center">
              <div class="text-h5 q-mt-sm q-mb-xs full-width">{{config.title}}</div>
            </q-card-section>
          </q-card>
        </q-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ConfigList",
  props: {
    configs: {
      type: Array,
      default: () => [{title: 'Config default', customClass: ['bg-blue-6 text-white'], to: {name: 'Configuration'}}]
    }
  },
  data: () => ({
    filter: {
      text: ''
    }
  }),
}
</script>

<style scoped>
.row {
  margin-top: 0.5rem;
}

.card-hover:hover {
  opacity: 60%;
}
</style>
