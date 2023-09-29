import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true;
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

axios.interceptors.response.use((res) => {
  res.headers["Access-Control-Allow-Origin"] = "*";
  res.headers["Access-Control-Allow-Credentials"] = "true";
  res.headers["Access-Control-Request-Method"] = "POST";
  return res;
});

export const api = axios.create({
  baseURL: "/api/",
  // withCredentials: false,
  headers: {
    ContentType: "application/json",
    Accept: "application/json",
  },
  auth: {
    username: "admin",
    password: "admin",
  },
  transformResponse(res) {
    try {
      return JSON.parse(res);
    } catch (e) {
      return res;
    }
  },
});

export const test_api = axios.create({
  baseURL: "https://yesno.wtf/api",
  transformResponse(res) {
    res = JSON.parse(res);
    return res;
  },
});

export const smartscope_api = axios.create({
  baseURL: "https://viewer.smartscope.org/api/",
  headers: {
    Authorization: "token 9e857ca09d2498f1a10231eb5a9dddd186c95dcf",
  },
  transformResponse(res) {
    res = JSON.parse(res);
    return res;
  },
});
