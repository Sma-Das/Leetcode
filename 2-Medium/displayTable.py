from collections import defaultdict, deque


def displayTable(orders: list[list[str]]) -> list[list[str]]:
    table = defaultdict(defaultdict)

    foods = set()
    for _, t_num, _ in orders:
        table[t_num] = defaultdict(int)
        table[t_num]["Table"] = t_num

    for _, t_num, food in orders:
        table[t_num][food] += 1
        foods.add(food)

    headers = ["Table", *foods]
    out = deque([])
    for entry in table.values():
        res = deque([])
        for header in headers:
            res.append(str(entry[header]))
        out.append(res)
    return [headers, *sorted(out, key=lambda x: int(x[0]))]


if __name__ == '__main__':
    orders = [
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["David", "3", "Ceviche"],
        ["Corina", "10", "Beef Burrito"],
        ["David", "3", "Fried Chicken"],
        ["Carla", "5", "Water"],
        ["Carla", "5", "Ceviche"],
        ["Rous", "3", "Ceviche"],
        ["Laura", "2", "Bean Burrito"],
        ["Jhon", "2", "Beef Burrito"],
        ["Melissa", "2", "Soda"],
        ["James", "12", "Fried Chicken"],
        ["Ratesh", "12", "Fried Chicken"],
        ["Amadeus", "12", "Fried Chicken"],
        ["Adam", "1", "Canadian Waffles"],
        ["Brianna", "1", "Canadian Waffles"]
    ]

    print(displayTable(orders))
