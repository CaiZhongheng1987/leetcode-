# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
# 示例 1:
#
# 输入:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
# 示例 2:
#
# 输入:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
#      但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
# 说明:
#
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 给定数独序列只包含数字 1-9 和字符 '.' 。
# 给定数独永远是 9x9 形式的。


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 先建立空字典，存储行、列、小方块的数字
        rows_list = [dict() for _ in range(9)]
        cols_list = [dict() for _ in range(9)]
        rect_list = [dict() for _ in range(9)]

        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] != '.':
                    # 根据row_idx和col_idx判断在哪个小方块里面， 有数字才记录
                    rect_idx = col_idx // 3 + (row_idx // 3) * 3
                    # 判断行是否匹配
                    if board[row_idx][col_idx] not in rows_list[row_idx]:
                        # 如果没有的话，就存入字典，将频次记为1
                        rows_list[row_idx][board[row_idx][col_idx]] = 1
                    else:
                        # 如果碰上相同的，那这个数独就无效
                        return False

                    # 判断列是否匹配
                    if board[row_idx][col_idx] not in cols_list[col_idx]:
                        # 如果没有的话，就存入字典，将频次记为1
                        cols_list[col_idx][board[row_idx][col_idx]] = 1
                    else:
                        # 如果碰上相同的，那这个数独就无效
                        return False

                    # 判断小方块是否匹配
                    if board[row_idx][col_idx] not in rect_list[rect_idx]:
                        # 如果没有的话，就存入字典，将频次记为1
                        rect_list[rect_idx][board[row_idx][col_idx]] = 1
                    else:
                        # 如果碰上相同的，那这个数独就无效
                        return False

        return True


# main test script
test_list = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

my_test = Solution()

return_result = my_test.isValidSudoku(test_list)
print(return_result)
