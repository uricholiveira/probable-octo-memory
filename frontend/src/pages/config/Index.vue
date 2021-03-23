<template>
  <q-page>
    <div class="row justify-center" style="margin-top: -1.5rem">
      <h4 style="font-weight: bold">Configurations</h4>
    </div>
    <ConfigList :configs="configs"/>
  </q-page>
</template>

<script>
import ConfigList from "components/config/lists/ConfigList";

export default {
  name: "Index",
  components: {ConfigList},
  data: () => ({
    configs: [
      {title: 'Users', customClass: ['bg-blue-6 text-white'], to: {name: 'UserConfiguration'}},
      {title: 'Situations', customClass: ['bg-orange-6 text-white'], to: {name: 'SituationConfiguration'}},
      {title: 'Priorities', customClass: ['bg-purple-6 text-white'], to: {name: 'PriorityConfiguration'}},
      {title: 'Categories', customClass: ['bg-blue-grey-6 text-white'], to: {name: 'CategoryConfiguration'}},
    ],
  }),
}
</script>

<style scoped>

</style>
