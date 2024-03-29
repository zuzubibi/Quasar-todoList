<template>
    <div>
        정상적인 로그인 후 access token을 받기 위한 callback 페이지 입니다
    </div>
</template>

<script>
import { GetToken } from '../api/index.js';

    export default {
        created(){
            /** For Naver Login **/
            const query = this.$route.query;
            console.log(query);
            const data = {
                'code': query.code,
                'state': query.state
            };
            const req = GetToken(data);
            req.then(response => {
                console.log(response.data);
                this.url = response.data;
            })
            .catch(error => {
                console.error('Error', error);
            })

        }
    }
</script>

<style scoped>

</style>