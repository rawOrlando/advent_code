package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
)

func power_surg(octopus_array [][]int, x, y int){
   //down
   if x-1 >= 0 {
      increase_power(octopus_array, x-1, y);
      //down left
      if y-1 >= 0{
         increase_power(octopus_array, x-1, y-1);
      }
      //down right
      if y+1 < len(octopus_array[x-1]) {
         increase_power(octopus_array, x-1, y+1);
      }
   }
   // //up
   if x+1 < len(octopus_array) {
      increase_power(octopus_array, x+1, y);
      //up left
      if y-1 >= 0{
         increase_power(octopus_array, x+1, y-1);
      }
      //up right
      if y+1 < len(octopus_array[x+1]) {
         increase_power(octopus_array, x+1, y+1);
      }
   }
   //left
   if y-1 >= 0{
      increase_power(octopus_array, x, y-1);
   }
   //right
   if y+1 < len(octopus_array[x]){
      increase_power(octopus_array, x, y+1);
   }
}

func increase_power(octopus_array [][]int, x, y int){
   octopus_array[x][y] = octopus_array[x][y] + 1;
   if octopus_array[x][y] == 10{
      power_surg(octopus_array, x, y);
   }
}

func step(octopus_array [][]int) int{
   for x := range octopus_array {
      for y:= range octopus_array[x]{
         increase_power(octopus_array, x, y);
      }
   }
   //Reset and count flasshes
   flash_counts := 0;
   for x := range octopus_array {
      for y:= range octopus_array[x]{
         if octopus_array[x][y] > 9{
            octopus_array[x][y] = 0;
            flash_counts = flash_counts + 1;
         }
      }
   }
   return flash_counts
}


func main() {
   // open file
   f, err := os.Open("day_11_puzzle_input.txt")
   if err != nil {
     log.Fatal(err)
   }
   // remember to close the file at the end of the program
   defer f.Close()

   // read the file line by line using scanner
   scanner := bufio.NewScanner(f)

   scanner.Scan()
   line := scanner.Text()

   //Make rd arrya for ints representing octopuses
   length := len([]rune(line))
   octopus_array := make([][]int, length);
   for i := range octopus_array {
   octopus_array[i] = make([]int, length)
   }

   index_x := 0;
   // Mimics do while
   for ok := true; ok; ok = scanner.Scan() {
     // do something with a line
     fmt.Printf("line: %s\n", scanner.Text())
     for index_y, c := range scanner.Text() {
      octopus_array[index_x][index_y], err = strconv.Atoi(string(c));
     }
     index_x++;
   }

   total := 0
   for i := 0; i<1000; i = i + 1 {
      current_flash := step(octopus_array)
      if current_flash >= len(octopus_array) * len(octopus_array[0]){
         fmt.Printf("Flashes sync on turn: %d\n", i+1)
         break;
      }
      total = total + current_flash
   }
   fmt.Printf("total flashes: %d\n", total)


   if err := scanner.Err(); err != nil {
     log.Fatal(err)
   }
 }