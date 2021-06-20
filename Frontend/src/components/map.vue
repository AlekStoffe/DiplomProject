<template>
    <el-row
        v-loading="pageIsLoading"
        class="map-page-wrapper"
    >
        <transition name="el-fade-in-linear">
            <el-col
                :span="5"
                class="menu-config"
                v-if="visible"
            >
                <div class="input-search">
                    <el-input
                        placeholder="Поиск"
                        prefix-icon="el-icon-search"
                        clearable
                        v-model="searchField"
                    ></el-input>
                </div>
                <div v-for="item in mapCompanies" :key="item.id">
                    <el-card
                        class="card-item"
                        :body-style="{ padding: '0px' }"
                        @click.native="_openIndustryPage(item.id)"
                    >
                        <img
                            :src="item.image"
                            class="image"
                            v-tooltip="'You have new messages.'"
                        />
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold">{{ item.name }}</div>
                            <div>{{ item.address }}</div>
                        </div>
                    </el-card>
                </div>
            </el-col>
        </transition>
        <el-button
            @click="_openSideMenu"
            class="side-menu-visible-button"
            circle
            size="small"
            :icon="iconButtonMenu"
            type="primary"
        >
        </el-button>
        <el-col
            class="map-wrapper"
        >
            <template>
                <gmap-map
                    :center="{ lat: 54.16836657190996, lng:  37.58855911182462}"
                    :zoom="15"
                    :streetViewControl="false"
                    style="width: 100%; height: 100%;"
                >
                    <div
                        v-for="res in mapCompanies"
                        :key="res.id"
                    >
                        <el-tooltip
                            placement="top"
                            :content="res.name"
                            effect="dark"
                        >
                            <gmap-marker
                                :position="{ lat: res.lat, lng: res.lon }"
                                :clickable="true"
                                :draggable="false"
                                :title="res.name"
                                @click="_openIndustryPage(res.id)"
                            >
                            </gmap-marker>
                        </el-tooltip>
                    </div>
                </gmap-map>
            </template>
        </el-col>
    </el-row>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: "Map",
    data() {
        return {
            searchField: '',
            visible: true,
            iconButtonMenu: 'el-icon-arrow-left',
            map_span: 19,
        }
    },
    mounted() {
        this.$store.dispatch('fetchMapCompanies')
            .catch(() => this.$message({
                type: 'error',
                message: 'Ошибка получения организаций.',
            }))
    },
    watch: {
        searchField(newValue) {
            this.$store.dispatch('searchFood', { search: newValue })
        },
    },
    computed: {
        ...mapState([
            'pageIsLoading',
            'mapCompanies',
        ]),
    },
    methods: {
        _openSideMenu() {
            this.visible = !this.visible;
            this.visible === true ? this.map_span = 19 : this.map_span = 21
            this.iconButtonMenu === 'el-icon-arrow-left' ? this.iconButtonMenu = 'el-icon-search' : this.iconButtonMenu = 'el-icon-arrow-left';
        },

        _openIndustryPage(id) {
            this.$router.push(`/industry/${id}`);
        },
    },
}
</script>

<style lang="scss">
.map-page-wrapper {
    overflow: auto;
    height: 908px;
}

.menu-config {
    position: relative;
    z-index: 1;
    background-color: white;
    height: 100%;
    overflow: scroll;
    overflow-x: hidden;
}

.input-search {
    margin: 25px 20px;
    border-bottom: 1px solid #e2e2e2;
}

.input-search .el-input__inner {
    border: 0;
}

.card-item {
    width: 88%;
    height: 90%;
    margin: 20px auto;
    cursor: pointer;
}

.image {
    width: 100%;
    height: 180px;
}

.side-menu-visible-button {
    position: fixed;
    margin: 20px 20px;
    z-index: 2;
}

.map-wrapper {
    position: absolute;
    height: 100%;
}
</style>