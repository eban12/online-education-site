<template>
  <v-card>
    <v-card-title>
      <v-select
        v-model="selectedCourse"
        :items="courses"
        item-text="name"
        item-value="id"
        label="Course"
        return-object
        single-line
        class="mr-12"
        @input="fetchChapters"
      ></v-select>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
      <v-btn
        color="success"
        class="ml-4"
        @click="openModal"
        v-if="selectedCourse"
        >Add Chapter</v-btn
      >
    </v-card-title>
    <v-data-table :headers="headers" :items="chapters" :search="search">
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
                    v-model="title"
                    :rules="[rules.required]"
                    label="Title*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="chapter_number"
                    :rules="[rules.required]"
                    label="Chapter Number*"
                    type="number"
                    required
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
    fetchChapters() {
      const url = `http://localhost:5000/api/courses/${this.selectedCourse["id"]}/chapters`;
      axios
        .get(url)
        .then((res) => {
          this.chapters = res.data.chapters;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    openModal() {
      this.dialog = true;
    },
    save() {
      if (this.$refs.form.validate()) {
        const url = `http://localhost:5000/api/courses/${this.selectedCourse["id"]}/chapters/`;
        axios
          .post(
            url,
            {
              title: this.title,
              chapter_number: this.chapter_number,
            },
            {
              headers: {
                "x-access-token": this.$store.state["x-access-token"],
              },
            }
          )
          .then((res) => {
            this.fetchChapters();
            this.dialog = false;
          })
          .catch((e) => {
            console.log(e.response);
          });
      }
    },
  },
  data() {
    return {
      dialog: false,
      modalTitle: "Add new Instructor",
      show: false,
      title: "",
      chapter_number: "",
      error: "",
      alert: false,
      courses: [],
      chapters: [],
      selectedCourse: null,
      search: "",
      rules: {
        required: (v) => !!v || "Required.",
        min: (v) => v.length >= 8 || "Min 8 characters",
        emailRule: (v) => /.+@.+/.test(v) || "E-mail must be valid",
      },
      headers: [
        { text: "Id", align: "start", value: "id" },
        {
          text: "Title",
          value: "title",
        },
        {
          text: "Chapter Number",
          value: "chapter_number",
        },
      ],
    };
  },
  mounted() {
    this.fetchCourses();
  },
};
</script>

<style>
</style>