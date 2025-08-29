import java.util.*;

class Solution {
    private void bfsRemove(char[][] grid, char target){
        int h = grid.length, w = grid[0].length;
        boolean[][] visited = new boolean[h][w];
        ArrayDeque<int[]> q = new ArrayDeque<>();

        // 테두리에서 시작점 등록 (좌우)
        for (int i = 0; i < h; i++) {
            touch(i, 0, grid, target, visited, q);
            touch(i, w - 1, grid, target, visited, q);
        }
        // 테두리에서 시작점 등록 (상하)
        for (int j = 0; j < w; j++) {
            touch(0, j, grid, target, visited, q);
            touch(h - 1, j, grid, target, visited, q);
        }

        int[][] d = { {1,0}, {-1,0}, {0,1}, {0,-1} };
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            for (int[] dd : d) {
                int nx = x + dd[0], ny = y + dd[1];
                if (nx < 0 || ny < 0 || nx >= h || ny >= w || visited[nx][ny]) continue;

                if (grid[nx][ny] == '.') {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                } else if (grid[nx][ny] == target) {
                    grid[nx][ny] = '.';          // 타깃 제거 → 공기
                    visited[nx][ny] = true;
                }
                // 다른 글자는 벽
            }
        }
    }

    private void touch(int i, int j, char[][] grid, char target, boolean[][] visited, ArrayDeque<int[]> q){
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || visited[i][j]) return;
        if (grid[i][j] == '.') {
            visited[i][j] = true;
            q.offer(new int[]{i, j});
        } else if (grid[i][j] == target) {
            grid[i][j] = '.';
            visited[i][j] = true;
        }
    }

    public int solution(String[] storage, String[] requests) {
        int h = storage.length;
        int w = storage[0].length();

        // 가변 그리드로 변경
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) grid[i] = storage[i].toCharArray();

        // 요청 처리
        for (String req : requests) {
            if (req.length() == 2 && req.charAt(0) == req.charAt(1)) {
                // 알파벳 2개(크레인): 전부 제거
                char target = req.charAt(0);
                for (int i = 0; i < h; i++) {
                    for (int j = 0; j < w; j++) {
                        if (grid[i][j] == target) grid[i][j] = '.';
                    }
                }
            } else if (req.length() == 1) {
                // 알파벳 1개(지게차): 외부 공기 BFS로 닿는 것만 제거
                char target = req.charAt(0);
                bfsRemove(grid, target);
            } // 그 외 입력 형태는 문제 조건상 없음
        }

        // 남은 컨테이너 수 세기
        int remain = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (grid[i][j] != '.') remain++;
            }
        }
        return remain;
    }
}
