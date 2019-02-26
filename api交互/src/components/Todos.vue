<template>
<div id="todos">
  <ul class="list-group">
    <li class="list-group-item" v-bind:class="{'completed': todo.completed}" v-for="(todo, index) in todos">
      <router-link :to="{name: 'todo', params: {id: todo.id}}">{{ todo.title }}</router-link>
      <button class="btn btn-xs pull-right"
              v-bind:class="[todo.completed ? 'btn-danger' : 'btn-success']"
              v-on:click="toggleComletion(todo)">
        {{ todo.completed ? 'undo' : 'completed' }}
      </button>
      
      <button class="btn btn-warning btn-xs pull-right" v-on:click="deleteTodo(index, todo)">Delete</button>
    </li>
  </ul>
  <todo-form :todos="todos"></todo-form>
</div>
</template>

<script>
import TodoForm from "./TodoForm";

export default {
  name: "todos",
  props: ["todos"],
  methods: {
    deleteTodo(index, todo) {
      this.axios.delete('/api/todo/' + todo.id + '/delete').then(response => {
        console.log(response.data)
        this.todos.splice(index, 1)
      })
      
    },
    toggleComletion(todo) {
      this.axios.patch('/api/todo/' + todo.id + '/completed').then(response => {
        console.log(response.data)
        todo.completed = !todo.completed
      })
      
    }
  },
  components: {
    TodoForm
  }
};
</script>

<style scoped>
.completed {
  color: #5cb85c;
  text-decoration: line-through;
}
</style>
