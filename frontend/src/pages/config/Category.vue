<template>
  <q-page>
    <div class="row justify-center" style="margin-top: -1.5rem">
      <h4 style="font-weight: bold">Category</h4>
    </div>
    <CategoryTable />
  </q-page>
</template>

<script>
import CategoryTable from "components/config/tables/CategoryTable";
export default {
  name: "Category",
  components: {CategoryTable}
}
</script>

<style scoped>
.row {
  margin-top: 1rem;
}
</style>
