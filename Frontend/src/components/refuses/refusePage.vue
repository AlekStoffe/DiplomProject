<template>
    <el-container class="refuse-page-wrapper">
        <div class="refuse-wrapper">
            <div style="width: 100%">
                <div class="add-refuse-button">
                    <el-button
                        type="warning"
                        round
                        @click="_openGiveAwayRefuseFormDialog"
                    >
                        Добавить предложение о получении отходов
                    </el-button>
                    <el-button
                        type="success"
                        round
                        @click="_openGiveRefuseFormDialog"
                    >
                        Добавить предложение о сбыте отходов
                    </el-button>
                </div>
                <div class="add-refuse-button">
                    <el-radio-group
                        v-model="refuse_type"
                    >
                        <el-radio-button
                            :label="true"
                        >
                            Получить отходы
                        </el-radio-button>
                        <el-radio-button
                            :label="false"
                            @change="radioButtonChange(orders_type)"

                        >
                            Сбыть отходы
                        </el-radio-button>
                    </el-radio-group>
                </div>
            </div>
            <div>
                <give-away-refuse
                    ref="give-away-refuse"
                    v-if="refuse_type"
                />
                <give-refuse
                    ref="give-refuse"
                    v-else
                />
            </div>
            <div>
                <el-dialog
                    :visible.sync="giveAwayRefuseFormIsVisible"
                    top="3vh"
                    :show-close="false"
                >
                    <el-form
                        ref="giveAwayRefuseForm"
                        :model="giveAwayRefuseFormModel"
                    >
                        <el-form-item
                            label="Вид отходов"
                            prop="name"
                        >
                            <el-input
                                placeholder="Введите название"
                                size="50px"
                                v-model="giveAwayRefuseFormModel.name"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="ФИО"
                            prop="username"
                        >
                            <el-input
                                placeholder="Введите имя"
                                size="50px"
                                v-model="giveAwayRefuseFormModel.username"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Объемы образования отходов(кг/л)"
                            prop="quantity"
                        >
                            <el-input-number
                                placeholder="Введите количество"
                                size="50px"
                                v-model="giveAwayRefuseFormModel.quantity"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Периодичность образования"
                            prop="period"
                        >
                            <el-input
                                placeholder="Введите период"
                                size="50px"
                                v-model="giveAwayRefuseFormModel.period"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Описание"
                            prop="description"
                        >
                            <el-input
                                type="textarea"
                                placeholder="Введите описание"
                                size="50px"
                                v-model="giveAwayRefuseFormModel.description"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Телефон"
                            prop="telephone"
                        >
                            <el-input
                                placeholder="Введите телефон"
                                size="50px"
                                v-model="giveAwayRefuseFormModel.telephone"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Территориальное расположение отходов"
                            prop="point"
                        >
                            <el-input
                                placeholder="Введите описание"
                                size="50px"
                                v-model="giveAwayRefuseFormModel.point"
                                clearable
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
                            <el-button
                                size="small"
                                type="primary"
                            >
                                Загрузить изображение продукта
                            </el-button>
                        </el-upload>
                    </el-form>
                    <div style="text-align: center">
                        <el-button @click="_closeGiveAwayRefuseFormDialog">Отменить</el-button>
                        <el-button type="primary" @click="createGiveAwayRefuseItem">Добавить</el-button>
                    </div>
                </el-dialog>
            </div>
            <div>
                <el-dialog
                    :visible.sync="giveRefuseFormIsVisible"
                    top="3vh"
                    :show-close="false"
                >
                    <el-form
                        ref="giveRefuseForm"
                        :model="giveRefuseFormModel"
                    >
                        <el-form-item
                            label="Вид отходов"
                            prop="name"
                        >
                            <el-input
                                placeholder="Введите название"
                                size="50px"
                                v-model="giveRefuseFormModel.name"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="ФИО"
                            prop="username"
                        >
                            <el-input
                                placeholder="Введите имя"
                                size="50px"
                                v-model="giveRefuseFormModel.username"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Требуемый минимальный объем отходов(кг/л)"
                            prop="quantity"
                        >
                            <el-input-number
                                placeholder="Введите количество"
                                size="50px"
                                v-model="giveRefuseFormModel.quantity"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Периодичность образования"
                            prop="period"
                        >
                            <el-input
                                placeholder="Введите период"
                                size="50px"
                                v-model="giveRefuseFormModel.period"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Описание"
                            prop="description"
                        >
                            <el-input
                                type="textarea"
                                placeholder="Введите описание"
                                size="50px"
                                v-model="giveRefuseFormModel.description"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="дата"
                            prop="date"
                        >
                            <el-date-picker
                                v-model="giveRefuseFormModel.date"
                                type="date"
                                format="dd.MM.yyyy"
                                value-format="yyyy-MM-dd-HH-mm"
                            >
                            </el-date-picker>
                        </el-form-item>
                        <el-form-item
                            label="Телефон"
                            prop="telephone"
                        >
                            <el-input
                                placeholder="Введите телефон"
                                size="50px"
                                v-model="giveRefuseFormModel.telephone"
                                clearable
                            />
                        </el-form-item>
                        <el-form-item
                            label="Адрес своего местонахождения"
                            prop="point"
                        >
                            <el-input
                                placeholder="Введите описание"
                                size="50px"
                                v-model="giveRefuseFormModel.point"
                                clearable
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
                            <el-button
                                size="small"
                                type="primary"
                            >
                                Загрузить изображение продукта
                            </el-button>
                        </el-upload>
                    </el-form>
                    <div style="text-align: center">
                        <el-button @click="_closeGiveRefuseFormDialog">Отменить</el-button>
                        <el-button type="primary" @click="createGiveRefuseItem">Добавить</el-button>
                    </div>
                </el-dialog>
            </div>
        </div>
    </el-container>
