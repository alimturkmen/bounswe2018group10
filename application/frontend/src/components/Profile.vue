<template>
  <div>
    <NavigationBar/>

    <b-container>
      <b-row>
        <b-col>
          <h2>My {{isClient ? "Client":"Freelancer"}} Profile</h2>
        </b-col>
        <b-col cols="auto">
          <b-button variant="primary" to="/profile-edit">
            <font-awesome-icon icon="user-edit" fixed-width/>Edit Profile
          </b-button>
        </b-col>
      </b-row>
      <b-row class="mb-4">
        <b-col cols="12" sm="2">
          <b-img v-if="isFreelancer" :src="freelancer.avatar" fluid rounded alt="img" class="m-1"/>
          <b-img v-if="isClient" :src="client.avatar" fluid rounded alt="img" class="m-1"/>
        </b-col>
        <b-col cols="12" sm="7">
          <h4>{{name}}</h4>
          <p v-if="isFreelancer">{{freelancer.body}}</p>
          <p v-if="isClient">{{client.body}}</p>
          <!--<p>Rating: {{rating}}</p>-->
        </b-col>
        <b-col cols="12" sm="3">
          <!--<b-card no-body header="<b>Skills</b>">
              <b-list-group flush>
                <b-list-group-item href="#">Java</b-list-group-item>
                <b-list-group-item href="#">Python</b-list-group-item>
                <b-list-group-item href="#">Javascript</b-list-group-item>
              </b-list-group>
          </b-card>-->
        </b-col>
      </b-row>

      <b-row class="mb-4">
        <b-col>
          <b-list-group v-show="isClient">
            <b-list-group-item>
              <b-row>
                <b-col>
                  <h5 class="mb-0">Comments ({{clientComments.length}})</h5>
                </b-col>
              </b-row>
            </b-list-group-item>
            <b-list-group-item :key="index" v-for="(comment,index) in clientComments">
              <b-row>
                <b-col md=2 lg=1>
                  <b-img left :src="comment.commenter_avatar ? comment.commenter_avatar : blankProfilePic" fluid rounded width="96" class="m-1"/>
                </b-col>
                <b-col md="10" lg="11">
                  <b-row>
                    <b-col>
                      <div>
                        <router-link :to="`/profile/${comment.user_id.id}`">
                          <strong>{{comment.user_id.name}}</strong>
                        </router-link>
                      </div>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      <p class="mb-0">{{comment.description}}</p>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      <small class="text-muted" v-b-tooltip.hover.bottom="$moment(comment.created_at).format('LLLL')">
                        {{comment.created_at | moment("from") }}
                      </small>
                    </b-col>
                  </b-row>
                </b-col>
              </b-row>
            </b-list-group-item>
          </b-list-group>

          <b-list-group v-show="isFreelancer">
            <b-list-group-item>
              <b-row>
                <b-col>
                  <h5 class="mb-0">Comments ({{freelancerComments.length}})</h5>
                </b-col>
              </b-row>
            </b-list-group-item>
            <b-list-group-item :key="index" v-for="(comment,index) in freelancerComments">
              <b-row>
                <b-col md=2 lg=1>
                  <b-img left :src="comment.commenter_avatar ? comment.commenter_avatar : blankProfilePic" fluid rounded width="96" class="m-1"/>
                </b-col>
                <b-col md="10" lg="11">
                  <b-row>
                    <b-col>
                      <div>
                        <router-link :to="`/profile/${comment.user_id.id}`">
                          <strong>{{comment.user_id.name}}</strong>
                        </router-link>
                      </div>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      <p class="mb-0">{{comment.description}}</p>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      <small class="text-muted" v-b-tooltip.hover.bottom="$moment(comment.created_at).format('LLLL')">
                        {{comment.created_at | moment("from") }}
                      </small>
                    </b-col>
                  </b-row>
                </b-col>
              </b-row>
            </b-list-group-item>
          </b-list-group>
        </b-col>
      </b-row>



    </b-container>
  </div>
</template>

<script>
import NavigationBar from "./NavigationBar.vue";

export default {
  name: "Profile",
  components: {
    NavigationBar
  },
  data() {
    return {
      blankProfilePic: require("../assets/blank-profile-picture.svg"),
      freelancer: {
        body: "",
        avatar: require("../assets/blank-profile-picture.svg")
      },
      client: {
        body: "",
        avatar: require("../assets/blank-profile-picture.svg")
      },
      name: "",
      rating: 0,
      clientComments: [],
      freelancerComments: [],
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.$axios
        .get(`/user/freelancerprofile/?search=${this.$root.$data.user_id}`)
        .then(response => {
          let profile = response.data[0];
          this.freelancer.body = profile.body;
          if (profile.avatar) {
            this.freelancer.avatar = profile.avatar;
          }
          this.name = profile.user.name;
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
      this.$axios
        .get(`/user/clientprofile/?search=${this.$root.$data.user_id}`)
        .then(response => {
          let profile = response.data[0];
          this.client.body = profile.body;
          if (profile.avatar) {
            this.client.avatar = profile.avatar;
          }
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
      this.$axios
        .get(`/comment/client/?search=${this.$root.$data.user_id}`)
        .then(response => {
          this.clientComments = response.data;
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
      this.$axios
        .get(`/comment/freelancer/?search=${this.$root.$data.user_id}`)
        .then(response => {
          this.freelancerComments = response.data;
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
