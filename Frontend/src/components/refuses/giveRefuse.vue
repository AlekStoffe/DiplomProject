<template>
    <div>
        <el-table
            :data="giveRefuseItems"
            min-width="250px"
        >
            <el-table-column
                label="Фотография">
                <template slot-scope="props">
                    <img
                        :src="props.row.image"
                        style="height: 50px"
                    />
                </template>
            </el-table-column>
            <el-table-column
                prop="username"
                label="Пользователь"
                min-width="100px"
            />
            <el-table-column
                prop="name"
                label="Название"
                min-width="100px"
            />
            <el-table-column
                prop="quantity"
                label="Количество"
                min-width="100px"
            />
            <el-table-column
                prop="period"
                label="Периодичность образования отходов"
                min-width="200px"
            />
            <el-table-column
                prop="description"
                label="Описание"
                min-width="100px"
            />
            <el-table-column
                prop="telephone"
                label="Номер телефона"
                min-width="100px"
            />
            <el-table-column
                prop="point"
                label="Адрес отходов"
                min-width="100px"
            />
        </el-table>
    </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
    name: "GiveAwayRefuse",
    mounted() {
        this.fetchGiveRefuseItems();
    },
    computed: {
        ...mapState([
            'giveRefuseItems',
        ]),
    },
    methods: {
        fetchGiveRefuseItems() {
            this.$store.dispatch('fetchGiveRefuseItems')
                .catch(() => this.message({
                    type: 'error',
                    message: 'Ошибка получения списка отходов.',
                }))
        }
    },
}
</script>

<style scoped>

</style>