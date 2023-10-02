export default {
  // sry
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
    // state.new_project.sequencing = state.default_project.sequencing.value;
    // state.new_project.status = state.default_project.status.value;
  },
  setCurrentProject(state, project) {
    state.current_project = project;
    state.current_updated_project = {
      owner: project.owner,
    };
  },
  setNextProjectID(state, data) {
    state.next_project_id = data.project_id;
  },
  // update
  updateUpdatedProject(state, key_val) {
    state.updated_project[key_val[0]] = key_val[1];
  },
  updateNewProject(state, key_val) {
    state.new_project[key_val[0]] = key_val[1];
  },
  addNewProject(state) {
    state.projects.push(state.new_project);
  },
  selectProject(state, selected_project) {
    state.current_project = selected_project;
  },
  updateCurrentProject(state, key_val) {
    state.current_project[key_val[0]] = key_val[1];
    state.current_updated_project[key_val[0]] = key_val[1];
    console.log(state.current_updated_project);
  },
  updateUpdated(state) {
    const curr_id = state.current_project.id;
    state.updated_projects[curr_id] = state.current_updated_project;
    console.log(state.updated_projects);
    state.current_project = {};
    state.current_updated_project = {};
  },

  // deleted
  updateDeleted(state, selected) {
    // update state.projects
    state.projects = state.projects.filter((el) => {
      return el.id != selected;
    });
    // update state.deleted_projects
    state.deleted_projects.push(selected);
  },
};
