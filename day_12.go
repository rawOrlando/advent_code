package main

import (
	"bufio"
    "fmt"
    "log"
    "os"
)

func main() {
   // open file
   f, err := os.Open("day_12_puzzle_input.txt")
   if err != nil {
     log.Fatal(err)
   }
   // remember to close the file at the end of the program
   defer f.Close()

   // read the file line by line using scanner
   scanner := bufio.NewScanner(f)

   for scanner.Scan() {
     // do something with a line
     fmt.Printf("line: %s\n", scanner.Text())
   }
}

// Tough problem... gonna use python, maybe come bacl and try this later.