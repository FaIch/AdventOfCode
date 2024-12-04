package day_1;

import java.io.*;
import java.util.ArrayList;
import java.util.*;

public class PuzzleOne {
    public static void main(String[] args) {
        String filePath = "src/main/java/day_1/input.txt";

        List<Integer> leftNumbers = new ArrayList<>();
        List<Integer> rightNumbers = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                leftNumbers.add(Integer.valueOf(parts[0]));
                rightNumbers.add(Integer.valueOf(parts[1]));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        Collections.sort(leftNumbers);
        Collections.sort(rightNumbers);

        int total_distance = 0;

        for (int i = 0; i < leftNumbers.size(); i++) {
            total_distance += Math.abs(leftNumbers.get(i) - rightNumbers.get(i));
        }

        System.out.println(total_distance);
    }
}