<template>
  <div class="container">
    <IconDropdown :data="input_data"></IconDropdown>
  </div>
</template>

<script>
import IconDropdown from "../../components/forms/IconDropdown";

export default {
  name: "EditProject",
  components: {
    IconDropdown,
  },
  data() {
    return {
      input_data: {
        label: "Projects",
        options: ["P001", "P002", "P003", "P004"],
      },
    };
  },
};
</script>

<style></style>
