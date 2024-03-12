<template lang="pug">
div
    input(type="text" v-model="newTodoItem" @keyup.enter="addTodo")
    button(@click="addTodo") add

</template>

<script>
export default {
    props: {value: Array},

    data(){
        return {
            newTodoItem: "",
            todoItems: [],
        }
    },
    watch:{
        todoItems(oldval,newval){
            if (oldval !== newval){
                this.$emit('input', this.todoItems);
            }
        }
    },
    methods:{
        addTodo(){
            if (this.newTodoItem !== '') {
                const obj = {completed: false, item: this.newTodoItem }
                localStorage.setItem(this.newTodoItem, JSON.stringify(obj));
                this.todoItems = [...this.value, obj];

                // 직접 접근은 위험합니다.
                // this.todoItems.push(this.todoItems);

                this.clearInput();
                // this.todoItems = [];
            } else{
                alert("type smt");
            }
        },
        clearInput(){
            this.newTodoItem = '';
        }
    },

}
</script>

<style scoped>

</style>