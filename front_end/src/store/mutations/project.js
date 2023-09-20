const mutations_project = {
  updateNewProject(state, key_val) {
    state.new_project[key_val[0]] = key_val[1];
  },
  selectProject(state, new_project) {
    state.current_project = new_project;
  },
  addNewProject(state) {
    state.projects.push(state.new_project);
    state.new_project = {
      project_id: "P0006",
    };
  },
  deleteProject(state, selected) {
    state.projects = state.projects.filter((el) => {
      return el.project_id != selected;
    });
  },
};
export default mutations_project;
