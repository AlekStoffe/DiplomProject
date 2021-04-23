<template>
    <div class="industries-wrapper">
        <el-row
                :gutter="40"
        >
            <el-col class="cards-list-title">
                <span>Ваши предприятия:</span>
            </el-col>
            <el-col
                    style="padding: 0px"
                    :span="8" v-for="item in industries" :key="item"
            >
                <el-card
                        span="8"
                        class="card-item"
                        :body-style="{ padding: '0px' }"
                        style="cursor: pointer;"
                        @click.native="_openIndustryPage"
                >
                    <img
                            src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                            class="image"

                    />
                    <div style="padding: 14px;">
                        <div style="margin-bottom: 10px; font-weight: bold">{{ item.name }}</div>
                        <div>{{ item.restaurant }}</div>
                    </div>
                </el-card>
            </el-col>
            <el-col>
                <el-button
                        class="add-industry-button"
                        @click="_openAddFormIndustry"
                >Добавить предприятие</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "MyIndustry",
        data() {
          return {
              industries: [
                  {
                      name: 'Yummy hamburger',
                      restaurant: 'Ресторан',
                  },
                  {
                      name: 'Yummy hamburger',
                      restaurant: 'Ресторан',
                  },
                  {
                      name: 'Yummy hamburger',
                      restaurant: 'Ресторан',
                  },
                  {
                      name: 'Yummy hamburger',
                      restaurant: 'Ресторан',
                  },
              ],
          };
        },
        methods: {
            _openAddFormIndustry() {
                this.$router.push('/addIndustry');
            },

            _openIndustryPage() {
                this.$router.push('/industry');
            },
        }
    }
</script>

<style scoped lang="scss">
    .industries-wrapper {
        width: 60%;
        margin: 100px auto;
    }

    .cards-list-title {
        font-size: 25px;
        line-height: 30px;
    }

    .card-item {
        height: 300px;
    }

    .add-industry-button {
        margin-top: 20px;
        padding: 20px 30px;
    }
</style>