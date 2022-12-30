import json

class Dependencies:

    def read_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def write_json(filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    def verify_food(filename, new_food_name):
        with open(filename) as f:
            lines = [line.rstrip() for line in f]
            for c in lines:
                if new_food_name not in c:
                    continue
                else:
                    return True
            return False