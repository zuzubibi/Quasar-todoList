<template lang='pug'>
.q-layout(view="1Hh Lpr lFf")
    .q-header
        .q-px-lg.q-pt-xl.q-mb-md
            .text-h3 Subeen's Todo List
            .text-subtitle1 {{ todaysDate }}

</template>

<script>
import {date} from 'quasar'
export default {
    computed: {
        todaysDate (){
            const timeStamp = Date.now()
            return date.formatDate(timeStamp, 'dddd D MMMM')
        }
    }


}
</script>

<style lang="stylus" scoped>
.q-layout
    background-color #64ffda
    padding 20px
.header-image
    height 100%
    z-index -1
    opacity 0.3
    filter grayscale(100%)
</style>