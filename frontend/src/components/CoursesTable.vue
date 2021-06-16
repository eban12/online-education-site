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
      <v-btn color="success" class="ml-4" @click="openModal">Add Course</v-btn>
    </v-card-title>
    <v-data-table :headers="headers" :items="courses" :search="search">
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
                    label="Course name*"
                    :rules="[required]"
                    v-model="courseName"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea
                    rows="3"
                    label="Description"
                    v-model="courseDesc"
                  ></v-textarea>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Course image"
                    v-model="courseImage"
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-select
                    :items="instructors"
                    label="Instructors"
                    multiple
                    v-model="courseInstructors"
                  ></v-select>
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
          <v-btn color="blue darken-1" text @click="saveCourse"> Save </v-btn>
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
      this.modalTitle = "Add new course";
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
    saveCourse() {
      if (this.$refs.form.validate()) {
        const url = "http://localhost:5000/api/courses/";
        axios
          .post(
            url,
            {
              name: this.courseName,
              description: this.courseDesc,
              course_image: this.courseImage,
            },
            {
              headers: {
                "x-access-token": this.$store.state["x-access-token"],
              },
            }
          )
          .then((res) => {
            this.fetchCourses();
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
      modalTitle: "Add new course",
      search: "",
      courseName: "",
      courseDesc: "",
      courseImage: "",
      courses: [],
      instructors: [],
      courseInstructors: "",
      required: (v) => !!v || "Required.",
      headers: [
        { text: "Id", align: "start", value: "id" },
        {
          text: "Name",
          value: "name",
        },
        { text: "Description", value: "description" },
      ],
    };
  },
  async mounted() {
    this.fetchCourses();
  },
};
</script>

<style>
</style>