var isValid = function(s) {
    let dictionary = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    };
    let stack = [];
    for (let c of s) {
        if (dictionary[c]) {
            if (stack.length && stack[stack.length - 1] === dictionary[c]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(c);
        }
    }

    return !stack.length;
};