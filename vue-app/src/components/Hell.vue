<template>
  <div>

    <div style="width:50%;display:inline-block">
      <h4>WebSocket</h4>
      <div class="square" v-for="(i, idx) in websocketitems" v-bind:key="'a' + idx" v-bind:style="squarestyle">
        <div class="innersquare" v-for="(color, idx2) in i" v-bind:key="'b' + idx2" v-bind:style="innersquarestyle">
          <square :color='color' :size='size' :ref="'square' + idx + idx2"/>
        </div>
      </div>
      <div :style="{fontSize: '40px', fontWeight: 'bold'}">{{websocket_count}}</div>
    </div>

    <div style="width:50%;display:inline-block">
      <h4>HTTP</h4>
      <div class="square" v-for="(i, idx) in httpitems" v-bind:key="'c' + idx" v-bind:style="squarestyle">
        <div class="innersquare" v-for="(color, idx2) in i" v-bind:key="'d' + idx2" v-bind:style="innersquarestyle">
          <square :color='color' :size='size' :ref="'square' + idx + idx2"/>
        </div>
      </div>
      <div :style="{fontSize: '40px', fontWeight: 'bold'}">{{http_count}}</div>
    </div>

  </div>
</template>

<script>

import Square from './Square.vue'

const SQUARE_SIZE = 20
const NUM_COLS = 10
const COUNT = 1000

const make2dArray = (start, end) => {
  var arr = [];
  for (let i = start; i <= end; i++) {
    arr.push(new Array(end))
  }
  return arr;
}

export default {
  name: 'HelloWorld',
  props: {},
  components: {
    square: Square
  },
  created: function () {
    this.$connect()
    this.$options.sockets.onopen = () => {
      this.send_message()
    }
    this.$options.sockets.onmessage = function (message) {
      const data = JSON.parse(message.data)
      this.websocketitems[data.x][data.y] = data.color
      if (this.websocket_count < COUNT) {
        this.send_message()
        this.websocket_count += 1
      }
    }

    this.fetch_http()

  },
  methods: {
    send_message: function () {
      this.$socket.send(JSON.stringify({max: NUM_COLS - 1}))
    },
    fetch_http: function () {
      const that = this
      const max = NUM_COLS - 1
      fetch('api/?max=' + max).then(function (response) {
         response.json().then(function (data) {
           that.httpitems[data.x][data.y] = data.color
           if (that.http_count < COUNT) {
             that.fetch_http()
             that.http_count += 1
           }
         })
      })
    }
  },
  data: () => {
    return {
      size: SQUARE_SIZE,
      websocketitems: make2dArray(1, NUM_COLS),
      websocket_count: 0,
      httpitems: make2dArray(1, NUM_COLS),
      http_count: 0,
      squarestyle: {
        height: SQUARE_SIZE + 'px',
        width: NUM_COLS * SQUARE_SIZE + 'px',
        margin: 'auto auto',
      },
      innersquarestyle: {
        height: SQUARE_SIZE + 'px',
        width: SQUARE_SIZE + 'px',
        display: 'inline-block',
        borderRadius: '30px',
        color: 'lightgray',
      }
    }
  }
}
</script>
