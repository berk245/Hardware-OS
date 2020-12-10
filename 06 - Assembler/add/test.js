function checkNesting(str) {
  let matchingChars = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  let charArray = str.split("");

  //if the length is odd
  if (charArray.length % 2 != 0) {
    console.log("Not valid length");
    return;
  }

  //Check character count
  //If amount of matching chars not equal, return false
  let characterCount = {};
  charArray.forEach((char) => {
    if (characterCount[char]) {
      characterCount[char]++;
    } else {
      characterCount[char] = 1;
    }
  });
  for (const key in matchingChars) {
    if (characterCount[key] != characterCount[matchingChars[key]]) {
      console.log("Not matching chars");
      return;
    }
  }

  //Check the order
  let stack = [];
  charArray.forEach((character) => {
    if (stack.length > 0) {
      if (matchingChars[stack[0]] == character) {
        stack = stack.slice(1);
      } else {
        stack.unshift(character);
      }
    } else {
      stack.push(character);
    }
  });
  //After the add remove to the stack
  if (stack.length) {
    console.log("Bad Order");
    return;
  } else {
    console.log("Valid String");
    return;
  }
}

let exStr1 = "[[(({{}}))]]";
let exStr2 = "[{]}";

checkNesting(exStr1);
checkNesting(exStr2);
