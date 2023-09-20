import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import state_project from "./state/project";
import state_task from "./state/task";
import state_samples from "./state/samples";
import state_bowite from "./state/bowtie";
import icons from "./state/icons";

import mutations_project from "./mutations/project";
import mutations_task from "./mutations/task";
import mutations_samples from "./mutations/samples";
import mutations_bowtie from "./mutations/bowtie";

import actions_project from "./actions/project";

export default new Vuex.Store({
  state: {
    ...icons,
    ...state_project,
    ...state_task,
    ...state_samples,
    ...state_bowite,
  },
  getters: {},
  mutations: {
    ...mutations_project,
    ...mutations_task,
    ...mutations_samples,
    ...mutations_bowtie,
  },
  actions: {
    ...actions_project,
  },
  modules: {},
});
