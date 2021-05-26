<template>
    <el-container style="height: 908px; overflow: auto">
        <div class="find-food-wrapper">
            <div class="find-food-title">
                Найти еду
            </div>
            <div class="find-food-form-wrapper">
                <el-select
                    v-model="food_type"
                    placeholder="Выберите категорию продукта"
                    style="width: 70%"
                    @change="_fetchSelectedFood"
                >
                    <el-option
                        v-for="item in foodTypeList"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                </el-select>
            </div>
            <div
                v-if="messageIsVisible"
                style="margin-top: 50px"
            >
                Выберите интересующую категорию продукта.
            </div>
            <div
                v-loading="pageIsLoading"
                v-if="!messageIsVisible"
                style="width: 100%; height: 100%"
            >
                <el-col
                    style="padding: 0px"
                    :span="8"
                    v-for="item in selectedFood"
                    :key="item.name"
                >
                    <el-card
                        span="8"
                        class="card-item"
                        :body-style="{ padding: '0px' }"
                        @click.native="_openIndustryPage(item.company)"
                    >
                        <img
                            :src="item.image"
                            class="image"
                        />
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; text-align: left; font-weight: bold; font-size: 18px">
                                {{ item.name }}
                            </div>
                            <div style="display: flex; justify-content: space-between">
                                <div>
                                    {{ item.company }}
                                </div>
                                <div style="font-size: 14px; font-weight: bold">
                                    {{ item.price }} Руб
                                </div>
                            </div>
                        </div>
                    </el-card>
                </el-col>
            </div>
        </div>
    </el-container>
</template>

<script>
import { mapState } from 'vuex';
import {foodTypes} from './foodEnums/selectFoodTypeEnum.js';

export default {
    name: "ShareFood",
    data() {
        return {
            food_type: '',
        };
    },
    computed: {
        ...mapState([
            'pageIsLoading',
            'selectedFood',
        ]),

        messageIsVisible() {
            return this.food_type === '';
        },

        foodTypeList() {
            return foodTypes;
        },
    },
    methods: {
        _openIndustryPage(id) {
            this.$router.push(`/industry/${id}`);
        },

        _fetchSelectedFood() {
            this.$store.dispatch('fetchSelectedFood', { food_type: this.food_type })
                .catch(() => this.$message({
                    type: 'error',
                    message: 'Ошибка получения списка продуктов.'
                }))
        },
    },
}
</script>

<style lang="scss" scoped>
.find-food-wrapper {
    width: 60%;
    height: 100%;
    margin: 50px auto;
    text-align: center;
}

.find-food-form-wrapper {
    width: 100%;
    margin: 0 auto;
}

.find-food-title {
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
