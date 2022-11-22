import random
import time

#グローバル変数定義
num_of_alphabet = 26 #全アルファベット数
num_of_all_chars = 10 #対象文字数
num_of_abs_chars = 2 #欠損文字数
num_of_trials = 2 #最大繰り返し回数

def shutudai(alphabet):
    #全アルファベットから対象文字を10個選択する。(重複なし)
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字：")
    for c in all_chars:
        print(c, end=" ")
    print()

    #対象文字から欠損文字を2個選択する。(重複なし)
    abs_chars = random.sample(all_chars, num_of_abs_chars)
    print("欠損文字(デバッグ用)：")
    for c in abs_chars:
        print(c, end=" ")
    print()

    print("表示文字：")
    for c in all_chars:
        #abs_chars に含まれていなければ表示文字として表示する
        if c not in abs_chars:
           print(c, end=" ")
    print()

    return abs_chars


def kaitou(abs_chars):
    num = int(input("欠損文字はいくつあるでしょうか？："))
    if num != num_of_abs_chars:
        print("不正解です。")
    else:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください。")
        for i in range(num):
            ans = input(f"{i + 1}つ目の文字を入力してください：")
            if ans not in abs_chars:
                print("不正解です。")
                return False
            else:
                abs_chars.remove(ans)

        print("全部正解です。")
        return True
            

if __name__ == "__main__":
    st = time.time()
    alphabet = [chr(i + 65) for i in range(num_of_alphabet)]
    print(alphabet)
    for _ in range(num_of_trials):
        abs_chars = shutudai(alphabet)
        ret = kaitou(abs_chars)
        if ret:
            break
        else:
            print("-"*20)

    ed = time.time()
    print(f"所要時間：{(ed-st):.2f}秒")