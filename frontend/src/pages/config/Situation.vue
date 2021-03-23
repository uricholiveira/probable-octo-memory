<template>
  <q-page>
    <div class="row justify-center" style="margin-top: -1.5rem">
      <h4 style="font-weight: bold">Situation</h4>
    </div>
    <SituationTable />
  </q-page>
</template>

<script>
import SituationTable from "components/config/tables/SituationTable";
export default {
  name: "Situation",
  components: {SituationTable}
}
</script>

<style scoped>

</style>
