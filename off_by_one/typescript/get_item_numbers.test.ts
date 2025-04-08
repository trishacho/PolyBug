import { getItemNumbers, getItemNumbersFixed } from './get_item_numbers';

describe('getItemNumbers', () => {
    test('should return correct range when max is less than 6', () => {
        expect(getItemNumbers(4, 5)).toEqual([1, 2, 3, 4, 5]);
    });

    test('should return range [1, 2, 3, 4, 5] for selected < 3 when max >= 6', () => {
        expect(getItemNumbers(2, 10)).toEqual([1, 2, 3, 4, 5]);
    });

    test('should return range [6, 7, 8, 9, 10] when selected is near max', () => {
        expect(getItemNumbers(8, 10)).toEqual([6, 7, 8, 9, 10]);
    });

    test('should return range based on selected when selected is in the middle', () => {
        expect(getItemNumbers(4, 10)).toEqual([2, 3, 4, 5, 6]);
    });
});

describe('getItemNumbersFixed', () => {
    test('should return correct range when max is less than 6', () => {
        expect(getItemNumbersFixed(4, 5)).toEqual([1, 2, 3, 4, 5]);
    });

    test('should return range [1, 2, 3, 4, 5, 6] for selected < 3 when max >= 6', () => {
        expect(getItemNumbersFixed(2, 10)).toEqual([1, 2, 3, 4, 5, 6]);
    });

    test('should return range [6, 7, 8, 9, 10] when selected is near max', () => {
        expect(getItemNumbersFixed(8, 10)).toEqual([6, 7, 8, 9, 10]);
    });

    test('should return range based on selected when selected is in the middle', () => {
        expect(getItemNumbersFixed(4, 10)).toEqual([2, 3, 4, 5, 6]);
    });
});