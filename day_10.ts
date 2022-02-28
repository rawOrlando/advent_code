var greet: string = "Greetings";
var geeks: string = "GeeksforGeeks";
console.log(greet + " from " + geeks);

import * as fs from 'fs';
var lines;

let closing_characters = {
    ")": 0,
    "]": 1,
    "}": 2,
    ">": 3
}

let opening_characters = {
    "(": 0,
    "[": 1,
    "{": 2,
    "<": 3
}

let scoring_characters = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

let auto_scoring_characters = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

function compareNumbers(a, b) {
  return a - b;
}

function do_stuff_with_data(lines)
{
    let total: number = 0;
    let scores: number[] = [];
    for(let line of lines)
    {
        let score = auto_complete_score_line(line)
        console.log("Line: " + line);
        console.log("Score: " + score);
        if (score > 0)
        {
            scores.push(score)
        }
    }
    scores = scores.sort(compareNumbers);
    console.log("Score: " + scores);
    console.log("Score: " + scores[Math.round((scores.length - 1) / 2)]);
}

function auto_complete_score_line(line)
{
    var stack = [];
    for(let char of line)
    {
        if (char in opening_characters)
        {
            stack.push(opening_characters[char])

        }
        else if (char in closing_characters)
        {
            if (stack.pop() != closing_characters[char])
            {
                return 0
            }
        }
    }
    let total: number = 0;
    while (stack.length > 0)
    {
        total *= 5
        total += stack.pop() + 1
    }
    return total
}
function score_line(line)
{
    var stack = [];
    for(let char of line)
    {
        if (char in opening_characters)
        {
            stack.push(opening_characters[char])

        }
        else if (char in closing_characters)
        {
            if (stack.pop() != closing_characters[char])
            {
                return scoring_characters[char]
            }
        }
    }
    return 0
}

function score_line_for_carrots(line)
{

}

fs.readFile('day_10_puzzle_input.txt', function(err, data) {
    if(err) throw err;

    do_stuff_with_data(data.toString().replace(/\r\n/g,'\n').split('\n'));

});
// todo was there a wau to get data out of this function

