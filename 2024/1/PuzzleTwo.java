import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PuzzleTwo {
    public static List<Integer> leftNumbers = new ArrayList<>();
    public static List<Integer> rightNumbers = new ArrayList<>();
    public static void main(String[] args) {
        String filePath = "2024/1/input.txt";
        
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                if (parts.length == 2) {
                    leftNumbers.add(Integer.valueOf(parts[0]));
                    rightNumbers.add(Integer.valueOf(parts[1]));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        long similarity_score = 0;

        for (int num:leftNumbers) {
            similarity_score += (long) num * countOccurrences(num);
        }

        System.out.println(similarity_score);
    }
    
    public static int countOccurrences(int number) {
        int occurrences = 0;
        for (Integer rightNumber : rightNumbers) {
            if (rightNumber.equals(number)) {
                occurrences++;
            }
        }
        return occurrences;
    }
}
