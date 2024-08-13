sample_demos = {
    "under_20": ["Bike", "Pokemon", "Turtle"],
    "20_to_39": ["Bike", "Ball"],
    "40_to_50": ["Ball", "Door", "Person", "Turtle"],
}


def get_unique_item_count(demographics: dict) -> dict:
    formatted_output = {}

    for demo_name in demographics:
        formatted_output[demo_name] = len(
            find_unique_values(
                demographics[demo_name], get_all_other_values(demo_name, demographics)
            )
        )

    return formatted_output


def find_unique_values(a: list, b: list) -> list:
    return list(set(a) - set(b))


def get_all_other_values(current_key: str, whole_dict: dict) -> list:
    other_values = []

    for key, value in whole_dict.items():
        if key is not current_key:
            other_values.append(value)

    return sum(other_values, [])


if __name__ == "__main__":
    print(get_unique_item_count(sample_demos))
