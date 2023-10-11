<template>
  <div class="container">
    <div class="navbar">
      <div class="title">
        <span>Applications</span>
      </div>
      <ul class="list">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/manage">Management</router-link></li>
        <li><router-link to="/rnaseq">RNA-Seq</router-link></li>
        <li><router-link to="/tools">Tools</router-link></li>
      </ul>
    </div>
    <router-view class="content"></router-view>
  </div>
</template>

<script>
export default {
  name: "ContentPage",
};
</script>

<style scoped>
.container {
  height: 40px;
  margin-top: 5px;
  box-sizing: border-box;
  background-color: lightgoldenrodyellow;
  border: 1px solid goldenrod;
}
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 40px;
  line-height: 40px;
}
ul {
  list-style-type: none;
}
li {
  display: inline;
  padding-left: 10px;
  padding-right: 10px;
  border-right: 1px solid black;
}
.list li:last-child {
  border: 0;
}
.container .content {
  height: 1200px;
  margin-top: 5px;
  padding: 20px;
  background-color: lightgrey;
}
</style>
