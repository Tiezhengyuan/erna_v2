const state_project = {
  new_project: {
    project_id: "P0001",
    project_name: "",
  },
  new_task_id: 10,
  projects: ["", "P001", "P002", "P003", "P004"],
  task_methods: [
    { task_method: "sequence alignment", component: "AlignerBowtie" },
    { task_method: "genome alignment", component: "AlignerTophat" },
    { task_method: "genome assembly", component: "AssemblerCufflinks" },
    { task_method: "Count reads", component: "CountReads" },
    { task_method: "trim sequence", component: "TrimSeq" },
    { task_method: "quality control", component: "" },
  ],
  tasks: [
    {
      project: "P001",
      task_method: "Trim sequence",
      status: "pending",
      parent_task: "",
      task_id: 9,
    },
  ],
  current_project: "",
  current_task: {},
};

export default state_project;
