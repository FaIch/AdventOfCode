package day_2;

import java.io.*;
import java.util.*;

public class PuzzleTwo {
    public static void main(String[] args) {
        String filePath = "src/main/java/day_2/input.txt";
        List<List<String>> listOfLists = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] list = line.split("\\s");
                listOfLists.add(Arrays.asList(list));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        int safe_reports = 0;

        for (List<String> currentList : listOfLists) {
            if (isSafeWithDampener(currentList)) {
                safe_reports++;
            }
        }

        System.out.println("Number of safe reports: " + safe_reports);
    }

    public static boolean isSafeWithDampener(List<String> list) {
        if (isSafe(list)) {
            return true;
        }
        for (int i = 0; i < list.size(); i++) {
            List<String> modifiedList = new ArrayList<>(list);
            modifiedList.remove(i);
            if (isSafe(modifiedList)) {
                return true;
            }
        }
        return false;
    }

    public static boolean isSafe(List<String> list) {
        boolean increasing = true;
        boolean decreasing = true;
        for (int i = 0; i < list.size() - 1; i++) {
            int num_1 = Integer.parseInt(list.get(i));
            int num_2 = Integer.parseInt(list.get(i+1));
            int diff = num_1 - num_2;

            if (Math.abs(diff) < 1 || Math.abs(diff) > 3) {
                return false;
            }

            if (diff < 0) {
                increasing = false;
            }
            if (diff > 0) {
                decreasing = false;
            }
        }

        return increasing || decreasing;
    }
}

