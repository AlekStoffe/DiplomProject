<template>
    <el-row class="map-page-wrapper">
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
                <div v-for="item in arr" :key="item">
                    <el-card class="card-item" :body-style="{ padding: '0px' }">
                        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image"/>
                        <div style="padding: 14px;">
                            <div style="margin-bottom: 10px; font-weight: bold">{{ item.name }}</div>
                            <div>{{ item.restaurant }}</div>
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
                    <gmap-marker
                            v-for="res in restaraunts"
                            :key="res.id"
                            :position="{ lat: res.latitude, lng: res.longitude }"
                            :clickable="true"
                            :draggable="false"
                    >
                    </gmap-marker>
                </gmap-map>
            </template>
        </el-col>
    </el-row>
</template>

<script>

    export default {
        name: "map",
        data() {
            return {
                arr: [
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
                    {
                        name: 'Yummy hamburger',
                        restaurant: 'Ресторан',
                    },
                ],
                searchField: '',
                visible: true,
                iconButtonMenu: 'el-icon-arrow-left',
                map_span: 19,
                restaraunts: [
                    {
                        id: 1,
                        latitude: 54.19259256331395,
                        longitude: 37.61542753295216,
                    },
                    {
                        id: 2,
                        latitude: 54.19423415096624,
                        longitude: 37.58641104722444,
                    },
                    {
                        id: 3,
                        latitude: 54.17819526822442,
                        longitude: 37.601576959214775,
                    },
                    {
                        id: 4,
                        latitude: 54.18632593216596,
                        longitude: 37.598578453467795,
                    },
                ]
            }
        },
        methods: {
            _openSideMenu() {
                this.visible = !this.visible;
                this.visible === true ? this.map_span = 19 : this.map_span = 21
                this.iconButtonMenu === 'el-icon-arrow-left' ?  this.iconButtonMenu = 'el-icon-search' : this.iconButtonMenu = 'el-icon-arrow-left';
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