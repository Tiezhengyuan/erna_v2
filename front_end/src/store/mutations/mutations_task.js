export default {
  addTask(state, new_task) {
    state.new_task_id += 1;
    state.tasks.push(new_task);
  },
  deleteTask(state, task) {
    state.tasks = state.tasks.filter((el) => {
      return el.task_id == task.task_id ? 0 : 1;
    });
  },
  refreshProjectTasks(state) {
    state.tasks = state.tasks.filter((el) => {
      return el.project == state.current_project ? 0 : 1;
    });
  },
  updateTaskStatus(state, task_obj) {
    state.tasks.forEach((el) => {
      if (el.task_id == task_obj.task_id) {
        el.status = task_obj.status;
      }
    });
  },
  setParentTask(state, task_pair) {
    state.tasks.forEach((el) => {
      if (el.task_id == task_pair[0]) {
        el.parent_task = task_pair[1];
      }
    });
  },
  selectTask(state, task_obj) {
    state.current_task = task_obj;
  },
};
