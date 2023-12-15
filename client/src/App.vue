
<template>
  <HelloWorld />
  <h1>{{example}}</h1>
</template>

<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import { ref } from "vue"

let example = ref<String>()

fetch("http://localhost:8000/api/example").then(res => {
    return res.json()
}).then(data => {
    example.value = data.message
})
</script>
