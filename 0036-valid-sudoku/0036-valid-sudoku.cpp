class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // 使用布林陣列來追蹤數字是否出現過
        bool rows[9][9] = {false};
        bool cols[9][9] = {false};
        bool boxes[9][9] = {false};

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char value = board[i][j];
                if (value == '.') continue;

                int num = value - '1'; // 將 '1'-'9' 映射為 0-8
                int boxIndex = (i / 3) * 3 + j / 3;

                // 檢查是否重複
                if (rows[i][num] || cols[j][num] || boxes[boxIndex][num]) {
                    return false;
                }

                // 標記該數字為已出現
                rows[i][num] = cols[j][num] = boxes[boxIndex][num] = true;
            }
        }
        return true;
    }
};