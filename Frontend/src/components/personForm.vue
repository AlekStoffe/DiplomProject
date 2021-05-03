<template>
      <div class="share-food-form-wrapper">
        <el-form
            ref="form"
            :model="formModel"
            :rules="formValidationRules"
        >
          <el-form-item
              label="ФИО:"
              prop="name"
          >
            <el-input
                placeholder="Введите ФИО"
                v-model="formModel.name"
            />
          </el-form-item>
          <el-form-item
              label="Номер телефона:"
          >
            <el-input
                placeholder="Введите номер"
                v-model="formModel.phone"
            />
          </el-form-item>
          <el-form-item
              label="Адрес электронной почты:"
          >
            <el-input
                type="textarea"
                placeholder="Введите email"
                v-model="formModel.email"
            />
          </el-form-item>
          <el-upload
              class="upload-field"
              action="dummy"
              :auto-upload="false"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              :on-exceed="handleExceed"
              :limit="limit"
              :file-list="fileList"
          >
            <el-button size="small" type="primary">Загрузить изображение продукта</el-button>
          </el-upload>
        </el-form>
      </div>
</template>

<script>
export default {
  name: "Person",
  data() {
    return {
      formModel: {
        name: '',
        email: '',
        phone: '',
        image: '',
      },
      dialogImageUrl: '',
      dialogVisible: false,
      fileList: [],
      limit: 1,
      formValidationRules: {
        name: {
          required: true,
          message: 'Поле обязательно для заполнения',
        },
        email: {
          required: true,
          message: 'Поле обязательно для заполнения',
        },
        phone: {
          required: true,
          message: 'Поле обязательно для заполнения',
        },
      },
    };
  },
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleExceed() {
      this.$message.warning(`Можно загрузить только 1 изображение.`);
    },
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
.share-food-form-wrapper {
  width: 600px;
  margin: 0 auto;
}

.upload-field {
  height: 80px;
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