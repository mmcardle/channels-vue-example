<template>
  <div id="app">
    <Hell />
  </div>
</template>

<script>
import Hell from './components/Hell.vue'

export default {
  name: 'app',
  components: {
    Hell
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
