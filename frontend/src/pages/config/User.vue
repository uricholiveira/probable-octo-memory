<template>
  <q-page>
    <div class="row justify-center" style="margin-top: -1.5rem">
      <h4 style="font-weight: bold">User</h4>
    </div>
    <UserTable />
  </q-page>
</template>

<script>
import UserTable from "components/config/tables/UserTable";
import RegisterUserForm from "components/config/forms/RegisterUserForm";
export default {
  name: "User",
  components: {UserTable},
  props: {},
  data: () => ({}),
  methods: {},
  mounted() {}
}
</script>

<style scoped>
.row {
  margin-top: 1rem;
}
</style>
