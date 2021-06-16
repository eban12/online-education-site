import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Register from "../views/Register.vue";
import Course from "../views/Course.vue";
import Login from "../views/Login.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
    path: "/login",
    name: "login",
    // route level code-
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited
    component: Login
  },
  {
    path: "/register",
    name: "register",
    // route level code-
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited
    component: Register
  },
  {
    path: "/course/:id",
    name: "course",
    // route level code-
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited
    component: Course
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
