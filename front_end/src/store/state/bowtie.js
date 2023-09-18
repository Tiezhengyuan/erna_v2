const state_bowtie = {
  bowtie_params: {
    specie: {
      name: "specie",
      label: "Specie",
      options: ["human", "mouse", "rat"],
    },
    raw_format: {
      name: "raw_format",
      label: "File format of raw data",
      options: ["FASTQ", "FASTA"],
    },
    mismatches: {
      name: "mismatches",
      label: "Number of mismatches",
      value: 0,
      min: 0,
      max: 2,
    },
    seed_length: {
      name: "seed_length",
      label: "Length of seed substrings",
      value: 20,
      min: 15,
      max: 30,
    },
    gaps: {
      name: "gaps",
      label: "Number of disallowed gaps",
      value: 15,
      min: 10,
      max: 30,
    },
    match_bonus: {
      name: "match_bonus",
      label: "Match bonus",
      value: 2,
      min: 0,
      max: 4,
    },
    suppress_unalign: {
      name: "suppress_unalign",
      label: "Suppress unaligned records in SAM",
      value: false,
    },
    suppress_header: {
      name: "suppress_header",
      label: "Suppress SAM header",
      value: false,
    },
    suppress_sq_header: {
      name: "suppress_sq_header",
      label: "Suppress @SQ SAM header",
      value: false,
    },
  },
};
export default state_bowtie;
