<template>
    <el-container
        v-loading="pageIsLoading"
        class="comments-page-wrapper"
    >
        <div class="comments-wrapper">
            <div class="add-comment-form">
                <div class="rating-form">
                    <span>Оставить оценку: </span>
                    <el-rate
                        style="margin-left: 10px;"
                        v-model="rating"
                    ></el-rate>
                </div>
                <div class="comment-form">
                    <el-input
                        type="textarea"
                        :autosize="{ minRows: 3, maxRows: 4}"
                        v-model="comment"
                        placeholder="Введите отзыв"
                        clearable
                    >
                    </el-input>
                    <el-button
                        class="add-comment-button"
                        type="primary"
                        @click="addComment()"
                    >
                        Добавить отзыв
                    </el-button>
                </div>
            </div>
            <div
                class="comments"
                v-for="comment in profileComments"
                :key="comment.id"
            >
                <div class="comment">
                    <div class="profile">
                        <div class="profile-name">
                            {{ comment.user.username }}
                        </div>
                        <el-rate
                            v-model="comment.score"
                            disabled
                        ></el-rate>
                    </div>
                    <div class="comment-text">
                        {{ comment.comment }}
                    </div>
                </div>
            </div>
        </div>
    </el-container>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: "CommentsPage",
    props: [
        'id',
    ],
    data() {
        return {
            rating: 0,
            comment: '',
        };
    },
    mounted() {
        this.fetchProfileComments();
    },
    computed: {
        ...mapState([
            'pageIsLoading',
            'profileComments',
        ]),
    },
    methods: {
        fetchProfileComments() {
            this.$store.dispatch('fetchProfileComments', {company: this.id})
        },

        addComment() {
            this.$store.dispatch('addComment', {
                user: localStorage.userId,
                company: this.id,
                score: this.rating,
                comment: this.comment,
            })
                .then(() => {
                    this.fetchProfileComments()
                    this.$message({
                        type: 'success',
                        message: 'Отзыв успешно добавлен.',
                    })
                    this.rating = 0
                    this.comment = ''
                })
                .catch(() => {
                    this.$message({
                        type: 'error',
                        message: 'Ошибка добавления отзыва.',
                    })
                })
        },
    },
}
</script>

<style scoped>
.comments-page-wrapper {
    height: 908px;
    overflow: auto;
}

.comments-wrapper {
    width: 60%;
    height: 100%;
    margin: 0 auto;
}

.add-comment-form {
    margin: 50px;
    margin-bottom: 100px;
}

.rating-form {
    display: flex;
}

.comment-form {
    display: flex;
    margin-top: 20px;
}

.add-comment-button {
    height: 40px;
    margin-left: 25px;
}

.comments {
    margin-top: 50px;
    width: 100%;
    padding-bottom: 50px;
}

.comment {
    height: 100%;
    display: flex;
    flex-grow: 1;
}

.profile {
    margin-right: 25px;
}

.comment-text {
    width: 80%;
    height: 100%;
    word-break: break-all;
}

.profile-name {
    font-size: 20px;
    font-weight: bold;
}
</style>