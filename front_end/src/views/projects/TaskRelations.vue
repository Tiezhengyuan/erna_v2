<template>
  <div class="container task-relations">
    <div class="parent-task">
      <inputDropdown
        :data="other_tasks"
        :receive="setParentTask"
      ></inputDropdown>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import inputDropdown from "../../components/forms/inputDropdown.vue";

export default {
  name: "TaskRelations",
  components: {
    inputDropdown,
  },
  props: ["task"],
  computed: {
    ...mapState(["task_methods", "tasks"]),
    other_tasks() {
      return {
        name: "parent_task",
        label: "Parent task",
        value: "",
        options: this.tasks
          .filter((el) => {
            return el.task_id != this.task.task_id;
          })
          .map((el) => {
            return el.task_id;
          }),
      };
    },
  },
  methods: {
    setParentTask(task_obj) {
      const tuple_pair = [this.task.task_id, task_obj[1]];
      this.$store.commit("setParentTask", tuple_pair);
    },
  },
};
</script>

<style>
.container.task-relations {
  margin: 2px;
}
</style>
