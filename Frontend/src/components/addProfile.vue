<template>
  <div class="page-wrapper">
    <div class="share-food-wrapper">
      <div class="share-food-title">
        Добавление профиля
      </div>
      <div class="share-food-form-wrapper">
        <el-radio v-model="formModel.profile_type" :label="true">Частное лицо</el-radio>
        <el-radio v-model="formModel.profile_type" :label="false">Юридическое лицо</el-radio>
        <person-form ref="form" v-if="formModel.profile_type"/>
        <company-form ref="form" v-if="!formModel.profile_type"/>
        <el-button
            class="save-button"
            @click="saveForm"
        >
          Сохранить
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import PersonForm from './personForm.vue';
import CompanyForm from './companyForm.vue';

export default {
  name: "AddIndustry",
  components: {
    PersonForm,
    CompanyForm,
  },
  data() {
    return {
      formModel: {
        profile_type: true,
      },
    };
  },
  methods: {
    saveForm() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          alert('OK');
          return;
        }
        return false;
      })
    },
  },
}
</script>

<style scoped lang="scss">
.page-wrapper {
  height: 908px;
  overflow: scroll;
  overflow-x: hidden;
}

.share-food-wrapper {
  width: 50%;
  margin: 15px auto;
  text-align: center;
}

.share-food-form-wrapper {
  width: 600px;
  margin: 0 auto;
}

.share-food-title {
  font-size: 30px;
  margin-bottom: 20px;
}

.upload-field {
  height: 80px;
}

.coordinate-form-wrapper {
  display: flex;
  width: 100%;
}

.coordinate-x {
  margin-right: 200px;
}

.save-button {
  padding: 15px 50px;
}

.help-message {
  text-decoration: none;
  margin-top: 10px;
  font-size: 12px;
  color: darkgray;
  width: 100%;
  text-align: left;
  line-height: 20px;
}
</style>