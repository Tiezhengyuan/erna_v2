<template>
  <div class="container">
    <div class="logo">
      <img src="#" />
    </div>
    <div>
      <h1>eRNA v2</h1>
    </div>
    <div class="login">
      User Name: <mark>{{ user_name }}</mark> |
      <a href="#">logout</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeaderBar",
  data() {
    return {
      user_name: "Tiezheng Yuan",
    };
  },
};
</script>

<style scoped>
.container {
  height: 100px;
  background-color: lightblue;
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
}
.container .logo {
  width: 100px;
  border: 1px solid white;
}
.container .login {
  text-align: right;
  margin-top: 10px;
}
a {
  margin-left: 10px;
  margin-right: 10px;
}
</style>
