import Vue from 'vue'
import App from './App.vue'
import VueNativeSock from 'vue-native-websocket'

Vue.config.productionTip = false

var wsprotocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://'
var ws = wsprotocol + window.location.hostname + ':' + window.location.port + '/ws/acolor/'

Vue.use(VueNativeSock, ws, {
  connectManually: true,
  reconnection: true,
  reconnectionDelay: 3000
})

new Vue({
  render: h => h(App),
}).$mount('#app')
