<template>
  <div id="app">
    <Header />
    <div class="body-wrapper">
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from './components/header.vue'

export default {
  name: 'App',
  components: {
    Header,
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin: 0;
  }

  .body-elements {
    height: 908px;
    overflow: scroll;
    overflow-x: hidden;
  }

  .body-wrapper {
    width: 100%;
    height: 100%;
    overflow: auto;
  }

  button,
  button:active,
  button:focus {
    outline: none;
  }
</style>
