import colors from 'vuetify/es5/util/colors'

export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - OCB',
    title: 'Overhead Cables & BirdLife',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    // link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    link: [],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/assets/styles'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins

  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
    '@nuxtjs/i18n',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://auth.nuxtjs.org
    '@nuxtjs/auth-next',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    'nuxt-leaflet',
  ],

  router: {
    middleware: ['auth'],
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    prefix: '/api/v1/',
    proxy: true,
  },

  proxy: {
    '/api/v1/': process.env.API_URL || 'http://localhost:8000',
  },

  auth: {
    cookie: false,
    redirect: {
      login: '/',
      logout: '/',
      home: '/',
    },
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access', // property name of access token get from Back-end
          global: true,
          required: true,
          type: 'JWT',
        },
        user: {
          property: false,
          autoFetch: true,
        },
        refreshToken: {
          // it sends request automatically when the access token expires, and its expire time has set on the Back-end
          property: 'refresh', // property name of refresh token get from Back-end
          data: 'refresh', // data can be used to set the name of the property you want to send in the request.
        },
        endpoints: {
          login: {
            url: 'auth/jwt/create/',
            method: 'post',
          },
          refresh: { url: 'auth/jwt/refresh', method: 'post' },
          logout: false, //  there is no endpoint for logout in API. Just remove the token from localstorage
          user: {
            url: 'auth/users/me',
            method: 'get',
            property: false,
          },
        },
      },
    },
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  i18n: {
    locales: [
      { code: 'en', iso: 'en-US', file: 'en.json' },
      { code: 'fr', iso: 'fr-FR', file: 'fr.json' },
    ],

    defaultLocale: 'fr',
    langDir: '~/locales/',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend(config, ctx) {
      if (ctx.isDev) {
        config.devtool = ctx.isClient ? 'source-map' : 'inline-source-map'
      }
    },
  },
}
