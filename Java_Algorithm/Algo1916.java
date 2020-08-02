package Java_Algorithm;

import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.BufferedReader;
import java.util.LinkedList;
import java.util.Queue;

public class Algo1916 {
    static int N;
    static int M;
    static ArrayList<ArrayList<int[]>> arr = new ArrayList<>();
    static int[] dis;
    static Queue<Integer> q = new LinkedList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        dis = new int[N];
        Arrays.fill(dis, 1000000000);

        for (int i = 0; i < N; i++)
            arr.add(new ArrayList<>());

        for (int i = 0; i < M; i++) {
            String[] busInfo = br.readLine().split(" ");
            int start = Integer.parseInt(busInfo[0]);
            int end = Integer.parseInt(busInfo[1]);
            int weight = Integer.parseInt(busInfo[2]);
            arr.get(start - 1).add(new int[] { end, weight });
        }

        String[] tmp = br.readLine().split(" ");
        int from = Integer.parseInt(tmp[0]) - 1;
        int to = Integer.parseInt(tmp[1]) - 1;

        dis[from] = 0;
        q.add(from);

        while (!q.isEmpty()) {
            int st = q.poll();
            for (int[] info : arr.get(st)) {
                int e = info[0] - 1;
                int w = info[1];
                if (dis[e] > dis[st] + w) {
                    q.add(e);
                    dis[e] = dis[st] + w;
                }
            }
        }
        System.out.println(dis[to]);
    }

}