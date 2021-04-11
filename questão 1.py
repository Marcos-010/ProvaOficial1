import random
import timeit


def selection_sort(list_func):
    n = len(list_func)

    for i in range(0, n):
        index_min = i
        for j in range(i + 1, n):
            if list_func[j] < list_func[index_min]:
                index_min = j
        list_func[i], list_func[index_min] = list_func[index_min], list_func[i]
        # temp = list_func[index_min]
        # list_func[index_min] = list_func[i]
        # list_func[i] = temp

    return list_func


def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        insert_value = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > insert_value:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = insert_value
    return lista


if __name__ == '__main__':
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range (1, 4):

        lista = random.sample(range(100_000), 50_000)


        print()
        print(f'Unordered: {lista}')


        ordered_list = selection_sort(lista)
        start_time = timeit.default_timer()
        print(f'Selection Sort:   {ordered_list}')
        selection_sort(lista)
        time1 = timeit.default_timer() - start_time
        print(f' tempo de resposta:{timeit.default_timer() - start_time}')

        print()
        print(f'Unordered: {lista}')

        ordered_list = bubble_sort(lista)
        start_time = timeit.default_timer()
        print(f'bubble_sort:   {ordered_list}')
        bubble_sort(lista)
        time2 = timeit.default_timer() - start_time
        print(f' tempo de resposta:{timeit.default_timer() - start_time}')

        print()
        print(f'Unordered: {lista}')

        ordered_list = insertion_sort(lista)
        start_time = timeit.default_timer()
        print(f'insertion_sort:   {ordered_list}')
        insertion_sort(lista)
        time3 = timeit.default_timer() - start_time
        print(f' tempo de resposta:{timeit.default_timer() - start_time}')

        total1 = time1 + total1
        total2 = time2 + total2
        total3 = time3 + total3

media1 = total1/3
media2 = total2/3
media3 = total3/3

print(f'valor da reposta: {total1}', f'valor da reposta: {total2}', f'valor da reposta: {total3}')

Professor o Insertion_sort tem uma evolução maior de tempo ele será o mais rápido.