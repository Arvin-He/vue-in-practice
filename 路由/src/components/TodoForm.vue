<template>
  <form v-on:submit.prevent="addTodo(newTodo)">
    <div class="form-group">
      <input type="text" class="form-control" placeholder="Add a new todo" v-model="newTodo.title">
    </div>
    <div class="form-group">
      <button class="btn btn-success" type="submit">Add Todo</button>
    </div>
  </form>
</template>

<script>
    export default {
        // name: "TodoForm",
        props: ['todos'],
        data() {
          return {
            newTodo:{id:null, title:"", completed:false}
          }
        },
        methods: {
          addTodo(newTodo){
            this.todos.push(newTodo)
            this.newTodo = {id:null, title:""}
          }
        }
    }
</script>

<style scoped>

</style>
