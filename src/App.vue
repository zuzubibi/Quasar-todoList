<template lang="pug">
#q-app
  TodoHeader
  TodoInput(v-model ="todoItems")
  TodoList(v-model= "todoItems")
  TodoFooter(@clearAll="clearAllItems")

</template>

<script>
import TodoHeader from './components/TodoHeader.vue';
import TodoInput from './components/TodoInputItems.vue';
import TodoList from './components/TodoList.vue';
import TodoFooter from './components/TodoFooter.vue';

export default {
  data(){
    return {
      todoItems:[]  // v-model로 값을 다시 가져옴
    }
  },
  methods:{
    clearAllItems(){
      localStorage.clear();
      this.todoItems = [];
    }
  },
  created(){
    if (localStorage.length >0){
      for (var i=0; i <localStorage.length; i++){
        if (localStorage.key(i) !== 'loglevel:webpack-dev-server'){
          this.todoItems.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
        }
      }
    }
  },
  components: {
    TodoHeader,
    TodoInput,
    TodoFooter,
    TodoList,
  },
}
</script>

<style>
body {
  text-align: center;
  background-color: #f6f6f6
}
input {
  border-style: groove;
  width: 200px;
}
button{
  border-style: groove;
}
.shadow{
  box-shadow: 5px 10px 10px rgba(0,0,0, 0.03);
}
</style>