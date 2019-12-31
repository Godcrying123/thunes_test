import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Transaction from '@/components/Transaction'

/* eslint-disable */
Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/transaction',
            name: 'Transaction',
            component: Transaction
        }
    ]
})
