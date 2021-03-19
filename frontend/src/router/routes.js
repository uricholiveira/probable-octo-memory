
const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('pages/user/Login.vue'),
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('pages/user/Register.vue'),
  },
  {
    path: '/app',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'Dashboard', component: () => import('pages/user/Dashboard.vue') },
      { path: '/app/task/:id', name: 'TaskDetail', component: () => import('pages/task/Edit.vue') },
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
