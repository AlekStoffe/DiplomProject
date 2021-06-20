<template>
    <div
        v-loading="pageIsLoading"
        class="page-wrapper"
    >
        <div class="share-food-wrapper">
            <div class="share-food-title">
                Добавление профиля
            </div>
            <div class="share-food-form-wrapper">
                <el-form v-model="formModel">
                    <el-form-item label="Тип профиля">
                        <el-select
                            v-model="formModel.company_type"
                            placeholder="Выберите тип предприятия"
                            style="width: 100%"
                        >
                            <el-option
                                v-for="item in industryTypeList"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            />
                        </el-select>
                    </el-form-item>
                </el-form>
                <el-form
                    ref="form"
                    :model="formModel"
                    :rules="formValidationRules"
                >
                    <el-form-item
                        label="Название:"
                        prop="name"
                    >
                        <el-input
                            placeholder="Введите название"
                            v-model="formModel.name"
                        />
                    </el-form-item>
                    <el-form-item
                        label="Номер телефона:"
                        prop="telephone"
                    >
                        <el-input
                            placeholder="Введите номер"
                            v-model="formModel.telephone"
                        />
                    </el-form-item>
                    <el-form-item
                        label="Адрес электронной почты:"
                        prop="email"
                    >
                        <el-input
                            type="textarea"
                            placeholder="Введите email"
                            v-model="formModel.email"
                        />
                    </el-form-item>
                    <el-form-item v-if="formIsAddPerson">
                        <div class="coordinate-form-wrapper">
                            <el-form-item
                                class="coordinate-x"
                                label="Широта:"
                            >
                                <el-input
                                    placeholder="Введите значение"
                                    v-model="formModel.lat"
                                    style="width: 100%"
                                />
                            </el-form-item>
                            <el-form-item
                                class="coordinate-y"
                                label="Долгота:">
                                <el-input
                                    placeholder="Введите значение"
                                    v-model="formModel.lon"
                                    style="width: 100%"
                                />
                            </el-form-item>
                        </div>
                        <div class="help-message">
                        <span>
                            Координаты необходимы для отображения предприятия на картах.
                        </span>
                            <el-link
                                href="https://www.google.ru/maps/@54.1850893,37.6239075,12.79z"
                                target="_blank"
                                style="font-size: 14px; margin: 0; text-decoration: none;"
                            >Открыть Google Maps для получения координат.
                            </el-link>
                        </div>
                    </el-form-item>
                    <el-form-item
                        v-if="formIsAddPerson"
                        label="Адрес:"
                    >
                        <el-input
                            type="textarea"
                            placeholder="Введите адрес"
                            v-model="formModel.address"
                        />
                    </el-form-item>
                    <el-form-item
                        v-if="formIsAddPerson"
                        label="Описание:"
                    >
                        <el-input
                            type="textarea"
                            placeholder="Введите значение"
                            v-model="formModel.description"
                        />
                    </el-form-item>
                    <el-upload
                        ref="upload"
                        action="dummy"
                        class="upload-field"
                        :auto-upload="false"
                        :on-exceed="handleExceed"
                        :limit="limit"
                    >
                        <el-button size="small" type="primary">Загрузить фотографию профиля</el-button>
                    </el-upload>
                </el-form>
                <el-button
                    class="save-button"
                    @click="createProfile"
                >
                    Сохранить
                </el-button>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import {industryTypes} from './industryEnums/selectIndustryTypeEnum.js';

export default {
    name: "AddIndustry",
    data() {
        return {
            formModel: {
                company_type: '11',
                name: '',
                email: '',
                address: '',
                telephone: '',
                lat: '',
                lon: '',
                description: '',
            },
            dialogImageUrl: '',
            dialogVisible: false,
            limit: 1,
            formValidationRules: {
                company_type: {
                    required: true,
                    message: 'Поле обязательно для заполнения',
                },
                name: {
                    required: true,
                    message: 'Поле обязательно для заполнения',
                },
                telephone: {
                    required: true,
                    message: 'Поле обязательно для заполнения',
                },
                email: [
                    {
                        required: true,
                        type: 'email',
                        message: 'Поле обязательно для заполнения',
                        trigger: 'blur',
                    },
                    {
                        type: 'email',
                        message: 'Введите корректный адрес электронной почты',
                        trigger: ['blur', 'change']
                    },
                ],
            },
        };
    },
    computed: {
        ...mapState([
            'pageIsLoading',
        ]),

        formIsAddPerson() {
            return !(this.formModel.company_type === '11');
        },
        industryTypeList() {
            return industryTypes;
        }
    },
    methods: {
        handleExceed() {
            this.$message.warning(`Можно загрузить только 1 изображение.`);
        },
        createProfile() {
            const dataForCreate = {
                ...this.formModel,
                image: this.$refs.upload.uploadFiles[0] === undefined ? {} : this.$refs.upload.uploadFiles[0].raw,
                user: localStorage.userId
            };
            let formData = new FormData()
            Object.keys(dataForCreate).forEach(key => formData.append(key, dataForCreate[key]))
            this.$refs.form.validate((valid) => {
                if (valid) {
                    this.$store.dispatch('createProfile', formData)
                        .then(() => {
                            this.$message({
                                type: 'success',
                                message: 'Профиль успешно создан.',
                            })
                            this.$router.push('/industries')
                        })
                        .catch(() => {
                            this.$message({
                                type: 'error',
                                message: 'Ошибка создания профиля.',
                            })
                        })
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