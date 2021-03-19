<template>
  <q-layout view="lHh lpR lFf">

    <q-header elevated class="bg-blue-grey-10 text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left"/>
        <q-space/>
<!--        <q-input dense outlined bg-color="white" color="red" placeholder="Pesquisa" v-model="textSearch"/>-->
<!--        <q-space/>-->
        <div>
          <q-btn round flat @click="avatarDropdown = true">
            <q-avatar>
              <img src="https://cdn.quasar.dev/img/avatar.png">
            </q-avatar>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="left" side="left" behavior="mobile" bordered>
      <!-- drawer content -->
      <SidebarLink :menu="sidebarLinks" :config="configLinks"/>
    </q-drawer>

    <q-page-container>
      <router-view style="padding: 1.5rem 2rem 1.5rem 2rem"/>
    </q-page-container>

  </q-layout>
</template>

<script>
import SidebarLink from "components/SidebarLink";

export default {
  components: {SidebarLink},
  data() {
    return {
      left: false,
      textSearch: '',
      avatarDropdown: false,
      sidebarLinks: {
        group: [
          {
            name: 'Dashboard',
            icon: 'developer_board',
            pathName: 'Dashboard',
          },
        ]
      },
      configLinks: {
        group: [
          {
            name: 'Configuration',
            icon: 'settings',
            pathName: 'Configuration',
            submenu: [
              {title: 'Category', icon: 'manage_accounts', pathName: 'CategoryConfiguration'},
            ]
          },
        ]

      }
    }
  }
}
</script>
