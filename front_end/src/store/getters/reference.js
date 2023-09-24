const getters_reference = {
  data_source() {
    return {
      name: "data_source",
      label: "Source of reference sequences",
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
};

export default getters_reference;
