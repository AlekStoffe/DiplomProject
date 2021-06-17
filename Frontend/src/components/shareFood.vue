<template>
    <el-container style="height: 908px; overflow: auto">
        <div
            v-loading="pageIsLoading"
            class="share-food-wrapper"
        >
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
                        label="Выберит профиль, от лица которого хотите добавить продукт:"
                        prop="company"
                    >
                        <el-select
                            v-model="formModel.company"
                            placeholder="Выберите тип продукта"
                            style="width: 100%"
                        >
                            <el-option
                                v-for="item in myProfiles"
                                :key="item.id"
                                :label="item.name"
                                :value="item.id"
                            />
                        </el-select>
                    </el-form-item>
                    <el-form-item
                        label="Тип продукта:"
                        prop="food_type"
                    >
                        <el-select
                            v-model="formModel.food_type"
                            placeholder="Выберите тип продукта"
                            style="width: 100%"
                        >
                            <el-option
                                v-for="item in foodTypeList"
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
                    <el-form-item label="Количество:">
                        <el-input-number
                            placeholder="Введите количество"
                            v-model="formModel.quantity"
                            style="margin-right: 300px"
                            :min="1"
                        />
                    </el-form-item>
                    <el-form-item label="Цена:">
                        <el-input
                            placeholder="Введите количество"
                            v-model="formModel.old_price"
                        >
                            <template slot="append">Руб</template>
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Скидка:">
                        <el-input
                            placeholder="Введите количество"
                            v-model="sale"
                            @change.native="_calculateNewPrice"
                        >
                            <template slot="append">%</template>
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Новая цена:">
                        <el-input
                            placeholder="Введите количество"
                            v-model="formModel.price"
                            disabled
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
                        <el-button size="small" type="primary">Загрузить изображение продукта</el-button>
                    </el-upload>
                </el-form>
                <el-button
                    class="save-button"
                    @click="createFood"
                >
                    Сохранить
                </el-button>
            </div>
        </div>
    </el-container>
</template>

<script>
import {mapState} from 'vuex';
import {foodTypes} from './foodEnums/selectFoodTypeEnum.js';

export default {
    name: "ShareFood",
    data() {
        return {
            defaultFormModel: {
                company: '',
                name: '',
                food_type: '',
                quantity: '',
                old_price: '',
                price: '',
            },
            sale: '',
            formModel: {},
            dialogVisible: false,
            limit: 1,
            formValidationRules: {
                company: {
                    required: true,
                    message: 'Поле обязательно для заполнения',
                },
                food_type: {
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
    mounted() {
        this.fillFormModel();
        this.$store.dispatch('fetchMyProfiles', {user: localStorage.userId})
            .catch(() => this.$message({
                type: 'error',
                message: 'Ошибка получения списка профилей.'
            }))
    },
    computed: {
        ...mapState([
            'myProfiles',
            'pageIsLoading',
        ]),

        foodTypeList() {
            return foodTypes;
        }
    },
    methods: {
        fillFormModel() {
            this.formModel = this.defaultFormModel;
            this.$refs.form.resetFields();
        },

        handleExceed() {
            this.$message.warning(`Можно загрузить только 1 изображение.`);
        },

        createFood() {
            const dataForCreate = {
                ...this.formModel,
                image: this.$refs.upload.uploadFiles[0] === undefined ? {} : this.$refs.upload.uploadFiles[0].raw,
            };
            let formData = new FormData()
            Object.keys(dataForCreate).forEach(key => formData.append(key, dataForCreate[key]))
            this.$refs.form.validate((valid) => {
                if (valid) {
                    this.$store.dispatch('createFood', formData)
                        .then(() => {
                            this.fillFormModel();
                            this.$message({
                                type: 'success',
                                message: 'Продукт успешно выгружен!',
                            })
                        })
                        .catch(() => this.$message({
                            type: 'error',
                            message: 'Ошибка добавления продукта!'
                        }))
                }
                return false;
            })
        },

        _calculateNewPrice() {
            this.formModel.price = this.formModel.old_price - (this.formModel.old_price / 100 * this.sale);
        },
    },
}
</script>

<style lang="scss" scoped>
.share-food-wrapper {
    width: 50%;
    margin: 40px auto;
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
    margin-bottom: 50px;
    padding: 15px 50px;
}
</style>