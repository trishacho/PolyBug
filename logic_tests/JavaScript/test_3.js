describe('getParentIndex', () => {
    it('should not throw when startingPoint becomes negative', () => {
      // Setup input where index is 0, so startingPoint = -1
      const index = 0;
      const commentsArr = []; // empty or shorter array
      const commentData = { childrenLevel: 1 };
  
      const getParentIndex = () => {
        let startingPoint = index - 1;
        try {
          while (
            startingPoint >= 0 &&
            commentsArr[startingPoint].childrenLevel > commentData.childrenLevel
          ) {
            startingPoint--;
          }
        } catch {
          startingPoint = undefined;
        }
        return startingPoint;
      };
  
      expect(() => getParentIndex()).not.toThrow();
      expect(getParentIndex()).toBeUndefined();
    });
  });