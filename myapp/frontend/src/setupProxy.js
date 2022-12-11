const { createProxyMiddleware } = require('http-proxy-middleware');

https://create-react-app.dev/docs/proxying-api-requests-in-development/
module.exports = function (app) {
    app.use(
        ['**/api/**', '/myapp', '/login'],
        createProxyMiddleware({
            target: 'http://10.10.20.233:3000/frontend/',
            changeOrigin: true,
        })
    );
}; 