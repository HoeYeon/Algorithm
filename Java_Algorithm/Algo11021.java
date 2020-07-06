package Java_Algorithm;

import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Algo11021 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            int ans = Integer.parseInt(inputs[0]) + Integer.parseInt(inputs[1]);
            System.out.println("Case #" + (i + 1) + ": " + ans);
        }
    }
}