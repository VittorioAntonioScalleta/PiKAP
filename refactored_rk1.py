
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


def get_computers_with_processors_ending_with(procs, comps, suffix):
    return [(c.model, p.name)
            for p in procs
            for c in comps
            if c.proc_id == p.id and p.name.endswith(suffix)]


def get_departments_with_average_prices(dev_depts, comps_devs, comps):
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

    return [(dept, sum(prices) / len(prices)) for dept, prices in dept_avg_price.items()]


def get_departments_starting_with_and_computers(dev_depts, comps_devs, comps, prefix):
    many_to_many_temp = [(d.name, cd.comp_id)
                         for d in dev_depts
                         for cd in comps_devs
                         if d.id == cd.dept_id and d.name.startswith(prefix)]

    return [(c.model, dept_name)
            for dept_name, comp_id in many_to_many_temp
            for c in comps if c.id == comp_id]
