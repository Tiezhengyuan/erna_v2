export default {
  // download new genome
  new_project_id(state) {
    return {
      label: "Project ID: ",
      value: state.next_project_id,
    };
  },
  data_source(state) {
    return {
      name: "data_source",
      label: "Data source of genome",
      value: "",
      options: state.data_sources.map((el) => {
        return { value: el, label: el, };
      }),
    };
  },
  specie_group(state) {
    return {
      name: "group",
      label: "Group of organism",
      value: "",
      options: state.specie_groups.map((el) => {
        return { value: el, label: el, };
      }),
    };
  },
  specie(state) {
    const options = state.species.map((el) => {
      return { value: el, label: el, };
    });
    return {
      name: "specie",
      label: "Specie",
      options: options,
    };
  },
  version(state) {
    const options = state.versions.map((el) => {
      return { value: el, label: el, };
    });
    return {
      name: "version",
      label: "Genome version",
      options: options,
    };
  },

  // create new project
  ready_genome(state) {
    const options = state.ready_genomes.map((el) => {
      return {
        value: el.id,
        label: `${el.specie}_${el.data_source}_${el.version}`,
      };
    });
    return {
      name: "genome",
      label: "Genome",
      required: true,
      options: options,
    };
  },

  new_specie(state) {
    const options = state.new_species.map((el) => {
      return {
        value: el,
        label: el,
      };
    });
    return {
      name: "specie",
      label: "Specie",
      options: options,
    };
  },


};
