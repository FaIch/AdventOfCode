package day_6;

import java.io.*;
import java.util.*;

public class PuzzleTwo {

    public static char[][] defaultMap;
    public static List<Integer> startingPosition;

    public static void main(String[] args) {
        String filePath = "src/main/java/day_6/input.txt";

        char[][] map;

        List<char[]> tempList = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                tempList.add(line.toCharArray());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        defaultMap = tempList.toArray(new char[0][]);
        map = tempList.toArray(new char[0][]);

        int count = 0;

        startingPosition = findStartingPosition();

        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == '.'){
                    map[i][j] = '#';
                    count += isLoop(map);
                    map[i][j] = '.';
                }
            }
        }
        System.out.println(count);
    }

    static int isLoop(char[][] map) {
        int[][] directions = {
                {-1, 0},
                {0, 1},
                {1, 0},
                {0, -1}
        };
        int directionIndex = 0;

        int i = startingPosition.get(0);
        int j = startingPosition.get(1);

        int rows = map.length;
        int cols = map[0].length;

        int max_steps = 50000;

        for (int k = 0; k < max_steps; k++) {

            int newI = i + directions[directionIndex][0];
            int newJ = j + directions[directionIndex][1];

            if (newI < 0 || newI >= rows || newJ < 0 || newJ >= cols) return 0;

            if (map[newI][newJ] == '#') {
                directionIndex = (directionIndex + 1) % 4;
            } else {
                i = newI;
                j = newJ;
            }
            k++;
        }
        return 1;
    }

    static List<Integer> findStartingPosition() {
        for (int i = 0; i < defaultMap.length; i++) {
            for (int j = 0; j < defaultMap[i].length; j++) {
                char currentChar = defaultMap[i][j];
                if (currentChar == '^') {
                    return Arrays.asList(i, j);
                }
            }
        }
        return null;
    }
}
