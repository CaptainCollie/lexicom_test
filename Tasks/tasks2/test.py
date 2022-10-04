def make_file_names(file_names: list[str]) -> list[str]:
    max_len = len(max(file_names, key=len))
    return [delete_dublicate_symbols(i).ljust(max_len, "_") for i in
            file_names]


def delete_dublicate_symbols(text: str):
    result = []
    seen = set()
    for symbol in text:
        if symbol not in seen:
            result.append(symbol)
            seen.add(symbol)

    return "".join(result)
