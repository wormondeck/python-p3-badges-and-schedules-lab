def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_list = [f"Hello, my name is {name}." for name in names]
    return badge_list

def assign_rooms(names):
    assign_list = [f"Hello, {name}! You'll be assigned to room {i}!" for i, name in enumerate(names, start=1)]
    return assign_list

def printer(names):
    batch = [print(assigned) for assigned in batch_badge_creator(names)]
    assign = [print(assigned) for assigned in assign_rooms(names)]
    return batch + assign