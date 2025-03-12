import './bootstrap';
import '../css/app.css';

import { createApp, h } from 'vue';
import { createInertiaApp } from '@inertiajs/vue3';
import { resolvePageComponent } from 'laravel-vite-plugin/inertia-helpers';
import { ZiggyVue } from '../../vendor/tightenco/ziggy';
import { createStore } from 'vuex';

const appName = import.meta.env.VITE_APP_NAME || 'Laravel';


const store = createStore({
    state: {
        stats: {},
    },
    mutations: {
        setStats(state, data) {
            state.stats = data;
        },
    },
    actions: {
        updateStats({ commit }, data) {
            commit('setStats', data);
        },
    },
});


createInertiaApp({
    title: (title) => `${title} - ${appName}`,
    resolve: (name) => resolvePageComponent(`./Pages/${name}.vue`, import.meta.glob('./Pages/**/*.vue')),
    setup({ el, App, props, plugin }) {
        return createApp({ render: () => h(App, props) })
            .use(plugin)
            .use(ZiggyVue)
            .use(store)
            .mount(el);
    },
    progress: {
        color: '#206aff',
    },
});
