<template>
    <div class="page-wrapper">
        <div class="share-food-wrapper">
            <div class="share-food-title">
                Добавить предприятие
            </div>
            <div class="share-food-form-wrapper">
                <el-button
                        class="save-button"
                        @click="saveForm"
                >
                    Сохранить
                </el-button>
                <el-form
                        ref="form"
                        :model="formModel"
                        :rules="formValidationRules"
                >
                    <el-form-item
                            label="Тип продукта:"
                            prop="industryType"
                    >
                        <el-select
                                v-model="formModel.industryType"
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
                            label="Название предприятия:"
                            prop="name"
                    >
                        <el-input
                                placeholder="Введите название"
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
                            label="Адрес:"
                    >
                        <el-input
                                type="textarea"
                                placeholder="Введите адрес"
                                v-model="formModel.adress"
                        />
                    </el-form-item>
                    <el-form-item>
                        <div class="coordinate-form-wrapper">
                            <el-form-item
                                    class="coordinate-x"
                                    label="Широта:"
                            >
                                <el-input
                                        placeholder="Введите значение"
                                        v-model="formModel.coordinateX"
                                        style="width: 100%"
                                />
                            </el-form-item>
                            <el-form-item
                                    class="coordinate-y"
                                    label="Долгота:">
                                <el-input
                                        placeholder="Введите значение"
                                        v-model="formModel.coordinateY"
                                        style="width: 100%"
                                />
                            </el-form-item>
                        </div>
                        <div class="help-message">
                        <span>
                            Координаты необходимы для отображения предприятия на картах.
                        </span>
                            <el-link
                                    href="https://www.google.ru/maps/@54.1954174,37.6101058,12.75z"
                                    target="_blank"
                                    style="font-size: 14px; margin: 0; text-decoration: none;"
                            >Открыть Google Maps для получения координат.
                            </el-link>
                        </div>
                    </el-form-item>
                    <el-form-item
                            label="Описание:"
                    >
                        <el-input
                                type="textarea"
                                placeholder="Введите значение"
                                v-model="formModel.note"
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
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AddIndustry",
        data() {
            return {
                formModel: {
                    name: '',
                    industryType: '',
                    adress: '',
                    phone: '',
                    coordinateX: '',
                    coordinateY: '',
                    note: '',
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
                    industryType: {
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