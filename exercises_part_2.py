import numpy


def count_a_number(numbers, number):
    count = 0
    for num in numbers:
        if num == number:
            count += 1
    return count


print("Number of equal numbers: ", count_a_number([1, 4, 5, 7, 4, 6, 8], 4))

print("-" * 80)


def play_with_lists(numbers, number):
    reversed_list = numbers.copy()
    reversed_list.reverse()
    print("The reversed list: ", reversed_list)

    new_list = numbers
    i = new_list.index(number)
    new_list[i] = 1
    print("The new list with 'number' replaced by 1:", new_list)

    sorted_list = numbers
    sorted_list = sorted(numbers, reverse=True)
    #sorted_list.sort(reverse=True)
    print("The sorted list:", sorted_list, "\n", numbers)
    """The difference between sort() and sorted() is that sort() changes the whole list without saving the old list
    and sorted() just copy the old list and sorts it than.
    I chose sorted() so that the old list is not overwritten."""


play_with_lists([1, 4, 3, 9, 6, 8, 2, 5, 7], 4)

print("-" * 80)


def compare_lists(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)

    print("The common elements are:", common_elements)


compare_lists([1, 2, 3, 4, 5, 6], [8, 9, 11, 4, 5, 2])

print("-" * 80)


def remove_duplicates(items):
    #new_item_list = list(set(items))
    new_item_list = numpy.unique(items).tolist()
    print("New list without duplicates:", new_item_list, type(new_item_list))
    return new_item_list


remove_duplicates(["apple", "pear", "ananas", "apple", "banana", "banana"])


def remove_duplicates_my_way(items):
    new_item_list = []
    for i in items:
        if i not in new_item_list:
            new_item_list.append(i)

    print("List without duplicates my way:", new_item_list)


remove_duplicates_my_way([1, 1, 2, 3, 5, 5, 4, 6, 9, 9, 8, 7])

print("-" * 80)


def describe_computer(computer):
    brand = computer.setdefault("Brand", "unknown Brand")
    c_type = computer.setdefault("Type", "unknown Type")
    price = computer.setdefault("Price", "unknown Price")

    print(f"You have a {c_type} from {brand} that costs {price}€.")

    computer.update({"OS": "Linux"})

    print(computer, type(computer))


my_notebook = {"Type": "Notebook", "Brand": "Dell", "Price": 2000}
describe_computer(my_notebook)
