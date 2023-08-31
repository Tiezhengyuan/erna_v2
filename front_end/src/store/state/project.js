const state_project = {
  new_project: {
    project_id: "P0001",
    project_name: "",
  },
  new_task_id: 10,
  projects: ["", "P001", "P002", "P003", "P004"],
  seq_methods: [
    "sequence alignment",
    "genome alignment",
    "genome assembly",
    "differential analysiss",
    "Trim sequence",
    "Quality control",
  ],
  current_project: "",
  tasks: [
    {
      project: "P001",
      seq_method: "Trim sequence",
      status: "pending",
      task_id: 9,
    },
  ],
};

export default state_project;
