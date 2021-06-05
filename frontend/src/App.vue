<template>
  <div class="app">
    <Header />
    <router-link to="/"></router-link>
    <router-link to="/about"></router-link>
    <router-link to="/signup"></router-link>

    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>
<style></style>
