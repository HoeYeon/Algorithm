package Java_Algorithm;

import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Algo3184 {
    public static char[][] arr;
    public static int[][] check;
    public static int wolf = 0, sheep = 0, row, col, S = 0, W = 0, escape = 0;
    public static int[][] go = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] s = bf.readLine().split(" ");
        row = Integer.parseInt(s[0]);
        col = Integer.parseInt(s[1]);
        arr = new char[row][col];
        check = new int[row][col];
        for (int i = 0; i < row; i++) {
            String line = bf.readLine();
            for (int j = 0; j < col; j++) {
                arr[i][j] = line.charAt(j);
                check[i][j] = 0;
                if (line.charAt(j) == 'o')
                    S++;
                if (line.charAt(j) == 'v')
                    W++;
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (check[i][j] == 0 && arr[i][j] != '#') {
                    check[i][j] = 1;
                    if (arr[i][j] == 'o')
                        sheep++;
                    if (arr[i][j] == 'v')
                        wolf++;
                    dfs(i, j);
                    if (sheep == 0 || wolf == 0) {
                        sheep = 0;
                        wolf = 0;
                        continue;
                    } else if (sheep > wolf)
                        W -= wolf;
                    else
                        S -= sheep;
                    sheep = 0;
                    wolf = 0;
                }
            }
        }
        System.out.println(Integer.toString(S) + " " + Integer.toString(W));

    }

    public static void dfs(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int xx = go[i][0];
            int yy = go[i][1];
            if (x + xx >= 0 && x + xx < row && y + yy >= 0 && y + yy < col && check[x + xx][y + yy] == 0
                    && arr[x + xx][y + yy] != '#') {
                check[x + xx][y + yy] = 1;
                if (arr[x + xx][y + yy] == 'o')
                    sheep++;
                if (arr[x + xx][y + yy] == 'v')
                    wolf++;
                dfs(x + xx, y + yy);
            }
        }
    }
}