<template>
    <div class="max-w-7xl mx-auto sm:px-6 lg:px-8 my-4">
        <div class="my-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div class="sm:col-span-2">
                <label
                    for="fromdate"
                    class="dark:text-gray-600 text-xs text-gray-600"
                    >From</label
                >
                <div class="mt-2 mr-4 input-area">
                    <input
                        id="fromdate"
                        type="date"
                        name="fromdate"
                        v-model="fromdate"
                        autocomplete="fromdate-field"
                        class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full px-2.5 py-4 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    />
                </div>
            </div>
            <div class="sm:col-span-2">
                <label
                    for="todate"
                    class="dark:text-gray-600 text-xs text-gray-600"
                    >To</label
                >
                <div class="mt-2 mr-4 input-area">
                    <input
                        id="todate"
                        type="date"
                        name="todate"
                        v-model="todate"
                        autocomplete="todate-field"
                        class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full px-2.5 py-4 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    />
                </div>
            </div>
        </div>
        <!-- line graph -->
        <div class="grid grid-cols-3 gap-4">
            <div
                class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg col-span-2"
            >
                <div
                    class="bg-[transparent] display-[unset] justify-start"
                >
                    <div
                        class="bg-gray-200 dark:bg-gray-800 bg-opacity-25] lg:gap-8 p-6 px-4 sm:px-0"
                    >
                        <slot
                            name="volume_line_graph"
                            key="volume_line_graph"
                            :fromdate="fromdate"
                            :todate="todate"
                        ></slot>
                    </div>
                </div>
            </div>
            <!-- table -->
            <div
                class="bg-white rounded-lg shadow-md dark:bg-gray-800 overflow-hidden"
            >
                <div
                    class="bg-[transparent] flex flex-wrap flex-grow justify-evenly"
                >
                    <slot
                        name="events_table"
                        key="events_table"
                        :fromdate="fromdate"
                        :todate="todate"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useDateMixin } from "@/mixins/date";

const { DEFAULT_RANGE, todate, fromdate } = useDateMixin();
</script>
