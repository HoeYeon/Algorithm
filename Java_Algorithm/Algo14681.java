package Java_Algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Algo14681 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        if (a > 0) {
            System.out.println(b > 0 ? 1 : 4);
        } else {
            System.out.println(b > 0 ? 2 : 3);
        }
    }
}