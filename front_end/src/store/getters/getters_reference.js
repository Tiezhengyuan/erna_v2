export default {
  new_project_id(state) {
    return {
      label: "Project ID: ",
      value: state.next_project_id,
    };
  },
  data_source() {
    return {
      name: "data_source",
      label: "Source of genome sequences",
      value: "NCBI",
      options: [
        { value: "NCBI", label: "NCBI" },
        { value: "ENSEMBL", label: "ENSEMBL" },
        { value: "other", label: "other" },
      ],
    };
  },
  specie(state) {
    const options = state.species.map((el) => {
      return {
        value: el.id,
        label: el.specie_name,
      };
    });
    return {
      name: "specie",
      label: "Specie",
      options: options,
    };
  },
  genome(state) {
    const options = state.genomes.map((el) => {
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
