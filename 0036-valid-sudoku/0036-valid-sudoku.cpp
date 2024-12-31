class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<pair<int, char>> rowElement;
        vector<pair<char, int>> elementCol;
        vector<tuple<int, int, char>> boxElement;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char element = board[i][j];
                if (element != '.') {
                    rowElement.push_back({i, element});
                    elementCol.push_back({element, j});
                    boxElement.push_back(make_tuple(i / 3, j / 3, element));
                }
            }
        }

        // Combine all the entries into a single set for uniqueness check
        set<pair<int, char>> uniqueRowElement(rowElement.begin(), rowElement.end());
        set<pair<char, int>> uniqueElementCol(elementCol.begin(), elementCol.end());
        set<tuple<int, int, char>> uniqueBoxElement(boxElement.begin(), boxElement.end());

        // Ensure that all sets have the same size as their respective vectors
        return rowElement.size() == uniqueRowElement.size() &&
               elementCol.size() == uniqueElementCol.size() &&
               boxElement.size() == uniqueBoxElement.size();
    }
};
