package day_3;

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class PuzzleOne {
    public static void main(String[] args) {
        String filePath = "src/main/java/day_3/input.txt";
        List<String> matches = new ArrayList<>();

        String regex = "mul\\((\\d{1,3}),(\\d{1,3})\\)";

        Pattern pattern = Pattern.compile(regex);

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                Matcher matcher = pattern.matcher(line);
                while (matcher.find()) {
                    matches.add(matcher.group());
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        long sum = multiplyAndAdd(matches);
        System.out.println(sum);
    }

    public static long multiplyAndAdd(List<String> list) {
        long sum = 0;

        String regex = "(\\d{1,3})";
        Pattern pattern = Pattern.compile(regex);

        List<Integer> numbers = new ArrayList<>();

        for (String string:list) {
            Matcher matcher = pattern.matcher(string);
            while (matcher.find()) {
                numbers.add(Integer.valueOf(matcher.group()));
            }
        }

        for (int i = 0; i < numbers.size() - 1; i+=2){
            sum += (long) numbers.get(i) * numbers.get(i+1);
        }

        return sum;
    }
}
