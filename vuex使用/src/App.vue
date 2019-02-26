<template>
  <div id="app">
    <!-- <todos :todos="todos"></todos> -->
    <!-- <todo-form :todos="todos"></todo-form> -->
    <router-view :todos="todos"></router-view>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
// import Todos from './components/Todos'
// import TodoForm from './components/TodoForm'
export default {
  name: 'App',
  data() {
    return {todos: [
      // {id:1,title:"Learn Vue.js", completed:false}
    ]
    }
  },
  mounted() {
    this.axios.get('/api/todos').then(response => {
      console.log(response.data["data"])
      this.todos = response.data["data"]
    })
  },
  computed: {
    todosCount() {
      return this.todos.length;
    }
  },
  components: {
    HelloWorld,
    // Todos,
    // TodoForm
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
