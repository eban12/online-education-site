<template>
  <v-container
      class="grey lighten-5 mt-8"
  >
    <v-row
      justify="space-between"
      no-gutters
      style="height: 150px;"
    >
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
  import HelloWorld from '../components/HelloWorld'
  import CourseCard from '../components/CourseCard.vue'

  let courses = [
    {
      "id": 1,
      "name": "Fundamentals of Programming",
      "description": "I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape. "
    },
    {
      "id": 2,
      "name": "Fundamentals of Programming",
      "description": "I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape. "
    },
    {
      "id": 3,
      "name": "Fundamentals of Programming",
      "description": "I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape. "
    }
  ]

  export default {
    name: 'Home',

    components: {
      HelloWorld,
      CourseCard
    },
    data: () => ({
      courses
    })
  }
</script>
