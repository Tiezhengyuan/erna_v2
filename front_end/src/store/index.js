import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import state_user from "./state/user";
import state_project from "./state/project";
import state_task from "./state/task";
import state_samples from "./state/samples";
import state_bowite from "./state/bowtie";
import icons from "./state/icons";

import getters_user from "./getters/user";

import mutations_project from "./mutations/project";
import mutations_user from "./mutations/user";
import mutations_task from "./mutations/task";
import mutations_samples from "./mutations/samples";
import mutations_bowtie from "./mutations/bowtie";

import actions_project from "./actions/project";
import actions_user from "./actions/user";

export default new Vuex.Store({
  state: {
    ...state_user,
    ...icons,
    ...state_project,
    ...state_task,
    ...state_samples,
    ...state_bowite,
  },
  getters: {
    ...getters_user,
  },
  mutations: {
    ...mutations_project,
    ...mutations_user,
    ...mutations_task,
    ...mutations_samples,
    ...mutations_bowtie,
  },
  actions: {
    ...actions_project,
    ...actions_user,
  },
  modules: {},
});
