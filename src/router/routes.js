const routes = [
  {
    path: '/',
    component: () => import('src/layouts/index.vue'),
    children: [
      { path: '', component: () => import('src/pages/Todo.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
