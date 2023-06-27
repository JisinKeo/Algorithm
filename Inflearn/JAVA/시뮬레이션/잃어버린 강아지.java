class Solution {
    public int solution(int[][] board){
        int answer = 0;

        int personX = 0;
        int personY = 0;
        int dogX = 0;
        int dogY = 0;

        for(int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++){
                if(board[i][j] == 2){
                    personX = i;
                    personY = j;
                    board[i][j] = 0;
                }
                else if(board[i][j] == 3){
                    dogX = i;
                    dogY = j;
                    board[i][j] = 0;
                }
            }
        }

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        int direction_person = 0;
        int direction_dog = 0;

        while (answer <= 10000) {


            if (personX == dogX && personY == dogY){
                return answer;
            }

            if (personX + dx[direction_person] >= 0 && personX + dx[direction_person] < 10 && personY + dy[direction_person] >= 0 && personY + dy[direction_person] < 10){
                if(board[personX + dx[direction_person]][personY + dy[direction_person]] == 0){
                    personX += dx[direction_person];
                    personY += dy[direction_person];
                }
                else if(board[personX + dx[direction_person]][personY + dy[direction_person]] == 1){
                    direction_person = (direction_person + 1) % 4;
                }
            }
            else{
                direction_person = (direction_person + 1) % 4;
            }

            if (dogX + dx[direction_dog] >= 0 && dogX + dx[direction_dog] < 10 && dogY + dy[direction_dog] >= 0 && dogY + dy[direction_dog] < 10){
                if(board[dogX + dx[direction_dog]][dogY + dy[direction_dog]] == 0){
                    dogX += dx[direction_dog];
                    dogY += dy[direction_dog];
                }
                else if(board[dogX + dx[direction_dog]][dogY + dy[direction_dog]] == 1){
                    direction_dog = (direction_dog + 1) % 4;
                }
            }
            else{
                direction_dog = (direction_dog + 1) % 4;
            }


            answer += 1;
        }

        return 0;
    }

    public static void main(String[] args){
        Solution T = new Solution();
        int[][] arr1 = {{0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 2, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 3, 0, 0, 0, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 0}};
        System.out.println(T.solution(arr1));
        int[][] arr2 = {{1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 1, 1, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 0},
                {1, 0, 0, 0, 0, 0, 1, 0, 1, 0},
                {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 1, 0, 0, 0, 0, 0, 2, 1},
                {0, 0, 0, 1, 0, 1, 0, 0, 0, 1},
                {0, 1, 0, 1, 0, 0, 0, 0, 0, 3}};
        System.out.println(T.solution(arr2));
    }
}
