<template>
  <v-container>
    <v-navigation-drawer app left>
      <v-toolbar flat>
        <v-toolbar-title>{{ course.name }}</v-toolbar-title>
      </v-toolbar>
      <v-divider class="mt-1"></v-divider>
      <v-treeview
        v-model="tree"
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
      <div v-html="section.content"></div>
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
          >
            Comment
          </v-btn>
        </v-form>

        <div class="comments mt-5">
          <CommentCard
            :comment="comment"
            v-for="comment in comments"
            :key="comment.id"
            class="mb-6"
          />
        </div>
      </div>
    </v-container>
  </v-container>
</template>

<script>
import CommentCard from "../components/CommentCard.vue";
import axios from "axios";

export default {
  components: {
    CommentCard,
  },
  methods: {
    fetchCourse() {
      const url = `http://localhost:5000/api/courses/${this.$route.params.id}`;
      axios
        .get(url)
        .then((res) => {
          this.course = res.data.course;
          this.section = res.data.course.chapters[0].sections[0];
          this.items = res.data.course.chapters.map((c) => {
            return {
              id: c.id,
              name: c.title,
              children: c.sections.map((s) => {
                return {
                  id: `${s.id} ${c.id}`,
                  name: s.title,
                };
              }),
            };
          });
        })
        .catch((e) => {
          console.log(e);
          return [];
        });
    },
    clickOnNode(node) {
      const ids = node[0]["id"].split(" ");
      console.log(ids);
      let chapter = this.course.chapters.filter(
        (c) => c["id"] == Number(ids[1])
      )[0];

      this.section = chapter.sections.filter((s) => s.id === Number(ids[0]))[0];
    },
  },
  computed: {
    htmlText() {
      return this.section.content;
    },
    comments() {
      return [
        {
          id: 1,
          username: "John Doe",
          text: "I like this course!",
        },
        {
          id: 2,
          username: "John Doe",
          text: "I like this course!",
        },
        {
          id: 3,
          username: "John Doe",
          text: "I like this course!",
        },
      ];
    },
  },
  data() {
    return {
      tree: "",
      course: null,
      valid: false,
      section: null,
      commentRules: [(v) => !!v || "Name is required"],
      items: [],
    };
  },
  mounted() {
    this.fetchCourse();
  },
};
</script>
