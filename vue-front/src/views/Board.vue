<template>
  <div class="board">
    <Board/>
    <Footer/>
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue'
import Board from '@/components/Board.vue'

export default {
  name: 'board',
  components: {
    Footer,
    Board
  }
}
</script>
