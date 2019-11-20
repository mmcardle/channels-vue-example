
const host = '127.0.0.1:8000'


module.exports = {
    runtimeCompiler: true,
    css: {
      // Required due to https://github.com/vuejs/vue-cli/issues/4572
      // See https://stackoverflow.com/questions/57916549/vue-cli-run-build-typeerror-name-undefined
      sourceMap: true
    },
    parallel: false, // https://github.com/vuejs/vue-cli/issues/2785
    devServer: {
        proxy: {
            '/api': {
                target: 'http://' + host,
                changeOrigin: true,
                xfwd: false
            },
            '/ws': {
                target: 'ws://' + host,
                changeOrigin: true,
                ws: true
            }
        }
    },
    lintOnSave: process.env.NODE_ENV !== 'production',
};
