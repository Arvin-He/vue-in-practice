// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import App from './App'
import Todos from './components/Todos'
import Todo from './components/Todo'
// Vue.config.productionTip = false

Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [
  {path: '/', component:Todos},
  {path: '/todo/:id', component:Todo, name:'todo'},
]

const router = new VueRouter({
  routes
})

const store = new Vuex.Store({
  state: {
    todos: []
  },
  // mutations存放方法的结合,负责更新state中的数据
  mutations: {
    get_todos_list (state, todos) {
      state.todos = todos
    }
  },
  // actions用于和后台打交道,负责从后端获取数据
  actions: {
    getTodos(store) {
      Vue.axios.get('/api/todos').then(response => {
        store.commit('get_todos_list', response.data)
      })
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  router,
  store
})
