module.exports = {
    devServer: {
        // the IP and port when starting the vue
        host: 'localhost',
        port: 8000,
        proxy: {
            // matching all url starting with '/api'
            '/api': {
                target: 'http://locahost:8000/api/v1',
                changeOrigin: true,
                ws: true
            }
        }
    }
}