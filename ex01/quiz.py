
import random
import time

def shutudai(qa_list):
    qa = random.choice(qa_list)
    print("問題:"+qa["q"])
    return qa ["a"]


def kaitou(asa_lst):
    ans = input("答えるんだ") 
    st = datetime.datetime.now
    ed = datetime.datetime.now

    if ans in ans_lst:
        print("正解")
    else:
        print("出直してこいや")

    print("解答時間:"+(ed-st).seconds)






if __name__=="__main__":
    qa_lst=[

        {"q":"サザエさんの旦那の名前は？","a":["マスオ","ますお"] }
        {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"] }
        {"q":"タラオはカツオから見てどんな関係？","a":["甥","甥っこ","おい"] }
    ]

    asa=











