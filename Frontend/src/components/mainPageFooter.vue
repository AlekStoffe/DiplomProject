<template>
    <div class="footer-wrapper">
        <div class="flex-wrapper">
            <div class="license-info">
                <h3>Спаси еду!!!</h3>
                <div>
                    Все права защищены////
                </div>
                <div>
                    ООО “Итми”
                </div>
                <div>
                    ИНН 7804653732
                </div>
                <div>
                    ОГРН 1197847155307
                </div>
                <div class="organization-tag">
                    © 2020 ООО «Итми»
                </div>
            </div>
            <div class="license-info">
                <h3>Спаси еду!!!</h3>
                <div>
                    Все права защищены////
                </div>
                <div>
                    ООО “Итми”
                </div>
                <div>
                    ИНН 7804653732
                </div>
                <div>
                    ОГРН 1197847155307
                </div>
                <div class="organization-tag">
                    © 2020 ООО «Итми»
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "mainPageFooter"
    }
</script>

<style lang="scss" scoped>
    .footer-wrapper {
        border-top: 1px solid #e2e2e2;
        background-color: azure;
    }

    .flex-wrapper {
        display: flex;
        justify-content: space-between;
        width: 1100px;
        height: 240px;
        margin: 0 auto;
        color: dimgray;
    }

    .license-info {
        font-size: 14px;
        margin-top: 30px;
        margin-left: 19px;
    }

    .organization-tag {
        margin-top: 70px;
    }
</style>