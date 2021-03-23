<template>
  <q-page>
    <div class="row justify-center" style="margin-top: -1.5rem">
      <h4 style="font-weight: bold">Priority</h4>
    </div>
    <PriorityTable />
  </q-page>
</template>

<script>
import PriorityTable from "components/config/tables/PriorityTable";
export default {
  name: "Priority",
  components: {PriorityTable}
}
</script>

<style scoped>

</style>
