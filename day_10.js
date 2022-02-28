"use strict";
exports.__esModule = true;
var greet = "Greetings";
var geeks = "GeeksforGeeks";
console.log(greet + " from " + geeks);
var fs = require("fs");
var lines;
var closing_characters = {
    ")": 0,
    "]": 1,
    "}": 2,
    ">": 3
};
var opening_characters = {
    "(": 0,
    "[": 1,
    "{": 2,
    "<": 3
};
var scoring_characters = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
};
var auto_scoring_characters = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
};
function compareNumbers(a, b) {
    return a - b;
}
function do_stuff_with_data(lines) {
    var total = 0;
    var scores = [];
    for (var _i = 0, lines_1 = lines; _i < lines_1.length; _i++) {
        var line = lines_1[_i];
        var score = auto_complete_score_line(line);
        console.log("Line: " + line);
        console.log("Score: " + score);
        if (score > 0) {
            scores.push(score);
        }
    }
    scores = scores.sort(compareNumbers);
    console.log("Score: " + scores);
    console.log("Score: " + scores[Math.round((scores.length - 1) / 2)]);
}
function auto_complete_score_line(line) {
    var stack = [];
    for (var _i = 0, line_1 = line; _i < line_1.length; _i++) {
        var char = line_1[_i];
        if (char in opening_characters) {
            stack.push(opening_characters[char]);
        }
        else if (char in closing_characters) {
            if (stack.pop() != closing_characters[char]) {
                return 0;
            }
        }
    }
    var total = 0;
    while (stack.length > 0) {
        total *= 5;
        total += stack.pop() + 1;
    }
    return total;
}
function score_line(line) {
    var stack = [];
    for (var _i = 0, line_2 = line; _i < line_2.length; _i++) {
        var char = line_2[_i];
        if (char in opening_characters) {
            stack.push(opening_characters[char]);
        }
        else if (char in closing_characters) {
            if (stack.pop() != closing_characters[char]) {
                return scoring_characters[char];
            }
        }
    }
    return 0;
}
function score_line_for_carrots(line) {
}
fs.readFile('day_10_puzzle_input.txt', function (err, data) {
    if (err)
        throw err;
    do_stuff_with_data(data.toString().replace(/\r\n/g, '\n').split('\n'));
});
// todo was there a wau to get data out of this function
