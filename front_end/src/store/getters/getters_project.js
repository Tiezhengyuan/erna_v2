export default {
  projects_list(state) {
    const options = state.projects.map((el) => {
      return {
        value: el.project_id,
        label: el.project_id,
      };
    });
    return {
      name: "project_id",
      label: "Project ID",
      value: "",
      options: options,
    };
  },
  project_name(state) {
    const val = state.new_project.project_name;
    return {
      name: "project_name",
      label: "Project Name",
      value: val ? val : "",
    };
  },
  description(state) {
    const val = state.new_project.description;
    return {
      name: "description",
      label: "Project Description",
      value: val ? val : "",
    };
  },
  sequencing(state) {
    const val = state.new_project.sequencing;
    return {
      name: "sequencing",
      label: "Sequencing Technique",
      value: val ? val : "",
      required: true,
      options: [
        { value: "M", label: "mRNA-Seq" },
        { value: "MI", label: "miRNA-Seq" },
        { value: "SC", label: "scRNA-Seq" },
        { value: "O", label: "Other" },
      ],
    };
  },
  status(state) {
    const val = state.new_project.status;
    return {
      name: "status",
      label: "Project Status",
      value: val ? val : "",
      options: [
        { value: "A", label: "active" },
        { value: "I", label: "inactive" },
      ],
    };
  },
};
