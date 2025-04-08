export const range = (start: number, end: number): number[] =>
  [...Array(end - start)].map((_, i) => i + start);

export const getItemNumbers = (selected: number, max: number): number[] => {
  if (max < 6) {
      return range(1, max + 1);
  }
  if (selected < 3) {
      return range(1, 6);
  }
  if (max - 5 <= selected) {
      return range(max - 4, max + 1);
  }
  return range(selected - 2, selected + 3);
};

export const getItemNumbersFixed = (selected: number, max: number): number[] => {
  if (max < 6) {
      return range(1, max + 1);
  }
  if (selected < 3) {
      return range(1, 7); // fixed to include 6 elements (1-6)
  }
  if (max - 4 <= selected) { // fixed - adjusted threshold
      return range(max - 4, max + 1);
  }
  return range(selected - 2, selected + 3);
};