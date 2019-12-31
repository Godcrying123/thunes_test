// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// import App from './App'
import router from './router'
import iView from 'iview'
import 'view-design/dist/styles/iview.css'
import { ValidationProvider, extend, ValidationObserver } from 'vee-validate'
import { required, email, digits, length, integer } from 'vee-validate/dist/rules'
import VueSource from 'vue-resource'
import QS from 'qs'
import axios from 'axios'
import VueAxios from 'vue-axios'

/* eslint-disable no-new */
/* eslint-disable */
// eslint-disable-next-line

Vue.config.productionTip = false
Vue.use(iView, VueSource, VueAxios, axios)
Vue.prototype.$axios = axios
Vue.prototype.qs = QS

// Override the default required rule
extend('required', {
    ...required,
    message: 'This field is required'
})

// Override the default email rule
extend('email', {
    ...email,
    message: 'This field is Email format required'
})

// extend the digits rule
extend('digits', digits)

// extend the regex rule
extend('length', length)

// extend the integer rule

extend('integer', {
    ...integer,
    message: 'This field must be an integer'
})

Vue.component('ValidationProvider', ValidationProvider)
Vue.component('ValidationObserver', ValidationObserver)

new Vue({
    el: '#app',
    router,
    template: `
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Thunes</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item nav-link">
                        <router-link to="/">Home</router-link>
                    </li>
                    <li></li>
                    <li class="nav-item nav-link">
                        <router-link to="/transaction">Transactions</router-link>
                    </li>
                </ul>
            </div>
        </nav>
        <hr><br>
        <router-view></router-view>
    </div>
  `
}).$mount('#app')