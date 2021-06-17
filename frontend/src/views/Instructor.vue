<template>
  <v-card>
    <v-tabs align-with-title>
      <v-tabs-slider color="blue-grey"></v-tabs-slider>

      <v-tab>Chapters</v-tab>
      <v-tab>Sections</v-tab>

      <v-tab-item>
        <ChaptersTable />
      </v-tab-item>
      <v-tab-item>
        <SectionsTable />
      </v-tab-item>
    </v-tabs>
  </v-card>
</template>

<script>
import ChaptersTable from "../components/ChaptersTable.vue";
import SectionsTable from "../components/SectionsTable.vue";

export default {
  components: {
    ChaptersTable,
    SectionsTable,
  },
};
</script>