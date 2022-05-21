import sys

arguments = sys.argv
final_cost = 'infinity'


def generate_arr_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()
        lines = lines[:-1]  # removing END OF INPUT
        dict_arr = []
        for line in lines:
            line_split = line.split()
            dict_arr.append({
                'cities': [line_split[0], line_split[1]],
                'cost': int(line_split[2])
            })
        return dict_arr


def generate_heuristic_arr_from_file(f_name):
    with open(f_name) as f:
        lines = f.readlines()
        lines = lines[:-1]  # removing END OF INPUT
        dict_arr = []
        for line in lines:
            line_split = line.split()
            dict_arr.append({
                'city': line_split[0],
                'cost': int(line_split[1])
            })
        return dict_arr


def generate_child(info, fringe_item, heuristic=[]):
    parent_node = fringe_item['name']
    current_cost = fringe_item['cost']
    route = fringe_item['route']
    children = []
    parent_paths = list(
        filter(lambda d: parent_node in d['cities'], info))
    for match in parent_paths:
        item_index = 1 if match['cities'].index(parent_node) == 0 else 0
        child = {
            'name': match['cities'][item_index],
            'cost': current_cost+match['cost'],
            'route': route+[{'from': parent_node, 'to': match['cities'][item_index], 'cost':current_cost+match['cost']}]
        }
        if len(heuristic) > 0:
            child['hcost'] = get_heuristic_cost(child['name'], heuristic)
            child['total_cost'] = child['cost']+child['hcost']
        children.append(child)
    return children


def uninformed_search(uninf_arguments):
    f_name = uninf_arguments[0]
    start = uninf_arguments[1]
    end = uninf_arguments[2]
    info = generate_arr_from_file(f_name)
    fringe = [{'name': start, 'cost': 0, 'route': []}]
    closed = []
    expanded = 0
    generated = 0
    found = False
    while 1:
        if len(fringe) > 0:
            fringe_item = fringe[0]
            fringe.pop(0)
            # if(fringe_item['name'] in closed):
            if(next((item for item in closed if item["name"] == fringe_item['name']), None)):
                continue
            closed.append(fringe_item)
            if end == fringe_item['name']:
                found = True
                break
            expanded += 1
            children = generate_child(info, fringe_item)
            generated += len(children)
            children_names = []
            for child in children:
                children_names.append(child['name'])
            fringe = fringe+children
            fringe = sorted(fringe, key=lambda i: i['cost'])
        else:
            break

    print('nodes expanded: ', expanded)
    print('nodes generated: ', generated)
    if found:
        print('distance:', closed[-1]['cost'], 'km')
        print('route:')
        prev_cumulative = 0
        for path in closed[-1]['route']:
            print(f"{path['from']} to {path['to']}, {path['cost']-prev_cumulative}km")
            prev_cumulative = path['cost']
    else:
        print('distance:infinity')
        print('route:none')



def get_heuristic_cost(city, heuristic):
    match = next((item for item in heuristic if item["city"] == city), None)
    return match['cost'] if match else None


def informed_search(inf_arguments):
    f_name = inf_arguments[0]
    start = inf_arguments[1]
    end = inf_arguments[2]
    heuristic_name = inf_arguments[3]
    info = generate_arr_from_file(f_name)
    heuristic = generate_heuristic_arr_from_file(heuristic_name)
    fringe = [{
        'name': start,
        'cost': 0,
        'hcost': get_heuristic_cost(start, heuristic),
        'total_cost': get_heuristic_cost(start, heuristic),
        'route': []}]
    closed = []
    expanded = 0
    generated = 0
    found = False
    while 1:
        if len(fringe) > 0:
            fringe_item = fringe[0]
            fringe.pop(0)
            # if(fringe_item['name'] in closed):
            if(next((item for item in closed if item["name"] == fringe_item['name']), None)):
                continue
            closed.append(fringe_item)
            if end == fringe_item['name']:
                found = True
                break
            expanded += 1
            children = generate_child(info, fringe_item, heuristic)
            generated += len(children)
            children_names = []
            for child in children:
                children_names.append(child['name'])
            fringe = fringe+children
            fringe = sorted(fringe, key=lambda i: i['total_cost'])
        else:
            break

    print('nodes expanded: ', expanded)
    print('nodes generated: ', generated)
    if found:
        print('distance:', closed[-1]['cost'], 'km')
        print('route:')
        prev_cumulative = 0
        for path in closed[-1]['route']:
            print(f"{path['from']} to {path['to']}, {path['cost']-prev_cumulative}km")
            prev_cumulative = path['cost']
    else:
        print('distance:infinity')
        print('route:none')




if len(arguments) == 5:
    informed_search(arguments[1:])
else:
    uninformed_search(arguments[1:])


# python find_route.py input1.txt Bremen Kassel

# python find_route.py input1.txt Bremen Kassel h_kassel.txt
