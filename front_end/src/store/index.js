import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import state_user from "./state/state_user";
import state_project from "./state/state_project";
import state_task from "./state/state_task";
import state_sample from "./state/state_sample";
import state_reference from "./state/state_reference";
import state_bowite from "./state/state_bowtie";
import state_icons from "./state/state_icons";

import getters_user from "./getters/getters_user";
import getters_project from "./getters/getters_project";
import getters_reference from "./getters/getters_reference";
import getters_sample from "./getters/getters_sample";

import mutations_project from "./mutations/mutations_project";
import mutations_user from "./mutations/mutations_user";
import mutations_task from "./mutations/mutations_task";
import mutations_sample from "./mutations/mutations_sample";
import mutations_bowtie from "./mutations/mutations_bowtie";
import mutations_reference from "./mutations/mutations_reference";

import actions_project from "./actions/actions_project";
import actions_sample from "./actions/actions_sample";
import actions_user from "./actions/actions_user";
import actions_reference from "./actions/actions_reference";
import test from "./actions/test";

export default new Vuex.Store({
  state: {
    ...state_user,
    ...state_icons,
    ...state_project,
    ...state_task,
    ...state_sample,
    ...state_bowite,
    ...state_reference,
  },
  getters: {
    ...getters_project,
    ...getters_user,
    ...getters_reference,
    ...getters_sample,
  },
  mutations: {
    ...mutations_project,
    ...mutations_user,
    ...mutations_task,
    ...mutations_sample,
    ...mutations_bowtie,
    ...mutations_reference,
  },
  actions: {
    ...actions_project,
    ...actions_user,
    ...actions_reference,
    ...actions_sample,
    ...test,
  },
  modules: {},
});
