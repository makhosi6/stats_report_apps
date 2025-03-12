<script setup>
import { defineProps } from "vue";
import {
    BeakerIcon,
    AcademicCapIcon,
    UserIcon,
    Cog6ToothIcon,
    InboxStackIcon,
} from "@heroicons/vue/24/solid";

defineProps({
    icon: {
        type: String,
    },
    change: {
        type: Number,
    },
    time_frame: {
        type: String,
    },
    type: {
        type: String,
    },
    value: {
        type: String,
    },
});

const getIconColor = (iconName) => {
    switch (iconName) {
        case "policies":
            return "border-yellow-500 bg-yellow-500 text-white hover:border-yellow-500 hover:bg-yellow-500";
        case "claims":
            return "border-pink-500 bg-pink-500 text-white hover:border-pink-500 hover:bg-pink-500";
        case "general":
            return "border-emerald-500 bg-emerald-500 text-white hover:border-emerald-500 hover:bg-emerald-500";
        case "benefits":
        default:
            return "border-indigo-500 bg-indigo-500 text-white hover:border-indigo-500 hover:bg-indigo-500";
    }
};

const getIcon = (iconName) => {
    switch (iconName) {
        case "benefits":
            return AcademicCapIcon;
        case "policies":
            return UserIcon;
        case "claims":
            return Cog6ToothIcon;
        case "general":
            return BeakerIcon;
        default:
            return InboxStackIcon;
    }
};
</script>

<template>
    <div
        class="max-w-2xl px-8 py-4 bg-white rounded-lg shadow-md dark:bg-gray-800"
    >
        <div class="flex items-right justify-between">
            <span
                class="text-sm font-light text-indigo-500-600 dark:text-indigo-500-400 text-left"
            >
                <span
                    :class="getIconColor(icon)"
                    class="inline-grid place-items-center border align-middle select-none font-sans font-medium text-center transition-all duration-300 ease-in disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-sm min-w-[38px] min-h-[38px] rounded-md shadow-sm hover:shadow-md hover:brightness-110"
                >
                    <component :is="getIcon(icon)" class="size-6 h-6 w-6" />
                </span>
            </span>
            <div class="text-right">
                <span
                    class="text-sm font-light text-gray-600 dark:text-gray-400"
                    >{{ type }}</span
                >
                <h2
                    href="#"
                    class="text-xl font-bold text-gray-700 dark:text-white hover:text-gray-600 dark:hover:text-gray-200 hover:underline"
                    tabindex="0"
                    role="link"
                >
                    {{ value }}
                </h2>
            </div>
        </div>
        <div class="flex items-center justify-between mt-4">
            <span
                class="text-sm font-light"
                :class="
                    Number(change) > 0
                        ? change >= Number(30)
                            ? 'text-green-600'
                            : 'text-red-500'
                        : 'text-gray-600 dark:text-gray-400'
                "
                >{{
                    Number(change) > 0
                        ? Number(change) >= Number(30)
                            ? "+"
                            : "-"
                        : ""
                }}<span>{{ change }} {{ isNaN(change) ? '': '%  ' }}</span>
                <span class="text-gray-600 dark:text-gray-400">
                 - {{ time_frame }}
                </span>
            </span>
        </div>
    </div>
</template>
