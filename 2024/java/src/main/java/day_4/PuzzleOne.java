package day_4;

import java.io.*;
import java.util.*;


public class PuzzleOne {

    static boolean search2D(char[][] grid, int row, int col, String word, int dir) {
        int m = grid.length;
        int n = grid[0].length;

        int len = word.length();
        int[] x = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] y = {-1, 0, 1, -1, 1, -1, 0, 1};

        int currX = row + x[dir], currY = col + y[dir];

        for (int k = 1; k < len; k++) {
            if (currX < 0 || currX >= m || currY < 0 || currY >= n || grid[currX][currY] != word.charAt(k)) {
                return false;
            }
            currX += x[dir];
            currY += y[dir];
        }

        return true;
    }


    static List<int[]> searchWord(char[][] grid, String word) {
        int m = grid.length;
        int n = grid[0].length;

        List<int[]> result = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == word.charAt(0)) {
                    for (int dir = 0; dir < 8; dir++) {
                        if (search2D(grid, i, j, word, dir)) {
                            result.add(new int[]{i, j});
                        }
                    }
                }
            }
        }

        return result;
    }

    static void printResult(int[][] ans) {
        System.out.println(ans.length);
    }


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

        for (int i = 0; i < grid.length; i++) {
            System.out.println(grid[i]);
        }

        String word = "XMAS";
        int[][] ans = searchWord(grid, word).toArray(new int[0][]);

        printResult(ans);
    }
}
