import ujson


def load_raw_json_from_file(a: str) -> str:
    with open(a, mode='r', encoding="utf-8") as a:
        return a.read()


def load_json_data_from_file(a: str) -> any:
    with open(a, mode='r', encoding="utf-8") as a:
        b = a.read()
        # Чтобы избежать исключения из ujson
        if not b:
            return {
                "boards": []
            }
        c = ujson.loads(b)

    return c


def parse_json(a: str) -> any:
    # Чтобы избежать исключения из ujson
    if not a:
        return {
            "boards": []
        }
    return ujson.loads(a)


def format_json(a: str) -> str:
    return a.replace(' ', '').replace('\t', '').replace('\n', '')


def get_json_by_data(a: any) -> str:
    return ujson.dumps(a)


def save_json_data_to_file(a: str, b: dict) -> None:
    with open(a, mode='w', encoding="utf-8") as c:
        c.seek(0)
        c.write(ujson.dumps(b))


def can_combine_boards_jsons(a: str, b: str) -> bool:
    return len(b) == 0 and len(a) != 0


def combine_boards_jsons(a: str, b: str) -> list:
    c = parse_json(a)
    c.update(parse_json(b))
    return [ujson.dumps(c), c]