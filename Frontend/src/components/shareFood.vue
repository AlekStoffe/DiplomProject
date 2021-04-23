<template>
    <div class="share-food-wrapper">
        <div class="share-food-title">
            Поделиться едой
        </div>
        <div class="share-food-form-wrapper">
            <el-form
                    ref="form"
                    :model="formModel"
                    :rules="formValidationRules"
            >
                <el-form-item
                        label="Тип продукта:"
                        prop="foodType"
                >
                    <el-select
                            v-model="formModel.foodType"
                            placeholder="Выберите тип продукта"
                            style="width: 100%"
                    >
                        <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                        />
                    </el-select>
                </el-form-item>
                <el-form-item
                        label="Название продукта:"
                        prop="name"
                >
                    <el-input
                            placeholder="Введите название"
                            size="50px"
                            v-model="formModel.name"
                            clearable
                    />
                </el-form-item>
                <el-form-item label="Срок годности:">
                    <el-input
                            placeholder="Введите срок годности"
                            size="50px"
                            v-model="formModel.expirationDate"
                            clearable
                    />
                </el-form-item>
                <el-form-item label="Количество:">
                    <el-input-number
                            placeholder="Введите количество"
                            v-model="formModel.count"
                            style="margin-right: 300px"
                            :min="1"
                    />
                </el-form-item>
                <el-form-item label="Цена:">
                    <el-input
                            placeholder="Введите количество"
                            v-model="formModel.price"
                    />
                </el-form-item>
                <el-upload
                        class="upload-field"
                        action="https://jsonplaceholder.typicode.com/posts/"
                        :on-preview="handlePictureCardPreview"
                        :on-remove="handleRemove"
                        :on-exceed="handleExceed"
                        :limit="limit"
                        :file-list="fileList"
                >
                    <el-button size="small" type="primary">Загрузить изображение продукта</el-button>
                </el-upload>
            </el-form>
            <el-button
                    class="save-button"
                    @click="saveForm"
            >
                Сохранить
            </el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ShareFood",
        data() {
            return {
                formModel: {
                    name: '',
                    foodType: '',
                    expirationDate: '',
                    count: '',
                    price: '',
                    image: '',
                },
                options: [{
                    value: 'Option1',
                    label: 'Option1'
                }, {
                    value: 'Option2',
                    label: 'Option2'
                }, {
                    value: 'Option3',
                    label: 'Option3'
                }, {
                    value: 'Option4',
                    label: 'Option4'
                }, {
                    value: 'Option5',
                    label: 'Option5'
                }],
                dialogImageUrl: '',
                dialogVisible: false,
                fileList: [],
                limit: 1,
                formValidationRules: {
                    foodType: {
                        required: true,
                        message: 'Поле обязательно для заполнения',
                    },
                    name: {
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

<style lang="scss" scoped>
    .share-food-wrapper {
        width: 50%;
        margin: 100px auto;
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

    .save-button {
        margin-top: 40px;
        padding: 15px 50px;
    }
</style>