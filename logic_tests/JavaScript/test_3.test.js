const getParentIndex = require('./helpers/getParentIndex');

describe('getParentIndex', () => {
  it('should not throw when startingPoint becomes negative', () => {
    const index = 0;
    const commentsArr = []; // empty or shorter array
    const commentData = { childrenLevel: 1 };

    expect(() => getParentIndex(index, commentsArr, commentData)).not.toThrow();
    expect(getParentIndex(index, commentsArr, commentData)).toBeUndefined();
  });

  it('should never return a negative value', () => {
    // Test with various edge cases that could potentially return negative
    const testCases = [
      { index: 0, commentsArr: [], commentData: { childrenLevel: 1 } },
      { index: 1, commentsArr: [{ childrenLevel: 0 }], commentData: { childrenLevel: 2 } },
      { index: 2, commentsArr: [{ childrenLevel: 0 }, { childrenLevel: 1 }], commentData: { childrenLevel: 3 } }
    ];
  
    testCases.forEach(({ index, commentsArr, commentData }) => {
      const result = getParentIndex(index, commentsArr, commentData);
      expect(result).not.toBeLessThan(0); // Ensures no negative returns
      // Also validates it's either undefined or a non-negative number
      expect(result === undefined || result >= 0).toBe(true);
    });
  });

  // Add more test cases as needed
  it('should return correct parent index for nested comments', () => {
    const commentsArr = [
      { childrenLevel: 0 },
      { childrenLevel: 1 },
      { childrenLevel: 2 },
      { childrenLevel: 1 }
    ];
    const commentData = { childrenLevel: 2 };
    
    expect(getParentIndex(2, commentsArr, commentData)).toBe(1);
  });
});