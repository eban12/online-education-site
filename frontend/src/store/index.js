import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    "x-access-token": ""
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },

    setToken(state, token) {
      state["x-access-token"] = token;
    }
  },
  actions: {
    fetchToken(context) {
      let token = localStorage.getItem("token");
      context.commit("setToken", token);
    },

    async fetchUser(context) {
      context.dispatch("fetchToken");
      const publicId = localStorage.getItem("publicId");
      const url = `http://localhost:5000/api/users/${publicId}`;
      try {
        const res = await axios.get(url, {
          headers: {
            "x-access-token": context.state["x-access-token"]
          }
        });
        context.commit("setUser", res.data.user);
      } catch (error) {
        context.commit("setUser", null);
      }
    }
  },
  modules: {}
});
