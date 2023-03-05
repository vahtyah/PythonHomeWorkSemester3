import re


def parse_data_string(data_str):
    pattern = r"\s*let\s+array\s*\(\s*(?P<nums>[^)]" \
              r"+)\s*\)\s*->\s*(?P<name>\S+)\s*\]\]"
    matches = re.findall(pattern, data_str)
    result = []
    for match in matches:
        first_dot_index = match[1].find(".")
        name = match[1][1:first_dot_index - 1]
        nums = match[0].split('.')
        nums = [int(num) for num in nums]
        result.append((name, nums))
    return result


data_str = "<%[[ let array( 7067 . 475 . 427 . 5004)-> 'enqued'. ]].[[ let array(\n-3046 . -3012 . -1807 ) ->'esce_184'.]].[[let array( 2602 . 2988 .\n2823 . -1998)->'bive_798'.]].[[ let array( 7106 . 3224 . -6421 )->\n'maed_397'.]]. %>"
result = parse_data_string(data_str)
print(result)
