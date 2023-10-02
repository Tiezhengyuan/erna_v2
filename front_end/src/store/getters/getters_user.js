export default {
  project_names(state) {
    return state.projects.map((el) => {
      return el.project_name;
    });
  },
};
