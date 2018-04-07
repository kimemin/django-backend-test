<template>
<div>
  <ul id="posts">
    <li v-for="post in posts">
      {{ post.pk }}
    </li>
  </ul>
</div>
</template>

<script>
export default {
  name: 'board',
  data: function () {
    return {
      posts: []
    }
  },
  mounted: function () {
    const testUrl = 'http://localhost:8000/posts'
    this.$http.get(testUrl)
    .then((result) => {
      this.posts = result.data;
    })
  }
}
</script>
