var longestConsecutive = function(nums) {
    const setItems = new Set(nums);
    let maxCount = 0;
    for (let i = 0; i < nums.length; i++) {
        if (!setItems.has(nums[i]-1)) {
            let count =1;
            let index =1;
            if (maxCount === 0) {maxCount = 1}
            while (setItems.has(nums[i] + index)) {
                count += 1;
                index += 1;
                if (count > maxCount) {
                    maxCount = count;
                }
            }
        }
    }
    console.log(maxCount);
    return maxCount;
};

longestConsecutive([0]);