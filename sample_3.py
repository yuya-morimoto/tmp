# 課題2-2. 文字列がすべて半角数字だけからなるかどうかを判定する関数を作成する
def includes_only_digits(string):
    # 引数 string: 判定する対象の文字列
    # 戻り値: 半角数字だけからなる文字列であればTrue、そうでないならFalse
    import re
    return bool(re.fullmatch('[0-9]+', string))


# — これより下は書き換えてはいけません —
if __name__ == "__main__":
    # テストケース定義
    test_cases = [
        ("0", True),
        ("1", True),
        ("2", True),
        ("3", True),
        ("4", True),
        ("5", True),
        ("6", True),
        ("7", True),
        ("8", True),
        ("9", True),
        ("01234567890123456789", True),
        (" ", False),
        ("a", False),
        (" 0", False),
        ("0 ", False),
        ("a0", False),
        ("0a", False),
        ("０", False),
        ("１", False),
        ("２", False),
        ("３", False),
        ("４", False),
        ("５", False),
        ("６", False),
        ("７", False),
        ("８", False),
        ("９", False),
        ("01234567890123456789 ", False),
        ("01234567890123456789a", False),
        ]

    # テスト実行
    n_ng = 0
    for case in test_cases:
        string, correct_answer = case
        func_answer = includes_only_digits(string)
        if type(func_answer) is not bool:
            n_ng += 1
            print("NG: includes_only_digits(\"" + string + "\") の戻り値がTrueでもFalseでもありません")
            continue
        if func_answer != correct_answer:
            n_ng += 1
            print("NG: includes_only_digits(\"" + string + "\")=" + str(func_answer))
    if n_ng == 0:
        print("OK")