import os, functools


def examine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if kwargs['examine']:
            count, output = 1, []
            folder_path = os.getcwd()
            while os.path.isfile(f"{folder_path}/out{count}.txt"):
                f = open(f"{folder_path}/out{count}.txt", 'r')
                temp = []
                for line in f.readlines():
                    if line.strip():
                        temp.append(line.strip())
                output.append(temp)
                count += 1

            success_count = 0
            for i, o in enumerate(output, start=1):
                func_output = function(**kwargs, folder_path=os.getcwd(), id=i)
                if func_output == o:
                    success_count += 1
                    print(f"#{i} = success!!")
                else:
                    print(f"#{i} = not success!!")
                    print(f"function(): {func_output}")
                print(f"output: {o}")
            print(f"success: {success_count} / {len(output)}")
        else:
            return function(*args, **kwargs)

    return wrapper