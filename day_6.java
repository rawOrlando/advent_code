import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.net.URL;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.*;

public class day_6 {

    private class LaternFish {
        int days;

        // public LaternFish()
        // {
        //     return new LaternFish(8);
        // }

        public LaternFish(int days)
        {
            this.days = days;
        }

        public void advance_day()
        {
            this.days--;
        }

        public boolean should_reproduce()
        {
            return this.days < 1;
        }

        public LaternFish reproduce()
        {
            this.days = 7;
            return new LaternFish(9);
        }

    }

    public static void main(String args[]) {
        day_6 program = new day_6();
        program.run();
    }

    public void run()
    {
        System.out.println("Day 6!");
        List<LaternFish> fish = new ArrayList<LaternFish>();

        long[] fish_counts = {0,0,0,0,0,0,0,0,0};

        try {
            //URL url = day_6.class.getResource("day_6_puzzle_input.txt");
            File file = new File("day_6_puzzle_input.txt");

            // Note:  Double backquote is to avoid compiler
            // interpret words
            // like \test as \t (ie. as a escape sequence)

            // Creating an object of BufferedReader class
            BufferedReader br
                = new BufferedReader(new FileReader(file));

            // // It is all on one line
            String st = br.readLine();
            String[] numbers = st.split("[,]", 0);
            for (int i = 0; i < numbers.length; i++)
            {
                int days = Integer.parseInt(numbers[i]);
                fish.add(new LaternFish(days));
                fish_counts[days] += 1;
            }

            br.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        for (int day = 0; day < 256; day++)
        {
            long[] new_fish_counts = {0,0,0,0,0,0,0,0,0};
            new_fish_counts[0] = fish_counts[1];
            new_fish_counts[1] = fish_counts[2];
            new_fish_counts[2] = fish_counts[3];
            new_fish_counts[3] = fish_counts[4];
            new_fish_counts[4] = fish_counts[5];
            new_fish_counts[5] = fish_counts[6];
            new_fish_counts[6] = fish_counts[7] + fish_counts[0];
            new_fish_counts[7] = fish_counts[8];
            new_fish_counts[8] = fish_counts[0];
            fish_counts = new_fish_counts;
        }
        long total = (fish_counts[0] + fish_counts[1] +
            fish_counts[2] + fish_counts[3] + fish_counts[4] +
            fish_counts[5] + fish_counts[6] + fish_counts[7] +
            fish_counts[8]);

        System.out.println(total);
        for (int i = 0; i < fish_counts.length; i++)
        {
            System.out.println(fish_counts[i]);
        }


        // int total = 0;
        // for (int j = 0; j < int_fish.size(); j++)
        // {
        //     List<Integer> these_fish = new ArrayList<Integer>();
        //     these_fish.add(int_fish.get(j));
        //     for (int day = 0; day < 256; day++)
        //     {
        //         for (int i = 0; i < these_fish.size(); i++)
        //         {
        //             Integer cur_fish = these_fish.get(i);
        //             if(cur_fish < 1)
        //             {
        //                 cur_fish = 7;
        //                 these_fish.add(9);
        //             }

        //             these_fish.set(i, cur_fish - 1);
        //         }
        //     }
        //     total += these_fish.size();
        // }
        // System.out.println(total);
    }
}