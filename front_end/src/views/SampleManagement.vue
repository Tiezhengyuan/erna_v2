<template>
  <div class="container-manage">
    <div class="manage-navbar">
      <div class="title">
        <span>Select an item...</span>
      </div>
      <ul class="list">
        <li>
          <router-link to="/manage/new_project">New Project</router-link>
        </li>
        <li>
          <router-link to="/manage/parse_samples">Parse Samples</router-link>
        </li>
        <li>
          <router-link to="/manage/edit_project">Edit Project</router-link>
        </li>
      </ul>
    </div>
    <router-view class="content"></router-view>
  </div>
</template>

<script>
export default {
  name: "SampleManagement",
};
</script>

<style scoped>
.container-manage {
  height: 40px;
  margin-top: 5px;
  box-sizing: border-box;
  background-color: lightgoldenrodyellow;
  border: 1px solid goldenrod;
}
.manage-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 40px;
  line-height: 40px;
  background-color: lightcyan;
  margin-bottom: 10px;
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
.container-manager .content {
  height: 800px;
  margin-top: 5px;
  padding: 20px;
  background-color: lightgrey;
}
.title span {
  font-size: 30px;
}
</style>
