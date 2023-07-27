import random

# 課題2-1. 0～9の範囲のランダムな整数を指定された個数分持つリストを生成する関数を作成する
def generate_random_digits(nod):
    # 引数 nod: 戻り値のリストの長さ
    # 戻り値: 整数0～9の範囲でランダムに選ばれた整数を要素に持つリスト
    result = []
    for i in range(nod):
        result.append(random.randint(0, 9))
    return result


# — これより下は書き換えてはいけません —
if __name__ == "__main__":
    # テストケース定義
    test_cases = [1, 2, 3, 4, 5, 6, 30]

    # テスト実行
    random.seed(0)
    n_ng = 0
    for nod in test_cases:
        digits = generate_random_digits(nod)
        if type(digits) is not list:
            n_ng += 1
            print("NG: generage_random_digits(" + str(nod) + ") の戻り値がリスト型ではありません")
        elif len(digits) != nod:
            n_ng += 1
            print("NG: len(generage_random_digits(" + str(nod) + "))=" + str(len(digits)))
    if n_ng == 0:
        for nod in test_cases:
            c_digits = [0] * 10
            n_trial = 100
            for i_trial in range(n_trial):
                digits = generate_random_digits(nod)
                for i_digit in range(len(digits)):
                    if type(digits[i_digit]) is not int:
                        n_ng += 1
                        print("NG: 試行#" + str(i_trial) + ": generage_random_digits(" + str(nod) + ")[" + str(i_digit) + "] が整数型ではありません")
                    elif (digits[i_digit] < 0) or (digits[i_digit] > 9):
                        n_ng += 1
                        print("NG: 試行#" + str(i_trial) + ": generage_random_digits(" + str(nod) + ")[" + str(i_digit) + "]=" + str(digits[i_digit]) + "（0～9の範囲内にありません）")
                    else:
                        c_digits[digits[i_digit]] += 1
            print(c_digits)
            for i_digit in range(10):
                if c_digits[i_digit] == 0:
                    n_ng += 1
                    print("NG: generage_random_digits(" + str(nod) + ")の出力リストに" + str(i_digit) + "が含まれないようです（" + str(n_trial) + "回試行した結果）")
    if n_ng == 0:
        print("OK")