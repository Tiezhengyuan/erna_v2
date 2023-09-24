const state_project = {
  // default values
  default_project: {
    project_name: {
      name: "project_name",
      label: "Project Name",
      value: "",
    },
    description: {
      name: "description",
      label: "Project Description",
      value: "",
    },
    sequencing: {
      name: "sequencing",
      label: "Sequencing Technique",
      value: "M",
      options: [
        { value: "M", label: "mRNA-Seq" },
        { value: "MI", label: "miRNA-Seq" },
        { value: "SC", label: "scRNA-Seq" },
        { value: "O", label: "Other" },
      ],
    },
    status: {
      name: "status",
      label: "Project Status",
      value: "A",
      options: [
        { value: "A", label: "active" },
        { value: "I", label: "inactive" },
      ],
    },
  },
  projects: [],
  next_project_id: "",
  new_project: {},
  current_project: {},
  current_updated_project: {},
  updated_projects: {},
  deleted_projects: [],
};

export default state_project;
