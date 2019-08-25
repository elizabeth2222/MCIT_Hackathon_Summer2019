import json


def parse_json(input_json):
    json_objects = []
    with open(input_json) as json_file:
        for json_string in json_file:
            json_objects.append(json.loads(json_string))

    return json_objects


if __name__ == '__main__':
    parse_json('../data/christmas_recipes.json')