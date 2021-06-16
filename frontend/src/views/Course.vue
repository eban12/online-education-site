<template>
<v-container>
    
  <v-navigation-drawer
    app
    left
  >
    <v-toolbar
      flat
    >
      <v-toolbar-title>Course Title</v-toolbar-title>
    </v-toolbar>
    <v-divider class="mt-1"></v-divider>
    <v-treeview
            v-model="tree"
            :load-children="fetch"
            :items="items"
            selected-color="indigo"
            open-on-click
            selectable
            activatable
            return-object
            expand-icon="mdi-chevron-down"
            on-icon="mdi-bookmark"
            off-icon="mdi-bookmark-outline"
            indeterminate-icon="mdi-bookmark-minus"
            @update:active="clickOnNode"
          >
    </v-treeview>
  </v-navigation-drawer>

  <v-container class="">
    <div v-html="htmlText"></div>
    <v-divider></v-divider>

    <div class="comment-form mx-12">
      <v-form v-model="valid">
        <v-textarea
          outlined
          rows="4"
          solo
          label="Comment"
          class="my-0"
          :rules="commentRules"
        ></v-textarea>
        <v-btn
          :disabled="!valid"
          color="blue-grey"
          dark
          class="ml-auto mr-2 my-0"
          @click="addComment"
        >
          Comment
        </v-btn>
      </v-form>

      <div class="comments mt-5">
        <CommentCard :comment="comment" v-for="comment in comments" :key="comment.id" class="mb-6"/>
      </div>
      
    </div>
  </v-container>

</v-container>
  
</template>

<script>
  import CommentCard from '../components/CommentCard.vue'

  export default {
    components: {
      CommentCard
    },
    methods: {
      clickOnNode(node) {
        this.section.text = `<h1>Now this is from section ${node[0]["id"]}</h1>`
      }
    },
    computed: {
      htmlText() {
        return this.section.text
      },
      comments() {
        return [{
          id: 1,
          username: "John Doe",
          text: "I like this course!"
        },
        {
          id: 2,
          username: "John Doe",
          text: "I like this course!"
        },
        {
          id: 3,
          username: "John Doe",
          text: "I like this course!"
        }]
      }
    },
    data: () => ({
      valid: false,
      section: {
        text: "This is the text for this section"
      },
      commentRules: [
        v => !!v || 'Name is required',
      ],
      items: [
        {
          id: 1,
          name: 'Applications :',
          children: [
            { id: 2, name: 'Calendar : app' },
            { id: 3, name: 'Chrome : app' },
            { id: 4, name: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          name: 'Documents :',
          children: [
            {
              id: 6,
              name: 'vuetify :',
              children: [
                {
                  id: 7,
                  name: 'src :',
                  children: [
                    { id: 8, name: 'index : ts' },
                    { id: 9, name: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              name: 'material2 :',
              children: [
                {
                  id: 11,
                  name: 'src :',
                  children: [
                    { id: 12, name: 'v-btn : ts' },
                    { id: 13, name: 'v-card : ts' },
                    { id: 14, name: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          name: 'Downloads :',
          children: [
            { id: 16, name: 'October : pdf' },
            { id: 17, name: 'November : pdf' },
            { id: 18, name: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          name: 'Videos :',
          children: [
            {
              id: 20,
              name: 'Tutorials :',
              children: [
                { id: 21, name: 'Basic layouts : mp4' },
                { id: 22, name: 'Advanced techniques : mp4' },
                { id: 23, name: 'All about app : dir' },
              ],
            },
            { id: 24, name: 'Intro : mov' },
            { id: 25, name: 'Conference introduction : avi' },
          ],
        },
      ],
    }),
  }
</script>
