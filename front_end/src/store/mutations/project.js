const mutations_project = {
  updateProject(state, new_project) {
    state.new_project = new_project;
    console.log(Object.values(state.new_project));
  },
  selectProject(state, new_project) {
    state.current_project = new_project;
  },
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
        console.log(el.status);
      }
    });
  },
};
export default mutations_project;
