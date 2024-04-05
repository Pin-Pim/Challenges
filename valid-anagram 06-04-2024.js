var isAnagram = function(s, t) {
  let array1 = s.split("");
  let array2 = t.split("");
  if (JSON.stringify(array1.sort()) === JSON.stringify(array2.sort())) {
      return true;
  } else {
      return false;
  }
};
console.log(isAnagram("anagram","nagaram"));

let str1 = "apple";
let str2 = "banana";

console.log(str1.localeCompare(str2)); // Output: -1 (str1 comes before str2)
console.log(str2.localeCompare(str1)); // Output: 1 (str2 comes after str1)
console.log(str1.localeCompare(str1)); // Output: 0 (str1 and str1 are equal)