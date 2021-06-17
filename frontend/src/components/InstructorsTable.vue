<template>
  <v-card>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
      <v-btn color="success" class="ml-4" @click="openModal"
        >Add Instructor</v-btn
      >
    </v-card-title>
    <v-data-table :headers="headers" :items="instructors" :search="search">
    </v-data-table>

    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="text-h5">{{ modalTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-form ref="form">
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="first_name"
                    :rules="[rules.required]"
                    label="First name*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="last_name"
                    :rules="[rules.required]"
                    label="Last name*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="email"
                    :rules="[rules.required, rules.emailRule]"
                    label="Email*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="password"
                    :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="[rules.required, rules.min]"
                    :type="show ? 'text' : 'password'"
                    name="input-10-1"
                    label="Password*"
                    hint="At least 8 characters"
                    counter
                    @click:append="show = !show"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-form>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    openModal() {
      this.modalTitle = "Add new Instructor";
      this.dialog = true;
    },
    fetchCourses() {
      let url = "http://localhost:5000/api/courses";
      axios
        .get(url)
        .then((res) => {
          this.courses = res.data.courses;
        })
        .catch((e) => {
          console.log(e);
          return [];
        });
    },
    fetchInctructors() {
      let url = "http://localhost:5000/api/instructors/";
      axios
        .get(url, {
          headers: {
            "x-access-token": this.$store.state["x-access-token"],
          },
        })
        .then((res) => {
          this.instructors = res.data.instructors;
        })
        .catch((e) => {
          return [];
        });
    },
    save() {
      if (this.$refs.form.validate()) {
        let url = "http://localhost:5000/api/instructors/";
        axios
          .post(
            url,
            {
              first_name: this.first_name,
              last_name: this.last_name,
              email: this.email,
              password: this.password,
            },
            {
              headers: {
                "x-access-token": this.$store.state["x-access-token"],
              },
            }
          )
          .then((res) => {
            this.fetchInctructors();
            this.dialog = false;
          })
          .catch((e) => {
            return [];
          });
      }
    },
  },
  data() {
    return {
      dialog: false,
      modalTitle: "Add new Instructor",
      show: false,
      password: "",
      email: "",
      first_name: "",
      last_name: "",
      error: "",
      alert: false,
      courses: [],
      instructors: [],
      courseInstructors: "",
      rules: {
        required: (v) => !!v || "Required.",
        min: (v) => v.length >= 8 || "Min 8 characters",
        emailRule: (v) => /.+@.+/.test(v) || "E-mail must be valid",
      },
      headers: [
        { text: "Public Id", align: "start", value: "public_id" },
        {
          text: "First Name",
          value: "first_name",
        },
        {
          text: "Last Name",
          value: "last_name",
        },
        {
          text: "Email",
          value: "email",
        },
      ],
    };
  },
  async mounted() {
    this.fetchInctructors();
  },
};
</script>

<style>
</style>