<template>
  <v-card
    max-width="350"
    outlined
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >
      <v-card-title>{{ course.name }}</v-card-title>
    </v-img>

    <v-card-actions>
      <v-btn
        color="orange"
        text
        :to="`/course/${course.id}`"
      >
        Take Course
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
      name: 'CourseCard',
      props: ['course']
  }
</script>


