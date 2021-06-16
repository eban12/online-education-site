<template>
  <v-card max-width="400" class="mx-auto mt-12 p-4">
    <v-form class="mx-auto">
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
      <v-btn dark color="blue-grey">Sign Up</v-btn>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      password: "",
      email: "",
      first_name: "",
      last_name: "",
      rules: {
        required: (v) => !!v || "Required.",
        min: (v) => v.length >= 8 || "Min 8 characters",
        emailRule: (v) => /.+@.+/.test(v) || "E-mail must be valid",
      },
    };
  },
};
</script>