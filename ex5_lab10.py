# когда мы задаём функцию, выполнение которой мы хотим разделить между некоторым
# количеством процессов, мы должны написать её аргументы
# если у функции нет аргументов, то надо её писать с пустыми скобками: target=worker()
# (в нашем случае)
# когда же у нас есть ннепосредственно заданные аргументы, то мы их можем указать как
# в круглых скобках самой функции, так и после самой функции с помощью args = ...
# (в этом случае мы пишем функцию без круглых скобок) (как было в лабе примером выше)

import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [multiprocessing.Process(target=worker()) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)

# сейчас код исправен и лист не пуст