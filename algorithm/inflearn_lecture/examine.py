import sys, os
def examine(function):
    def wrapper():
        count, output = 1, []
        folder_path = os.getcwd()
        while os.path.isfile(f"{folder_path}/out{count}.txt"):
            f = open(f"{folder_path}/out{count}.txt", 'r')
            for line in f.readlines():
                output.append(line)

        for i, o in enumerate(output):
            input_args = []
            f = open(f"{folder_path}/in{i}.txt", 'r')
            for line in f.readlines():
                input_args.append(line)
            if function(input_args) == o:
                print("success!!")
            else:
                print("not success!!")
    return wrapper

sys.stdin = open("input.txt", "rt")  # 파일 읽는 방법을 찾아서 넣어두어야겠다.

# 이걸 데코레이터로 만드는 것도 방법일 것 같다는 생각이 든다.
# 결과 저장
# while 파일 존재
# 파일 오픈
# 함수 실행