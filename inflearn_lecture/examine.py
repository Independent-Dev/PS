import os, functools


def examine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if kwargs['examine']:
            count, output = 1, []
            folder_path = os.getcwd()
            while os.path.isfile(f"{folder_path}/out{count}.txt"):
                f = open(f"{folder_path}/out{count}.txt", 'r')
                for line in f.readlines():
                    if line.strip():
                        output.append(line.split())
                count += 1

            for i, o in enumerate(output, start=1):
                func_output = function(**kwargs, folder_path=os.getcwd(), id=i)
                if func_output == o:
                    print(f"#{i} = success!!")
                else:
                    print(f"#{i} = not success!!")
                    print(f"function(): {func_output}")
                print(f"output: {o}")
        else:
            return function(*args, **kwargs)

    return wrapper