import json
# quantity, item, price, buyer, date

file_json = 'orders.json'


def write_order_to_json(quantity, item, price, buyer, date):
    """
    Считывание и запись файла json
    """
    result_to_json = {}
    result_to_json['item'] = item
    result_to_json['quantity'] = quantity
    result_to_json['price'] = price
    result_to_json['buyer'] = buyer
    result_to_json['date'] = date
    with open(file_json) as file:
        OBJ = json.load(file)

    with open(file_json, 'w') as file:

        OBJ['orders'].append(result_to_json)
        json.dump(OBJ, file, sort_keys=True, indent=4, ensure_ascii=False)


write_order_to_json('scanner', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('принтер', '20', '10000', 'Petrov P.P.', '11.01.2018')