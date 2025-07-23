import axios from 'axios'
export default {
    test(data) {
        return axios.post('/api/btn_click', data)
    }
}