
<template>
  <div :style="style">{{color}}</div>
</template>

<script>
export default {
  name: 'Square',
  props: ['color', 'size'],
  computed: {
    style: function () {
      return {
        backgroundColor: this.color,
        color: this.color,
        overflow: 'hidden',
        height: '100%',
        borderRadius: this.size + 'px'
      }
    }
  },
}
</script>
