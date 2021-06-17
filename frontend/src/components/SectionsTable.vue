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
      <v-select
        v-model="selectedChapter"
        :items="chapters"
        item-text="title"
        item-value="id"
        label="Chapter"
        return-object
        single-line
        class="mr-12"
        @input="fetchSections"
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
        v-if="selectedChapter"
        >Add Section</v-btn
      >
    </v-card-title>
    <v-data-table :headers="headers" :items="sections" :search="search">
    </v-data-table>

    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
      fullscreen
      hide-overlay
    >
      <v-card>
        <v-toolbar dark color="blue-grey darken-1">
          <v-btn icon dark @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Create new section</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark text @click="save"> Save </v-btn>
          </v-toolbar-items>
        </v-toolbar>

        <v-form class="mx-12 mt-5" ref="form">
          <v-text-field
            label="Title*"
            :rules="[rules.required]"
            v-model="title"
          ></v-text-field>
          <v-text-field
            label="Section Number*"
            :rules="[rules.required]"
            v-model="section_number"
            type="number"
          ></v-text-field>
          <ckeditor
            :editor="editor"
            v-model="editorData"
            :config="editorConfig"
          ></ckeditor>
        </v-form>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import axios from "axios";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

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
    fetchSections() {
      const url = `http://localhost:5000/api/courses/${this.selectedCourse["id"]}/chapters/${this.selectedChapter["id"]}/sections`;
      axios
        .get(url)
        .then((res) => {
          this.sections = res.data.sections;
        })
        .catch((e) => {
          console.log(e);
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
      if (this.$refs.form.validate() && this.editorData) {
        const url = `http://localhost:5000/api/courses/${this.selectedCourse["id"]}/chapters/${this.selectedChapter["id"]}/sections`;
        axios
          .post(
            url,
            {
              title: this.title,
              section_number: this.section_number,
              content: this.editorData,
            },
            {
              headers: {
                "x-access-token": this.$store.state["x-access-token"],
              },
            }
          )
          .then((res) => {
            this.fetchSections();
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
      section_number: "",
      error: "",
      alert: false,
      courses: [],
      chapters: [],
      sections: [],
      selectedCourse: null,
      selectedChapter: null,
      search: "",
      editor: ClassicEditor,
      editorData: "",
      editorConfig: {},
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
          text: "Section Number",
          value: "section_number",
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