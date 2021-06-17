<template>
  <v-container class="grey lighten-5 mt-8">
    <v-row justify="space-between" no-gutters style="height: 150px">
      <v-col
        v-for="course in courses"
        :key="course.id"
        width="30%"
        class="mb-3"
      >
        <CourseCard :course="course" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HelloWorld from "../components/HelloWorld";
import CourseCard from "../components/CourseCard.vue";
import axios from "axios";

export default {
  name: "Home",

  components: {
    HelloWorld,
    CourseCard,
  },
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
  },
  data() {
    return {
      courses: [],
    };
  },
  mounted() {
    this.fetchCourses();
  },
};
</script>
