const getParentIndex = (index, commentsArr, commentData) => {
    let startingPoint = index - 1;
    try {
      while (commentsArr[startingPoint].childrenLevel > commentData.childrenLevel) {
        startingPoint--;
      }
    } catch {
      startingPoint = undefined;
    }
    return startingPoint;
  }
  
  module.exports = getParentIndex;