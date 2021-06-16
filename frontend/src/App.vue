<template>
  <v-app>
    <v-app-bar app color="blue-grey darken-2" flat dark>
      <v-app-bar-nav-icon
        @click="drawer = true"
        v-if="user"
      ></v-app-bar-nav-icon>

      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 mr-4 hidden-md-and-down"
          contain
          min-width="100"
          src="./assets/img/logo-nav.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn to="/" text>
        <span class="mr-2">Home</span>
      </v-btn>
      <v-btn to="/courses" text>
        <span class="mr-2">Courses</span>
      </v-btn>
      <v-btn to="/login" text v-if="!user">
        <span class="mr-2">Login</span>
      </v-btn>
      <v-btn to="/register" text v-if="!user">
        <span class="mr-2">Register</span>
      </v-btn>
      <v-btn text v-else>
        <span class="mr-2" @click="logout">Logout</span>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group class="text-center">
          <v-list-item>
            <v-avatar>
              <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
            </v-avatar>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>{{
              user ? `${user.first_name} ${user.last_name}` : ""
            }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>

        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
          class="mt-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>My Courses</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  computed: {
    user() {
      return this.$store.state.user;
    },
  },
  methods: {
    async logout() {
      localStorage.setItem("token", "");
      localStorage.setItem("publicId", "");

      this.$router.push("/").catch(() => {});
    },
  },
  data: () => ({
    drawer: false,
    group: null,
  }),
  async mounted() {
    await this.$store.dispatch("fetchUser");
    console.log("here");
  },
};
</script>
