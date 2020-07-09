package Java_Algorithm;

import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Algo18258 {
    public static void main(String[] args) throws Exception {
        Queue q = new Queue();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < N; i++) {
            String[] arg = br.readLine().split(" ");
            if (arg[0].equals("push")) {
                q.push(Integer.parseInt(arg[1]));
            } else if (arg[0].equals("pop")) {
                ans.append(q.pop() + "\n");
            } else if (arg[0].equals("size")) {
                ans.append(q.getSize() + "\n");
            } else if (arg[0].equals("empty")) {
                ans.append(q.empty() + "\n");
            } else if (arg[0].equals("front")) {
                ans.append(q.getFront() + "\n");
            } else if (arg[0].equals("back")) {
                ans.append(q.getBack() + "\n");
            }
        }
        System.out.println(ans);

    }
}

class Queue {
    final static int MAX_SIZE = 2000000;
    private int front;
    private int back;
    private int[] q;
    private int size;

    Queue() {
        this.q = new int[MAX_SIZE];
        this.front = -1;
        this.back = -1;
        this.size = 0;
    };

    public void push(int X) {
        this.back = (this.back + 1) % MAX_SIZE;
        this.q[this.back] = X;
        this.size++;
    }

    public int pop() {
        if (this.empty() == 1) {
            return -1;
        }
        this.size--;
        this.front = (this.front + 1) % MAX_SIZE;
        return this.q[this.front];
    }

    public int getSize() {
        return this.size;
    }

    public int empty() {
        return this.back == this.front && this.size == 0 ? 1 : 0;
    }

    public int getFront() {
        return this.empty() == 1 ? -1 : this.q[(this.front + 1) % MAX_SIZE];
    }

    public int getBack() {
        return this.empty() == 1 ? -1 : this.q[this.back];
    }
}