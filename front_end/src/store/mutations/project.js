const mutations_project = {
  setUserProjects(state, projects) {
    state.projects = projects;
  },
  setNewProject(state) {
    // initialize project_id
    if (state.projects.length > 0) {
      const last = state.projects[state.projects.length - 1];
      const next_id = Number(last.project_id.slice(1)) + 1;
      state.next_project_id = "P" + next_id.toString().padStart(3, "0");
    } else {
      state.next_project_id = "P001";
    }
    state.new_project.project_id = state.next_project_id;
    // initialize other params
    state.new_project.owner = state.current_user.id;
    state.new_project.sequencing = state.default_project.seq.value;
    state.new_project.status = state.default_project.status.value;
  },
  updateNewProject(state, key_val) {
    state.new_project[key_val[0]] = key_val[1];
  },
  selectProject(state, new_project) {
    state.current_project = new_project;
  },
  addNewProject(state) {
    state.projects.push(state.new_project);
  },
  deleteProject(state, selected) {
    state.projects = state.projects.filter((el) => {
      return el.project_id != selected;
    });
  },

  // others
  setNewAnswer(state, answer) {
    state.new_answer = answer;
  },
  setUsers(state, users) {
    state.users = users;
  },
};
export default mutations_project;
