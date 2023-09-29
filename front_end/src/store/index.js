import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import state_user from "./state/user";
import state_project from "./state/project";
import state_task from "./state/task";
import state_samples from "./state/samples";
import state_reference from "./state/reference";
import state_bowite from "./state/bowtie";
import icons from "./state/icons";

// import getters_project from "./getters/project";
import getters_user from "./getters/user";
import getters_reference from "./getters/reference";

import mutations_project from "./mutations/project";
import mutations_user from "./mutations/user";
import mutations_task from "./mutations/task";
import mutations_samples from "./mutations/samples";
import mutations_bowtie from "./mutations/bowtie";
import mutations_reference from "./mutations/reference";

import actions_project from "./actions/project";
import actions_user from "./actions/user";
import actions_reference from "./actions/reference";
import test from "./actions/test";

export default new Vuex.Store({
  state: {
    ...state_user,
    ...icons,
    ...state_project,
    ...state_task,
    ...state_samples,
    ...state_bowite,
    ...state_reference,
  },
  getters: {
    // ...getters_project,
    ...getters_user,
    ...getters_reference,
  },
  mutations: {
    ...mutations_project,
    ...mutations_user,
    ...mutations_task,
    ...mutations_samples,
    ...mutations_bowtie,
    ...mutations_reference,
  },
  actions: {
    ...actions_project,
    ...actions_user,
    ...actions_reference,
    ...test,
  },
  modules: {},
});
