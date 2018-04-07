<template>
<div>
  <b>ajax test</b>
  <div>{{ testText }}</div>
</div>
</template>

<script>
export default {
  name: 'board',
  data: function() {
    return {
      testText: ""
    }
  },
  mounted: function () {
    const testUrl = 'https://jsonplaceholder.typicode.com/posts/1'
    this.$http.get(testUrl)
      .then((result) => {
        console.log(result.data)
        this.testText = result.data.title
      })
  }
}
</script>
