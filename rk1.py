from operator import itemgetter

class Processor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Computer:
    def __init__(self, id, model, price, proc_id):
        self.id = id
        self.model = model
        self.price = price
        self.proc_id = proc_id

class CompDevDept:
    def __init__(self, dept_id, comp_id):
        self.dept_id = dept_id
        self.comp_id = comp_id

class DevDept:
    def __init__(self, id, name):
        self.id = id
        self.name = name

procs = [
    Processor(1, 'Intel Core i7'),
    Processor(2, 'AMD Ryzen'),
    Processor(3, 'Intel Pentium'),
    Processor(4, 'AMD Athlon'),
    Processor(5, 'Intel Xeon')
]


comps = [
    Computer(1, 'Dell XPS', 1200, 1),
    Computer(2, 'HP Spectre', 1500, 2),
    Computer(3, 'Lenovo ThinkPad', 1000, 3),
    Computer(4, 'Apple MacBook', 2000, 4),
    Computer(5, 'Asus', 200, 5),
    Computer(6, 'Acer Aspire', 800, 2)
]

dev_depts = [
    DevDept(1, 'Architecture Dept'),
    DevDept(2, 'Advanced Systems'),
    DevDept(3, 'AI Research'),
    DevDept(4, 'Analytics Team')
]

comps_devs = [
    CompDevDept(1, 1),
    CompDevDept(1, 5),
    CompDevDept(2, 2),
    CompDevDept(2, 3),
    CompDevDept(3, 4),
    CompDevDept(4, 6)
]

def main():
    one_to_many = [(c.model, p.name)
                   for p in procs
                   for c in comps
                   if c.proc_id == p.id and p.name.endswith('on')]
    
    print("Компьютеры с процессором, заканчивающимся на 'оn':")
    for item in one_to_many:
        print(item)

    many_to_one = [(d.name, c.price)
                   for d in dev_depts
                   for cd in comps_devs
                   for c in comps
                   if c.id == cd.comp_id and d.id == cd.dept_id]
    
    dept_avg_price = {}
    for dept, price in many_to_one:
        if dept not in dept_avg_price:
            dept_avg_price[dept] = []
        dept_avg_price[dept].append(price)
    
    dept_avg_price = [(dept, sum(prices) / len(prices)) for dept, prices in dept_avg_price.items()]
    
    print("\nОтделы со средней ценой компьютеров:")
    for dept, avg_price in sorted(dept_avg_price, key=itemgetter(1), reverse=True):
        print(f"{dept}: {avg_price:.2f} USD")

    many_to_many_temp = [(d.name, cd.comp_id)
                         for d in dev_depts
                         for cd in comps_devs
                         if d.id == cd.dept_id and d.name.startswith('A')]

    many_to_many = [(c.model, dept_name)
                    for dept_name, comp_id in many_to_many_temp
                    for c in comps if c.id == comp_id]
    
    print("\nОтделы, начинающиеся на 'A', и компьютеры:")
    for model, dept_name in many_to_many:
        print(f"{dept_name}: {model}")

if __name__ == "__main__":
    main()