<template>
    <div class="max-w-7xl mx-auto sm:px-6 lg:px-8 my-4">
        <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div class="sm:col-span-2">
                <label
                    for="fromdate"
                    class="dark:text-gray-600 text-xs text-gray-600"
                    >From</label
                >
                <div class="mt-2 mr-4 input-area">
                    <input
                        type="date"
                        name="fromdate"
                        id="fromdate"
                        v-model="fromdate"
                        autocomplete="fromdate-field"
                        color="#9ca3af"
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
                        type="date"
                        name="todate"
                        id="todate"
                        v-model="todate"
                        autocomplete="todate-field"
                        class="bg-gray-50 border border-gray-300 text-gray-600 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full px-2.5 py-4 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    />
                </div>
            </div>
        </div>
        <div class="overflow-hidden">
            <div
                class="bg-[transparent] flex flex-wrap flex-grow mb-6 justify-between"
            >
                <div class="w-[calc(100%/3.5)] lg:gap-8 p-6 px-4 sm:px-0 m-2">
                    <slot
                        name="m2m_policies"
                        key="m2m_policies"
                        :fromdate="fromdate"
                        :todate="todate"
                    />
                </div>
                <div class="w-[calc(100%/3.5)] lg:gap-8 p-6 px-4 sm:px-0 m-2">
                    <slot
                        name="m2m_benefits"
                        key="m2m_benefits"
                        :fromdate="fromdate"
                        :todate="todate"
                    />
                </div>
                <div class="w-[calc(100%/3.5)] lg:gap-8 p-6 px-4 sm:px-0 m-2">
                    <slot
                        name="m2m_claims"
                        key="m2m_claims"
                        :fromdate="fromdate"
                        :todate="todate"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useDateMixin } from '@/mixins/date';

const { DEFAULT_RANGE, todate, fromdate } = useDateMixin();
</script>
