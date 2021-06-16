<template>
  <v-container class="mx-auto mt-5" justify="center">
    <v-alert
      v-model="alert"
      dismissible
      dense
      outlined
      type="error"
      max-width="500"
      class="mx-auto"
    >
      {{ error }}
    </v-alert>
    <v-card max-width="400" class="mx-auto mt-12 p-4">
      <v-form class="mx-auto" ref="form">
        <v-card-title class="center">Register</v-card-title>
        <v-text-field
          v-model="first_name"
          :rules="[rules.required]"
          label="First name"
          required
        ></v-text-field>

        <v-text-field
          v-model="last_name"
          :rules="[rules.required]"
          label="Last name"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          :rules="[rules.required, rules.emailRule]"
          label="Email"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show ? 'text' : 'password'"
          name="input-10-1"
          label="Password"
          hint="At least 8 characters"
          counter
          @click:append="show = !show"
        ></v-text-field>
        <v-btn dark color="blue-grey" @click="signup">Sign Up</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  methods: {
    login() {
      const authUrl = "http://localhost:5000/api/auth/";
      const usernamePasswordBuffer = Buffer.from(
        this.email + ":" + this.password
      );

      axios
        .get(authUrl, {
          headers: {
            "Content-Type": "aplication/json",
            Authorization: `Basic ${usernamePasswordBuffer.toString("base64")}`,
          },
        })
        .then((res) => {
          localStorage.setItem("token", res.data.token);
          this.$router.push("/");
        })
        .catch((e) => {
          if (e.response.status === 401) {
            this.error = "Invalid email and/or password!";
            this.alert = true;
          } else {
            this.error = "Something went wrong!";
            this.alert = true;
          }
        });
    },

    signup() {
      if (this.$refs.form.validate()) {
        const usersUrl = "http://localhost:5000/api/users/";

        axios
          .post(usersUrl, {
            first_name: this.first_name,
            last_name: this.last_name,
            email: this.email,
            password: this.password,
          })
          .then((res) => {
            this.login();
          })
          .catch((e) => {
            this.error = e.response.data;
            this.alert = true;
          });
      }
    },
  },
  data() {
    return {
      show: false,
      password: "",
      email: "",
      first_name: "",
      last_name: "",
      error: "",
      alert: false,
      rules: {
        required: (v) => !!v || "Required.",
        min: (v) => v.length >= 8 || "Min 8 characters",
        emailRule: (v) => /.+@.+/.test(v) || "E-mail must be valid",
      },
    };
  },
};
</script>