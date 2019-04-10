<template>
  <div class="about">
    <h1>Backend Resources Demo</h1>
    <p>Click links below to fetch data from the Sanic server</p>
    <a href="" @click.prevent="getResource">Fetch</a>&nbsp;
    <a href="" @click.prevent="postResource">Post Resource</a>&nbsp;
    <a href="" @click.prevent="postResourceAuthorized">Post Resource with Auth</a>
    <h4>Results</h4>
    <p v-for="r in resources" :key="r.timestamp">
      Server Timestamp: {{r.timestamp | formatTimestamp }}
    </p>
    <p>{{error}}</p>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'about',
  data () {
    return {
      resources: [],
      error: ''
    }
  },
  methods: {
    getResource () {
      $backend.getResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    postResource () {
      $backend.postResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    postResourceAuthorized () {
      $backend.postResourceAuthorized()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}

</script>

<style lang="scss">
</style>
