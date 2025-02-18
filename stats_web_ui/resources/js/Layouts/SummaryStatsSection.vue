<template>
    <div class="max-w-7xl mx-auto sm:px-6 lg:px-8 my-4">
        <div class="overflow-hidden">
            <div
                class="bg-[transparent] flex flex-wrap flex-grow mb-6 justify-evenly"
            >
                <div class="w-[calc(100%/4.5)] lg:gap-8 p-6 px-4 sm:px-0 m-2">
                    <slot
                        name="sum_policies"
                        key="sum_policies"
                    />
                </div>
                <div class="w-[calc(100%/4.5)] lg:gap-8 p-6 px-4 sm:px-0 m-2">
                    <slot
                        name="sum_benefits"
                        key="sum_benefits"
                    />
                </div>
                <div class="w-[calc(100%/4.5)] lg:gap-8 p-6 px-4 sm:px-0 m-2">
                    <slot
                        name="sum_claims"
                        key="sum_claims"
                    />
                </div>
                <div class="w-[calc(100%/4.5)] lg:gap-8 p-6 px-4 sm:px-0 m-2">
                    <slot
                        name="sum_newusers"
                        key="sum_newusers"
                    />
                </div>
            </div>
        </div>
        <slot></slot>
    </div>
</template>
