package day_5;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class PuzzleTwo {
    public static void main(String[] args) {
        String filePath = "src/main/java/day_5/input.txt";

        HashMap<String, List<String>> map = new HashMap<>();
        List<List<String>> incorrectOrders = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("|")) {
                    List<String> values = Arrays.asList(line.split("\\|"));
                    String key = values.get(0);
                    String value = values.get(1);
                    map.computeIfAbsent(key, k -> new ArrayList<>());
                    map.get(key).add(value);
                } else {
                    if (line.isBlank()) continue;
                    List<String> order = new ArrayList<>(Arrays.asList(line.split(",")));
                    if (!isCorrectOrder(map, order)) incorrectOrders.add(order);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        List<List<String>> correctOrders = new ArrayList<>();
        for (List<String> order : incorrectOrders) {
            correctOrders.add(correctOrder(map, order));
        }

        findAndPrintSum(correctOrders);
    }

    static boolean isCorrectOrder(HashMap<String, List<String>> map, List<String> order) {
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

    static List<String> correctOrder(HashMap<String, List<String>> map, List<String> order) {
        boolean swapped;

        do {
            swapped = false;

            for (int i = 0; i < order.size() - 1; i++) {
                String current = order.get(i);
                String next = order.get(i + 1);

                if (map.containsKey(current) && map.get(current).contains(next)) {
                    order.set(i, next);
                    order.set(i + 1, current);
                    swapped = true;
                }
            }
        } while (swapped);

        return order;
    }

    static void findAndPrintSum(List<List<String>> orders) {
        int sum = 0;
        for (List<String> order : orders) {
            sum += Integer.parseInt(order.get(order.size() / 2));
        }
        System.out.println(sum);
    }
}
