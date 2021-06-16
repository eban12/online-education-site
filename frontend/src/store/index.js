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

    fetchUser(context) {
      context.dispatch("fetchToken");
      const publicId = localStorage.getItem("publicId");
      const url = `http://localhost:5000/api/users/${publicId}`;
      axios
        .get(url, {
          headers: {
            "x-access-token": context.state["x-access-token"]
          }
        })
        .then(res => {
          context.commit("setUser", res.data.user);
        })
        .catch(e => {
          context.commit("setUser", null);
        });
    }
  },
  modules: {}
});
