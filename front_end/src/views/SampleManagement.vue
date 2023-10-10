<template>
  <div class="container-manage">
    <div class="manage-navbar">
      <div class="title">
        <span>Select...</span>
      </div>
      <ul class="list">
        <li>
          <router-link to="/manage/load_samples">Load Samples</router-link>
        </li>
        <li>
          <router-link to="/manage/create_project">Create Project</router-link>
        </li>
        <li>
          <router-link to="/manage/import_raw_data">Import Raw Data</router-link>
        </li>
        <li>
          <router-link to="/manage/build_reference">
            Build Reference
          </router-link>
        </li>
        <li>
          <router-link to="/manage/update_projects">
            Update Projects
          </router-link>
        </li>
      </ul>
    </div>
    <div>
      <router-view class="content"></router-view>
    </div>
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
  font-size: 16px;
  font-weight: bold;
}
li {
  display: inline;
  padding-left: 5px;
  padding-right: 5px;
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
