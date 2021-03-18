<template>
  <div>
    <div class="row" style="width: 100%; padding: 1.5rem;">
      <div class="col">
        <div class="row justify-center">
          <q-avatar size="72px">
            <img src="https://cdn.quasar.dev/img/avatar.png">
          </q-avatar>
        </div>
        <div class="row justify-center" style="margin-top: 2rem;">
          Hello USER! Welcome back
        </div>
      </div>
    </div>
    <div style="margin-top: 4rem">
      <q-expansion-item
        v-for="(menu, key) in menu.group"
        dense-toggle
        group="somegroup"
        expand-icon-class="hidden"
        :key="key"
        :icon="menu.icon"
        :label="menu.name"
        exact
        dense
      >
        <q-item
          clickable
          dense
          v-for="(submenu, submenuKey) in menu.submenu"
          :key="submenuKey"
          :to="{name: submenu.pathName}"
          style="text-decoration: none;"
        >
          <q-item-section
            v-if="submenu.icon"
            avatar
          >
            <q-icon :name="submenu.icon"/>
          </q-item-section>

          <q-item-section>
            <q-item-label>{{ submenu.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-expansion-item>
    </div>
    <div>
      <q-expansion-item
        v-for="(config, key) in config.group"
        dense-toggle
        group="somegroup"
        expand-icon-class="hidden"
        :key="key"
        :icon="config.icon"
        :label="config.name"
        :hidden="!$store.getters['user/userAdmin']"
        exact
        dense
      >
        <q-item
          clickable
          dense
          v-for="(submenu, submenuKey) in config.submenu"
          :key="submenuKey"
          :to="{name: submenu.pathName}"
          style="text-decoration: none;"
        >
          <q-item-section
            v-if="submenu.icon"
            avatar
          >
            <q-icon :name="submenu.icon"/>
          </q-item-section>

          <q-item-section>
            <q-item-label>{{ submenu.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-expansion-item>
    </div>
    <div class="absolute-bottom">
      <div class="row justify-center text-blue-grey-10">
        Versão 1.0 (test)
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SidebarLink",
  props: {
    menu: {
      type: Object,
      required: true
    },
    config: {
      type: Object,
      required: true
    }
  },
  data() {
    return {}
  }
}
</script>

<style scoped>

</style>
