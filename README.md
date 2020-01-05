#thunes_test
* This Branch is showing the front-end code based on vue.js
* and below is its file struct
```
.
├── build
│   ├── build.js
│   ├── check-versions.js
│   ├── logo.png
│   ├── utils.js
│   ├── vue-loader.conf.js
│   ├── webpack.base.conf.js
│   ├── webpack.dev.conf.js
│   └── webpack.prod.conf.js
├── config
│   ├── dev.env.js
│   ├── index.js
│   ├── prod.env.js
│   └── test.env.js
├── index.html -> (home page)
├── package.json -> (required dependencies)
├── package-lock.json
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── components -> (all wrote components)
│   │   ├── Additional.vue
│   │   ├── Beneficiary.vue
│   │   ├── Home.vue
│   │   ├── Sender.vue
│   │   ├── TransactionDetail.vue
│   │   ├── TransactionList.vue
│   │   ├── Transaction.vue
│   │   └── UsedBeneficiary.vue
│   ├── main.js -> (main javascript to import different packages)
│   └── router
│       └── index.js -> (rounter definition and path mapping)
├── vue.config.js
└── webpack-dev-server

```
* In my project I only run nodejs server when I developing vuejs code. but in the production environment,
I build this front-end and put it into nginx.
* If you would like to run the nodejs server. please follow below steps:
```
1. please make sure nodejs and npm are ready
$ node -v
v12.11.1

zhkai@CNzhkai03 MINGW64 ~/vuejs/vueexample/thunes_test (vue-js)
$ npm -v
6.11.3
2. In this folder, please run 'npm install' to install all required packages;
3. you can run 'npm run dev' to start the nodejs server and access this webservice
```
