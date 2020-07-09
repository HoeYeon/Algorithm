package Java_Algorithm;

import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Algo2523 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        StringBuilder ans = new StringBuilder();
        for (int i = 1; i < n * 2; i++) {
            int loop = i <= n ? i : n - (i % n);
            for (int j = 0; j < loop; j++)
                ans.append('*');
            ans.append('\n');
        }
        System.out.print(ans);
    }
}