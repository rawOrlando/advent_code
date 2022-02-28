#include <iostream>
#include <fstream>

// to do come back and fix this.

using namespace std;

int main() {
  cout << "Hello World!";


  int numbers[100][100];

  for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            numbers[i][j] = 9;
        }
    }

  // Create a text string, which is used to output the text file
  string myText;

  // Read from the text file
  ifstream MyReadFile("day_09_puzzle_input.txt");

  int row_index = 0;
  // Use a while loop together with the getline() function to read the file line by line
  while (getline (MyReadFile, myText)) {
    for (int i = 0; i < myText.size(); i++) {
        numbers[row_index][i] = (int)myText[i];
        cout << myText[i] << "\n";
    }
    row_index++;
  }

  // Close the file
  MyReadFile.close();
  cout << "\nEnd \n";



  return 0;
}