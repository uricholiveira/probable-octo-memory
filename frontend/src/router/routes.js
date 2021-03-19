
const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('pages/user/Login'),
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('pages/user/Register'),
  },
  {
    path: '/app',
    component: () => import('layouts/MainLayout'),
    children: [
      { path: '', name: 'Dashboard', component: () => import('pages/user/Dashboard') },
      { path: '/app/task/:id', name: 'TaskDetail', component: () => import('pages/task/Edit') },
    ]
  },
  {
    path: '/config',
    component: () => import('layouts/MainLayout'),
    children: [
      { path: '', name: 'Configuration', component: () => import('pages/config/Index') },
      { path: '/config/user', name: 'UserConfiguration', component: () => import('pages/config/Category') },
      { path: '/config/category', name: 'CategoryConfiguration', component: () => import('pages/config/Category') },
      { path: '/config/situation', name: 'SituationConfiguration', component: () => import('pages/config/Category') },
      { path: '/config/priority', name: 'PriorityConfiguration', component: () => import('pages/config/Category') },
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
