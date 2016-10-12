class things:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.value}, {self.weight})"

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def value_Weight(self):
        return self.value / self.weight


def build_menu(name, value, weight):
    menu = []
    for i in range(len(value)):
        menu.append(things(name[i], value[i], weight[i]))
    return menu


def greedy(item, maxCost, keyFunc):
    itemsCopy = sorted(item, key=keyFunc, reverse=True)
    result = []
    totalValue, total_cost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (total_cost + itemsCopy[i].get_weight()) <= maxCost:
            result.append(itemsCopy[i])
            total_cost += itemsCopy[i].get_weight()
            totalValue += itemsCopy[i].get_value()
    return (result, totalValue)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
