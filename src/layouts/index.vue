<template>
<q-layout view="lHh Lpr lFf">
    <q-header>
    <div class="q-px-lg q-pt-xl q-mb-md">
        <div class="text-h3">Subeen's Todo List</div>
        <div class="text-subtitle1">{{ todaysDate }}</div>
    </div>
    <q-img
        src="../statics/mountains.jpg"
        class="header-image absolute-top"/>
    </q-header>
    <q-page-container>
        <keep-alive>
            <router-view />
        </keep-alive>
    </q-page-container>
</q-layout>
</template>

<script>
import { date } from 'quasar'

export default {
name: 'MainLayout',

data () {
    return {
    leftDrawerOpen: false
    }
},

computed: {
    todaysDate () {
    const timeStamp = Date.now()
    return date.formatDate(timeStamp, 'dddd D MMMM')
    }
}
}
</script>

<style lang="stylus">
.header-image
    height 100%
    z-index -1 
    opacity 0.3
    filter grayscale(100%)
</style>