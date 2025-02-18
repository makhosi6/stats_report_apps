import { ref } from 'vue';

export const useDateMixin = () => {
  const DEFAULT_RANGE = 12;
  const todate = ref(new Date().toISOString().split('T')[0]);
  const fromdate = ref(
    new Date(new Date().setMonth(new Date().getMonth() - DEFAULT_RANGE))
      .toISOString()
      .split('T')[0]
  );

  return {
    DEFAULT_RANGE,
    todate,
    fromdate,
  };
};
