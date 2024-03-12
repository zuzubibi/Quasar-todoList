<template>
    <div>
        <ul>
            <li v-for="(todoItem, index) in value" :key="todoItem.item" class="shadow">
                <!-- 1. 체크여부 기능 -->
                <span 
                v-on:click="toggleComplete(todoItem, index)"
                v-bind:class="{checkBtnCompleted: todoItem.completed}">
                    <q-icon name="check"></q-icon>
                </span>

                <!-- 할일 -->
                <span id="here" :class="{textCompleted: todoItem.completed }" :contenteditable="todoItem.edit">
                    {{ todoItem.item }}
                </span>

                <!-- 2. 삭제 기능 -->
                <!-- (1) 아이콘 없는 버전 -->
                <!-- <button v-on:click="removeTodo(todoItem, index)">delete</button> -->

                <!-- (2) 아이콘 있는 버전 -->
                <span v-on:click="removeTodo(todoItem, index)">
                    <q-icon name="delete"></q-icon>
                </span>

                <!-- 3. 수정 기능 -->
                <span >
                    <div v-if="todoItem.edit===false">
                        <q-btn label="수정" v-on:click="editTodo(todoItem, index)"></q-btn>
                    </div>
                    <div v-else>
                        <q-btn push color="primary" label="완료" v-on:click="editOk(todoItem, index)"/>
                        <q-btn push color="primary" label="취소" v-on:click="editNo(todoItem, index)" />
                    </div>
                </span>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    props: ['value'],
    data(){
        return {
            val: "",
        }
    },
    watch:{
        editTodo(oldval, newval){
            if (oldval !== newval){
                console.log(oldval)
                console.log(newval)
                // console.log("여기가 마지막");
            }
        }
    },
    methods: {
        toggleComplete(todoItem, index){
            // this.$emit('toggleItem', todoItem, index)

            // 원래 기존거 삭제
            localStorage.removeItem(todoItem.item);

            // ** 1) 이벤트 버스를 통해 컴포넌트 간의 경계를 명확히 해야함
            // this.todoItems[index].completed = !this.todoItems[index].completed;
            
            const arr = [...this.value.slice(0, index), {...todoItem, completed: !todoItem.completed}, ...this.value.slice(index+1, this.value.length)];
            this.$emit("input", arr);

            // ** 2) 별로 안 좋은 거
            // todoItem.completed = !todoItem.completed;

            // 새로운 변경사항 반영해서 다시 저장
            localStorage.setItem(todoItem.item, JSON.stringify(todoItem))
        },
        removeTodo(todoItem, index){
            // this.$emit('removeItem', todoItem, index)
            localStorage.removeItem(todoItem.item);
            
            const newarr = [...this.value];
            console.log(newarr[index]);
            newarr.splice(index, 1);

            this.$emit('input', newarr);
        },
        editTodo(todoItem, index){
            todoItem.edit = true;
            this.val = document.getElementById("here").innerHTML
            this.val = this.val.trim()
            // console.log(val)
        },
        editOk(todoItem, index){
            todoItem.edit = false;
            console.log(this.val);
            
        },
        editNo(todoItem,index){
            todoItem.edit = false;
            console.log(this.val);
        }
    }
   
}
</script>

<style scoped>
.checkBtn{
    line-height: 45px;
    color: #62acde;
    margin-right: 5px;
}
.checkBtnCompleted{
    color: #b3adad;
}
.textCompleted{
    text-decoration: line-through;
    color: #b3adad;
}
</style>