</template>

<script>
import GiveAwayRefuse from "./giveAwayRefuse.vue";
import GiveRefuse from './giveRefuse.vue';

export default {
    name: "RefusePage",
    components: {
        GiveAwayRefuse,
        GiveRefuse,
    },
    data() {
        return {
            refuse_type: true,
            giveRefuseFormIsVisible: false,
            giveAwayRefuseFormIsVisible: false,
            giveRefuseFormModel: {
                name: '',
                username: '',
                quantity: '',
                period: '',
                description: '',
                point: '',
                telephone: '',
                date: '',
            },
            giveAwayRefuseFormModel: {
                name: '',
                username: '',
                quantity: '',
                period: '',
                description: '',
                point: '',
                telephone: '',
            },
            limit: 1,
        };
    },
    methods: {
        _openGiveRefuseFormDialog() {
            this.giveRefuseFormIsVisible = true;
        },

        _closeGiveRefuseFormDialog() {
            this.giveRefuseFormIsVisible = false;
            this.$refs.giveRefuseForm.resetFields();
        },

        _openGiveAwayRefuseFormDialog() {
            this.giveAwayRefuseFormIsVisible = true;
        },

        _closeGiveAwayRefuseFormDialog() {
            this.giveAwayRefuseFormIsVisible = false;
            this.$refs.giveAwayRefuseForm.resetFields();
        },

        createGiveRefuseItem() {
            const dataForCreate = {
                ...this.giveRefuseFormModel,
                image: this.$refs.upload.uploadFiles[0] === undefined ? {} : this.$refs.upload.uploadFiles[0].raw,
                user: localStorage.userId,
            };
            let formData = new FormData()
            Object.keys(dataForCreate).forEach(key => formData.append(key, dataForCreate[key]))
            this.$store.dispatch('createGiveRefuseItem', formData)
                .finally(() => this.$refs["give-refuse"].fetchGiveRefuseItems())
        },

        createGiveAwayRefuseItem() {
            const dataForCreate = {
                ...this.giveAwayRefuseFormModel,
                image: this.$refs.upload.uploadFiles[0] === undefined ? {} : this.$refs.upload.uploadFiles[0].raw,
                user: localStorage.userId,
            };
            let formData = new FormData()
            Object.keys(dataForCreate).forEach(key => formData.append(key, dataForCreate[key]))
            this.$store.dispatch('createGiveAwayRefuseItem', formData)
                .finally(() => this.$refs["give-away-refuse"].fetchGiveAwayRefuseItems())
        },

        handleExceed() {
            this.$message.warning(`Можно загрузить только 1 изображение.`);
        },
    },
}
</script>

<style lang="scss" scoped>
.refuse-page-wrapper {
    height: 908px;
    overflow: auto;
}

.refuse-wrapper {
    width: 75%;
    height: 100%;
    margin: 0 auto;
}

.add-refuse-button {
    margin: 50px 0 50px 0;
    text-align: center;
}

.upload-field {
    text-align: center;
    height: 80px;
}
</style>