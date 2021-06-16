<template>
  <v-card>
    <v-tabs align-with-title>
      <v-tabs-slider color="blue-grey"></v-tabs-slider>

      <v-tab>Couses</v-tab>
      <v-tab>Users</v-tab>
      <v-tab>Instructors</v-tab>

      <v-tab-item>
        <CoursesTable />
      </v-tab-item>
      <v-tab-item>
        <h1>Users</h1>
      </v-tab-item>
      <v-tab-item>
        <h1>Instructors</h1>
      </v-tab-item>
    </v-tabs>
  </v-card>
</template>

<script>
import CoursesTable from "../components/CoursesTable.vue";
export default {
  components: {
    CoursesTable,
  },
};
</script>

<style>
</style>