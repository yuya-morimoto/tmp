# 4. ヒットの数を数える
def count_hits(l_parent, l_child):
    # 引数 l_parent: 親が考えた数字列に対応する整数のリスト
    # 引数 l_child: 子が考えた数字列に対応する整数のリスト
    # 戻り値: ヒット数
    hit = 0
    for i in range(len(l_parent)):
        hit += 1 if l_parent[i] == l_child[i] else 0

    return hit


# — これより下は書き換えてはいけません —
if __name__ == "__main__":
    # テストケース定義
    test_cases = [
        ([0], [1], 0),
        ([0], [0], 1),
        ([0, 1], [0, 0], 1),
        ([0, 1], [0, 1], 2),
        ([0, 1], [1, 0], 0),
        ([0, 1], [1, 1], 1),
        ([1, 2, 3, 4], [1, 2, 3, 4], 4),
        ([1, 2, 3, 4], [1, 2, 3, 3], 3),
        ([1, 2, 3, 4], [1, 2, 2, 2], 2),
        ([1, 2, 3, 4], [1, 1, 1, 1], 1),
        ([1, 1, 1, 1], [1, 2, 3, 4], 1),
        ([1, 1, 1, 1], [4, 3, 2, 1], 1),
        ([4, 9, 4, 5], [1, 2, 3, 4], 0),
        ([4, 9, 4, 5], [1, 2, 4, 3], 1),
        ([4, 1, 1, 9], [9, 4, 3, 9], 1),
        ([4, 3, 1, 9], [1, 1, 2, 9], 1),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10)
        ]
# テスト実行
    n_ng = 0
    for case in test_cases:
        l_parent, l_child, correct_answer = case
        func_answer = count_hits(l_parent, l_child)
        if type(func_answer) is not int:
            n_ng += 1
            print("NG: count_hits(", l_parent, ",", l_child, ") の戻り値が整数型ではありません")
            continue
        if func_answer != correct_answer:
            n_ng += 1
            print("NG: count_hits(", l_parent, ",", l_child, ")=", func_answer)
    if n_ng == 0:
        print("OK")