<template>
  <v-card
    outlined
    class="p-3"
  >
      <v-row class="ml-3" justify="start">
        <v-col cols="1">
            <v-avatar
                size="36px"
                class="mx-0"
            >
                <img
                alt="Avatar"
                src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
                >
            </v-avatar>
        </v-col>
        <v-col class="ml-0">
            <strong v-html="comment.username"></strong>
        </v-col>
      </v-row>
      <v-card-text>
          {{ comment.text }}
      </v-card-text>
  </v-card>
</template>

<script>
export default {
    props: ['comment']
}
</script>
