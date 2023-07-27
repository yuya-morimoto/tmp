# 課題2-3. 半角数字だけからなる文字列を整数のリストに変換する関数を作成する
def convert_digitstring_to_list(string):
    # 引数 string: 変換する対象の半角数字だけからなる文字列
    # 戻り値: 変換後の整数のリスト
    return [int(i) for i in string]


# — これより下は書き換えてはいけません —
if __name__ == "__main__":
    # テストケース定義
    test_cases = [
        ("0", [0]),
        ("1", [1]),
        ("2", [2]),
        ("3", [3]),
        ("4", [4]),
        ("5", [5]),
        ("6", [6]),
        ("7", [7]),
        ("8", [8]),
        ("9", [9]),
        ("0000", [0, 0, 0, 0]),
        ("1234", [1, 2, 3, 4]),
        ("01234567890123456789", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ]
    # テスト実行
    n_ng = 0
    for case in test_cases:
        string, correct_answer = case
        func_answer = convert_digitstring_to_list(string)
        if type(func_answer) is not list:
            n_ng += 1
            print("NG: convert_digitstring_to_list(\"" + string + "\") の戻り値がリスト型ではありません")
            continue
        if len(func_answer) != len(correct_answer):
            n_ng += 1
            print("NG: len(convert_digitstring_to_list(\"" + string + "\"))=" + str(len(func_answer)))
            continue
        for index in range(len(func_answer)):
            if func_answer[index] != correct_answer[index]:
                n_ng += 1
                print("NG: convert_digitstring_to_list(\"" + string + "\")[" + str(index) + "]=" + str(func_answer[index]))
    if n_ng == 0:
        print("OK")