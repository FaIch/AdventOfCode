package day_5;

import java.io.*;
import java.util.*;

public class PuzzleOne {
    public static void main(String[] args) {
        String filePath = "src/main/java/day_5/input.txt";

        HashMap<String, List<String>> map = new HashMap<>();
        List<List<String>> correctOrders = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("|")) {
                    List<String> values = List.of(line.split("\\|"));
                    String key = values.get(0);
                    String value = values.get(1);
                    map.computeIfAbsent(key, k -> new ArrayList<>());
                    map.get(key).add(value);
                }
                else {
                    if (line.isBlank()) continue;
                    List<String> order = List.of(line.split(","));
                    if (correctOrder(map, order)) correctOrders.add(order);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        findAndPrintSum(correctOrders);
    }

    static boolean correctOrder(HashMap<String, List<String>> map, List<String> order) {
        HashMap<String, Integer> pageIndices = new HashMap<>();
        for (int i = 0; i < order.size(); i++) {
            pageIndices.put(order.get(i), i);
        }

        for (String key : map.keySet()) {
            if (!pageIndices.containsKey(key)) continue;

            int keyIndex = pageIndices.get(key);

            for (String value : map.get(key)) {
                if (!pageIndices.containsKey(value)) continue;

                int valueIndex = pageIndices.get(value);

                if (keyIndex >= valueIndex) {
                    return false;
                }
            }
        }

        return true;
    }

    static void findAndPrintSum(List<List<String>> orders) {
        int sum = 0;
        for (List<String> order: orders) {
            sum += Integer.parseInt(order.get((order.size()/2)));
        }
        System.out.println(sum);
    }
}
