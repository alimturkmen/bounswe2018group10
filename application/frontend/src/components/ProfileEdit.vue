<template>
  <div>
    <NavigationBar/>

    <b-container>
      <h2>Edit {{isClient ? "Client":"Freelancer"}} Profile</h2>
      <b-form @submit="onSubmit">
        <b-form-row>
          <b-col cols="12" md="6">
            <div>Current Profile Picture</div>
            <b-img v-if="isClient" :src="clientAvatar" rounded width="160" alt="img" class="m-1"/>
            <b-img
              v-if="isFreelancer"
              :src="freelancerAvatar"
              rounded
              width="160"
              alt="img"
              class="m-1"
            />
            <b-form-group
              label="New Profile Picture"
              label-for="inputAvatar"
              description="You can drag and drop your profile picture to this input box."
            >
              <b-form-file
                v-if="isClient"
                id="inputAvatar"
                accept="image/*"
                v-model="clientForm.file"
                placeholder="Choose an image file..."
                ref="fileClientInput"
              ></b-form-file>
              <b-form-file
                v-if="isFreelancer"
                id="inputAvatar"
                accept="image/*"
                v-model="freelancerForm.file"
                placeholder="Choose an image file..."
                ref="fileFreelancerInput"
              ></b-form-file>
            </b-form-group>
            <b-form-group>
              <b-button v-if="isClient" @click="clearClientFiles" size="sm">Reset browsed image file</b-button>
              <b-button
                v-if="isFreelancer"
                @click="clearFreelancerFiles"
                size="sm"
              >Reset browsed image file</b-button>
            </b-form-group>
          </b-col>
          <b-col cols="12" md="6">
            <!--
            <b-form-group label="Name"
                          label-for="inputName">
              <b-form-input id="inputName"
                            type="text"
                            maxlength="255"
                            v-model="clientForm.name"
                            placeholder="Enter name"
                            required>
              </b-form-input>
            </b-form-group>-->
            <b-form-group label="Profile Body" label-for="inputBody">
              <b-form-textarea
                v-if="isClient"
                id="inputBody"
                v-model="clientForm.body"
                placeholder="Tell us about yourself"
                :rows="4"
                :max-rows="8"
                required
              ></b-form-textarea>
              <b-form-textarea
                v-if="isFreelancer"
                id="inputBody"
                v-model="freelancerForm.body"
                placeholder="Tell us about yourself"
                :rows="4"
                :max-rows="8"
                required
              ></b-form-textarea>
            </b-form-group>
          </b-col>
        </b-form-row>

        <b-button type="submit" variant="primary" block>
          <font-awesome-icon icon="save" fixed-width/>Save changes
        </b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import NavigationBar from "./NavigationBar.vue";

export default {
  name: "ProfileEdit",
  components: {
    NavigationBar
  },
  data() {
    return {
      clientAvatar: require("../assets/blank-profile-picture.svg"),
      freelancerAvatar: require("../assets/blank-profile-picture.svg"),
      clientForm: {
        //name: "",
        file: null,
        body: ""
      },
      freelancerForm: {
        //name: "",
        file: null,
        body: ""
      },
      clientProfileId: null,
      freelancerProfileId: null
      //firstProfile: false // if it is true the user does not have a profile, we should create a new one
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.$axios
        .get(`/user/clientprofile/?search=${this.$root.$data.user_id}`)
        .then(response => {
          let profile = response.data[0];
          this.clientProfileId = profile.id;
          //this.form.name = profileData.name;
          if (profile.avatar) {
            this.clientAvatar = profile.avatar;
          }
          this.clientForm.body = profile.body;
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
      this.$axios
        .get(`/user/freelancerprofile/?search=${this.$root.$data.user_id}`)
        .then(response => {
          let profile = response.data[0];
          this.freelancerProfileId = profile.id;
          //this.form.name = profileData.name;
          if (profile.avatar) {
            this.freelancerAvatar = profile.avatar;
          }
          this.freelancerForm.body = profile.body;
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      if (this.isClient) {
        this.onClientSubmit();
      } else {
        this.onFreelancerSubmit();
      }
    },
    onClientSubmit() {
      let formData = new FormData();
      //formData.append("name", this.form.name);
      formData.append("body", this.clientForm.body);
      if (this.clientForm.file) {
        formData.append(
          "avatar",
          this.clientForm.file,
          this.clientForm.file.name
        );
      }

      /*let method;
      let url;
      if (this.firstProfile) {
        method = "post";
        url = "/user/profile/";
      } else {
        method = "patch";
        url = `/user/profile/${this.profileId}/`;
      }*/

      this.$axios({
        method: "patch",
        url: `/user/clientprofile/${this.clientProfileId}/`,
        data: formData,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
        .then(() => {
          this.$router.push("/profile");
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
    },
    onFreelancerSubmit() {
      let formData = new FormData();
      //formData.append("name", this.form.name);
      formData.append("body", this.freelancerForm.body);
      if (this.freelancerForm.file) {
        formData.append(
          "avatar",
          this.freelancerForm.file,
          this.freelancerForm.file.name
        );
      }

      this.$axios({
        method: "patch",
        url: `/user/freelancerprofile/${this.freelancerProfileId}/`,
        data: formData,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
        .then(() => {
          this.$router.push("/profile");
        })
        .catch(err => {
          // eslint-disable-next-line
          console.log(err);
        });
    },
    clearClientFiles() {
      this.$refs.fileClientInput.reset();
    },
    clearFreelancerFiles() {
      this.$refs.fileFreelancerInput.reset();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
