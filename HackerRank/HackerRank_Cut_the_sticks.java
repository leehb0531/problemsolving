import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class HackerRank_Cut_the_sticks {

    // Complete the cutTheSticks function below.
    static int[] cutTheSticks(int[] arr) {
        int size = arr.length;
        Arrays.sort(arr);
        List<Integer> copy = new ArrayList<>();
        ArrayList<Integer> arrlist1 = new ArrayList<Integer>();
        ArrayList<Integer> result = new ArrayList<>();
        for(int a=0; a<arr.length;a++){
            arrlist1.add(arr[a]);
        }

        for(int a=0; a<arr.length;a++){
            if(!copy.contains(arr[a])){
                result.add(arrlist1.size());
                copy.add(arr[a]);
                arrlist1.removeAll(copy);
            }
            
        }
        int[] resultArray = new int[result.size()];
        for(int i=0; i<result.size();i++){
            resultArray[i] = result.get(i).intValue();
        }
        return resultArray;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int[] result = cutTheSticks(arr);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}