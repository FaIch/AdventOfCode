package day_3;

import java.io.*;
import java.util.*;
import java.util.regex.*;

public class PuzzleTwo {
    public static void main(String[] args) {
        String filePath = "src/main/java/day_3/input.txt";


        String fullString = "";
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                fullString += line;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        int sum = calculateSum(fullString);
        System.out.println(sum);
    }

    public static int calculateSum(String input) {
        Pattern pattern = Pattern.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)|do\\(\\)|don't\\(\\)");
        Matcher matcher = pattern.matcher(input);

        int sum = 0;
        boolean mulEnabled = true;

        List<String> matches = new ArrayList<>();

        while (matcher.find()) {
            matches.add(matcher.group());
        }

        for (String match : matches) {
            if (match.startsWith("mul")) {
                Pattern mulPattern = Pattern.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)");
                Matcher mulMatcher = mulPattern.matcher(match);

                if (mulMatcher.matches()) {
                    int x = Integer.parseInt(mulMatcher.group(1));
                    int y = Integer.parseInt(mulMatcher.group(2));

                    if (mulEnabled) {
                        sum += x * y;
                    }
                }
            } else if (match.equals("do()")) {
                mulEnabled = true;
            } else if (match.equals("don't()")) {
                mulEnabled = false;
            }
        }

        return sum;
    }
}
