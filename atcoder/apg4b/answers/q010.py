Student_number = int(input()) #生徒の数

Test_score = list(map(int,input().split())) #生徒の点数を受け取る

Total = sum(Test_score) #合計する

Test_score_average = Total // Student_number #平均点を求める（小数点切り捨てのため//）

for i in range(Student_number):#平均点からの差

    if Test_score[i] > Test_score_average:
        print(Test_score[i] - Test_score_average)
        
    else:
        print(Test_score_average - Test_score[i])


