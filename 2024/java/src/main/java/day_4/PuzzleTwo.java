package day_4;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class PuzzleTwo {
    public static void main(String[] args) {
        String filePath = "src/main/java/day_4/input.txt";

        ArrayList<char[]> gridList = new ArrayList<>();


        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                gridList.add(line.toCharArray());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        char[][] grid = gridList.toArray(new char[gridList.size()][]);

        findXMAS(grid);
    }

    static void findXMAS(char[][] grid) {
        int timesFound = 0;

        for (int i = 1; i < grid.length - 1; i++) {
            for (int j = 1; j < grid[i].length - 1; j++) {
                char currentChar = grid[i][j];
                if (currentChar == 'A') {
                    if(isXMAS(grid, i, j)) timesFound++;
                }
            }
        }
        System.out.println(timesFound);
    }

    static boolean isXMAS(char[][] grid, int i, int j){
        char topleft = grid[i-1][j-1];
        char topright = grid[i-1][j+1];
        char bottomleft = grid[i+1][j-1];
        char bottomright = grid[i+1][j+1];
        if (topleft == 'M' && bottomright == 'S' || topleft =='S' && bottomright == 'M'){
            return topright == 'M' && bottomleft == 'S' || topright == 'S' && bottomleft == 'M';
        }
        return false;
    }
}
