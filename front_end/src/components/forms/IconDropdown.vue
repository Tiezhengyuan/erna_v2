<template>
  <div class="container icon-dropdown">
    <div class="active-dropdown">
      <label class="icon-label">{{ selected }}</label>
      <img
        class="icon-svg"
        src="../../../node_modules/bootstrap-icons/icons/caret-down-fill.svg"
        @click="showItems"
      />
    </div>
    <!-- <select v-if="show_dropdown" v-model="selected" @change="sendSelected">
      <option v-for="(item, i) in data.options" :key="i">
        {{ item }}
      </option>
    </select> -->
    <div v-if="show_dropdown">
      <div
        class="hover-item"
        v-for="(item, i) in data.options"
        :key="i"
        @click="sendSelected(item)"
      >
        {{ item }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "IconDropdown",
  props: ["data", "receive"],
  data() {
    return {
      show_dropdown: false,
      selected: this.data.label,
    };
  },
  methods: {
    showItems() {
      this.show_dropdown = true;
    },
    sendSelected(val) {
      this.selected = val;
      this.show_dropdown = false;
    },
  },
};
</script>

<style scoped>
.container.icon-dropdown {
  /* max-width: 150px; */
  padding: 3px;
}
.container.icon-dropdown:hover {
  background-color: lightcyan;
}
.icon-dropdown .active-dropdown {
  display: flex;
}
.icon-label {
  height: 30px;
  line-height: 30px;
  margin-right: 5px;
  font-weight: bold;
}
.icon-svg {
  height: 30px;
  border: 1px solid grey;
  border-radius: 5px;
}
.container.icon-dropdown .hover-item:hover {
  background-color: lightgreen;
}
</style>
