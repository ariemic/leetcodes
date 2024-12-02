/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const hashmap = {};
  //create hashmap with every number as a key to be able to retrive it in O(n) time and value as false, it will mean that
  //we didn't use it yet to create a ss

  nums.forEach((num) => {
    if (!hashmap[num]) {
      hashmap[num] = true;
    }
  });

  let maxi = 0;
  for (const num of nums) {
    //this element is a start of current subsequence
    if (!hashmap[num - 1]) {
      let currentNum = num;
      let ss_len = 0;
      while (hashmap[currentNum]) {
        hashmap[currentNum] = false; //mark as visited -> sth like bfs/dfs :)
        currentNum += 1;
        ss_len += 1;
      }
      maxi = Math.max(maxi, ss_len);
      if (ss_len > nums.length / 2) {
        return maxi;
      }
    }
  }
  return maxi;
};

console.log(longestConsecutive([100, 4, 200, 1, 3, 2])); // Output: 4
