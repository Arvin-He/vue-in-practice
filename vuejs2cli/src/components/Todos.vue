<template>
  <ul class="list-group">
    <li class="list-group-item"
        v-bind:class="{'completed': todo.completed}"
        v-for="(todo,index) in todos">
      {{ todo.title }}
      <button class="btn btn-xs pull-right"
              v-bind:class="[todo.completed ? 'btn-danger' : 'btn-success']"
              v-on:click="toggleComletion(todo)">{{ todo.completed ? 'undo' : 'completed' }}</button>
      <button class="btn btn-warning btn-xs pull-right" v-on:click="deleteTodo(index)">Delete</button>
    </li>
  </ul>
</template>

<script>
    export default {
        // name: "Todos",
        props: ["todos"],
        methods: {
          deleteTodo(index){
            this.todos.splice(index, 1)
          },
          toggleComletion(todo) {
            todo.completed = !todo.completed
          }
        }
    }
</script>

<style scoped>
  .completed {
    color: #5cb85c;
    text-decoration: line-through;
  }
</style>
