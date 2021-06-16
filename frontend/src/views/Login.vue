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
        <v-card-title class="center">Login</v-card-title>
        <v-text-field
          v-model="email"
          :rules="[rules.required, rules.emailRule]"
          label="Email"
          required
        ></v-text-field>

        <v-text-field
          v-model="password"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show ? 'text' : 'password'"
          name="input-10-1"
          label="Password"
          hint="At least 8 characters"
          counter
          @click:append="show = !show"
        ></v-text-field>
        <v-btn dark color="blue-grey" @click="login">Login</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    login() {
      if (this.$refs.form.validate()) {
        const authUrl = "http://localhost:5000/api/auth/";
        const usernamePasswordBuffer = Buffer.from(
          this.email + ":" + this.password
        );

        axios
          .get(authUrl, {
            headers: {
              "Content-Type": "aplication/json",
              Authorization: `Basic ${usernamePasswordBuffer.toString(
                "base64"
              )}`,
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
      }
    },
  },
  data() {
    return {
      show: false,
      email: "",
      password: "",
      alert: false,
      error: "",
      rules: {
        required: (v) => !!v || "Required.",
        min: (v) => v.length >= 8 || "Min 8 characters",
        emailRule: (v) => /.+@.+/.test(v) || "E-mail must be valid",
      },
    };
  },
};
</script>

<style>
</style>