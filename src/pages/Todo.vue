<template lang="pug">
q-page
  .wrap
    input.search-input(type='text' placeholder="데이터를 입력해주세요" v-model="message")
    q-btn.search-btn(color='deep-orange' glossy label="추가" v-on:click="addTodo")

  .app
    p {{ message }}


</template>

<script>
export default {
  name: 'Todo',
  components:{
  // TodoButton,
  // TodoList,
  // TodoInput,
  // TodoSelect
  },
  data() {
    return {
      message: '',
      todoList: [
        {
            title: '기깔나게 숨쉬기',
            complete: false
        },
        {
            title: '멋있게 코딩하기',
            complete: false
        }
      ]
    }
  },
  computed: {
  },
  methods:{
    addTodo: function(){
      console.log(this.newTodoItem);
    }
  }
}
</script>

<style lang="stylus" scoped>
.q-page
  padding 10px
  padding-top 20px
  
  .wrap
    // background: yellow
    width 100%
    height 40px
    padding 0 10px
    display flex
    gap 15px
    font-size 60.5%

    .search-input
      // background-color: red
      // width 50%
      height 100%
      flex 7
      font-size 0.85rem
      padding-left 10px
      border-radius 10px

    .search-btn
      // width: 10px
      height: 100% 
      font-size 0.75rem 
      flex: 1.5
      margin-left 10px

  .app
    width 100%
    height 50px
    padding 10px 20px
    margin-top 20px
    font-size 15px
    background-color:red
</style>
    