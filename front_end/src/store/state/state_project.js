export default {
  // set by fetch
  projects: [],
  next_project_id: "",
  // new project
  new_project: {
    project_name: "",
    description: "",
    sequencing: null,
    status: "A",
    genome: null,
  },
  //store updated before submit
  updated_project: {},

  // selection
  current_project: {},
  current_updated_project: {},
  deleted_projects: [],
};
