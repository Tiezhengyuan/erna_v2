import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);

import HomePage from "../views/HomePage";
import SampleManagement from "../views/SampleManagement";
import RNAseqPipeline from "../views/RNAseqPipeline";
import AnalyticTools from "../views/AnalyticTools";

import CreateProject from "../views/project/CreateProject";
import UpdateProjects from "../views/project/UpdateProjects";
import ParseSamples from "../views/sample/ParseSamples";
import BuildReference from "../views/reference/BuildReference";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/manage",
    name: "manage",
    component: SampleManagement,
    children: [
      {
        path: "create_project",
        name: "create_project",
        component: CreateProject,
      },
      {
        path: "update_projects",
        name: "update_projects",
        component: UpdateProjects,
      },
      {
        path: "parse_samples",
        name: "parse_samples",
        component: ParseSamples,
      },
      {
        path: "build_reference",
        name: "build_reference",
        component: BuildReference,
      },
    ],
  },
  {
    path: "/rnaseq",
    name: "rnaseq",
    component: RNAseqPipeline,
  },
  {
    path: "/tools",
    name: "tools",
    component: AnalyticTools,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
