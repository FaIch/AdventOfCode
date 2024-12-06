package day_6;

import java.io.*;
import java.util.*;

public class PuzzleOne {

    public static char[][] map;
    public static Set<String> visitedPositions = new HashSet<>();

    public static void main(String[] args) {
        String filePath = "src/main/java/day_6/input.txt";

        List<char[]> tempList = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                tempList.add(line.toCharArray());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        map = tempList.toArray(new char[0][]);

        findPath();
    }

    static void findPath() {
        int[][] directions = {
                {-1, 0},
                {0, 1},
                {1, 0},
                {0, -1}
        };
        int directionIndex = 0;

        List<Integer> startingPosition = findStartingPosition();
        System.out.println(startingPosition);
        int i = startingPosition.get(0);
        int j = startingPosition.get(1);

        int rows = map.length;
        int cols = map[0].length;

        while (true) {
            String positionKey = i + "," + j;
            visitedPositions.add(positionKey);

            int newI = i + directions[directionIndex][0];
            int newJ = j + directions[directionIndex][1];

            if (newI < 0 || newI >= rows || newJ < 0 || newJ >= cols) break;

            if (map[newI][newJ] == '#') {
                directionIndex = (directionIndex + 1) % 4;
            } else {
                i = newI;
                j = newJ;
            }
        }

        System.out.println(visitedPositions.size());
    }

    static List<Integer> findStartingPosition() {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                char currentChar = map[i][j];
                if (currentChar == '^') {
                    return Arrays.asList(i, j);
                }
            }
        }
        return null;
    }
}
