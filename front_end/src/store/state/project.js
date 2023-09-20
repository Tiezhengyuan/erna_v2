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
    seq: {
      name: "seq_tech",
      label: "Sequencing Technique",
      value: "mRNA-Seq",
      options: ["mRNA-Seq", "miRNA-Seq", "scRNA-Seq", "Other"],
    },
    status: {
      name: "status",
      label: "Project Status",
      value: true,
    },
  },
  // all projects
  projects: [
    {
      project_id: "P001",
      project_name: "a",
      description: "",
      seq_tech: "mRNA-Seq",
      status: true,
    },
    {
      project_id: "P002",
      project_name: "b",
      description: "abc",
      seq_tech: "Other",
      status: false,
    },
  ],
  new_project: {
    project_id: "P0005",
  },
  current_project: "",
};

export default state_project;
