export default {
  study_name() {
    return {
      name: "study_name",
      label: "Study name",
      value: "",
    };
  },
  study_names(state) {
    return {
      name: "study_name",
      label: "Study name",
      value: "",
      options: state.study_names.map((el) => {
        return {
          value: el,
          label: el,
        };
      }),
    }
  },
  sample_name_reg(state) {
    return {
      name: "reg",
      label: "RegExpression",
      value: state.parse_samples.reg,
    };
  },
};
