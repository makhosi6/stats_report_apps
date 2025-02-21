<script setup>
import AppLayout from "@/Layouts/AppLayout.vue";
import Welcome from "@/Components/Welcome.vue";

defineProps({
    stats: {
        type: Object,
    }
});
</script>

<template>
    <AppLayout title="Dashboard">
        <template #header>
            <p
                class="text-sm text-gray-900 dark:text-gray-200 leading-tight flex"
            >
                <a href="#"
                    ><svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                        aria-hidden="true"
                        data-slot="icon"
                        width="20"
                        heighgt="20"
                    >
                        <path
                            fill-rule="evenodd"
                            d="M9.293 2.293a1 1 0 0 1 1.414 0l7 7A1 1 0 0 1 17 11h-1v6a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6H3a1 1 0 0 1-.707-1.707l7-7Z"
                            clip-rule="evenodd"
                        ></path></svg
                ></a>
                <span class="text-gray-600 px-2"> > </span>
                <a href="#"> Stats </a>
            </p>
        </template>
        <div class="py-12">
            <Welcome :stats="stats"  />
        </div>
    </AppLayout>
</template>

<style scoped>
.breadcrumbs span,
.breadcrumbs a {
    max-width: 100px !important;
}
</style>
