class Statistics:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
    def mean(self):
        return sum(self.data) / (self.length)

    def median(self):
        sorted_data = sorted(self.data)
        mid_index = self.length // 2
        if self.length % 2 == 0:
            midpoint = sum(sorted_data[(mid_index):mid_index+2])
            return midpoint / 2
        else:
            midpoint = sorted_data[mid_index]
            return midpoint

    def data_dict(self):
        data_dict = {}
        for i in self.data:
            key_str = str(i)
            if key_str in data_dict:
                data_dict[key_str] += 1
            else:
                data_dict[key_str] = 1
            
        return data_dict

    def mode(self):
        data_dict = self.data_dict()
        max_value = 0
        mode = 0
        for key, value in data_dict.items():
            if value > max_value:
                max_value = value
                mode = key
        return {'mode': mode, 'count': max_value}

    def range_stats(self):
        diff = max(self.data) - min(self.data)
        return diff

    def variance(self):
        square_diff = [((x - self.mean()) ** 2) for x in self.data]
        sum_square = sum(square_diff)
        variance = sum_square / (self.length - 1)

        return variance

    def std(self):
        return self.variance() ** 0.5

    def count(self):
        return self.length

    def sum_stats(self):
        sum_ = 0
        for i in self.data:
            sum_ += i
        
        return sum_

    def min_stats(self):
        min_ = self.data[0]
        for i in self.data:
            if min_ > i:
                min_ = i
            
        return min_

    def max_(self):
        max_ = 0
        for i in self.data:
            if max_ < i:
                max_ = i
        return max_

    def percentile(self, position):
        sorted_data = sorted(self.data)
        index = (position * (self.length + 1)) / 100
        percentile = 0
        if type(index) == 'int':
            percentile = sorted_data[index]
        else:
            sum_ = sorted_data[int(index) - 1] + sorted_data[int(index)]
            percentile = sum_ / 2

        return percentile

    def freq_dist(self):
        data_dict = self.data_dict()
        table = []
        for key, value in data_dict.items():
            table.append((key, value))

        return table





class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return sum(self.incomes)

    def total_expense(self):
        return sum(self.expenses)

    def account_balance(self):
        return self.total_income - self.total_expense

    def add_income(self, income):
        return self.incomes.append(income)

    def add_expense(self, expense):
        return self.expenses.append(expense)

    def account_info(self):
        return f'Account name: {self.firstname} {self.lastname}\n \
Account balance: {self.account_balance()}'