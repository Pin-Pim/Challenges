var twoSum = function(nums, target) {
  const pairIdx = {};

  for (let i = 0; i < nums.length; i++) {
      const num = nums[i];
      if (target - num in pairIdx) {
          return [i, pairIdx[target - num]];
      }
      pairIdx[num] = i;
  }
};
/*Only thing I wonder with this code is what if it uses itself twice? */