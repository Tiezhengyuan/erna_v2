const getters_user = {
  project_names(state) {
    return state.projects.map((el) => {
      return el.project_name;
    });
  },
};

export default getters_user;
