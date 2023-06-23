import java.util.*;
class Solution {
    public int[] solution(int[][] board, int k){
        int[] answer = new int[2];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        int n = board.length;
        int x = 0;
        int y = 0;
        int direction = 0;

        for(int i = 0; i < k; i++){
            if (x + dx[direction] >=  0 && x + dx[direction] < n && y + dy[direction] >= 0 && y + dy[direction] < n) {
                if (board[x + dx[direction]][y + dy[direction]] == 0) {
                    x = x + dx[direction];
                    y = y + dy[direction];
                }
                else{
                    direction = (direction + 1) % 4;
                }
            }
            else{
                direction = (direction + 1) % 4;
            }

        }
        answer[0] = x;
        answer[1] = y;
        return answer;
    }

    public static void main(String[] args){
        Solution T = new Solution();
        int[][] arr1 = {{0, 0, 0, 0, 0},
                {0, 1, 1, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 1, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr1, 10)));
        int[][] arr2 = {{0, 0, 0, 1, 0, 1},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 1},
                {1, 1, 0, 0, 1, 0},
                {0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr2, 20)));
        int[][] arr3 = {{0, 0, 1, 0, 0},
                {0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0},
                {1, 0, 0, 0, 1},
                {0, 0, 0, 0, 0}};
        System.out.println(Arrays.toString(T.solution(arr3, 25)));

    }
}
