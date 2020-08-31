import random
import re
import string

HAS_NUMBER_RULE = "has_number"
HAS_UPPER_RULE = "has_upper"
HAS_LOWER_RULE = "has_lower"
HAS_SPECIAL_RULE = "has_special"

NUMBER_OF_RULES = 4


def strongify_password(password: str, target_size=8):
    rules_map = {}
    password_size = len(password)
    remaining_size = password_size
    password_to_verify = password

    # Complete smallers passwords
    if (password_size < target_size):
        missing_len = target_size - password_size
        password = complete_password(password, missing_len)
        password_to_verify = password
        remaining_size = len(password_to_verify)

    while len(rules_map) < NUMBER_OF_RULES and remaining_size > 0:
        pivot = random.randint(0, remaining_size-1)
        char_to_verify = password_to_verify[pivot]
        password_to_verify = password_to_verify[0:pivot] + \
            password_to_verify[pivot + 1:]
        remaining_size = len(password_to_verify)
        missing_rules = NUMBER_OF_RULES - len(rules_map)

        if (remaining_size <= missing_rules):
            match_rule = check_rule(char_to_verify)
            if match_rule in rules_map:
                first_missing_rule = get_missing_rules(rules_map)
                char_with_rule = get_char_by_rule(first_missing_rule)
                password = password.replace(char_to_verify, char_with_rule, 1)
                rules_map[first_missing_rule] = True
            else:
                rules_map[match_rule] = True
        else:
            match_rule = check_rule(char_to_verify)
            rules_map[match_rule] = True

    if len(rules_map) >= NUMBER_OF_RULES:
        return password
    else:
        return "Error"


def get_char_by_rule(rule: str):
    if rule == HAS_NUMBER_RULE:
        return generate_number()
    elif rule == HAS_UPPER_RULE:
        return generate_upper()
    elif rule == HAS_LOWER_RULE:
        return generate_lower()
    elif rule == HAS_SPECIAL_RULE:
        return generate_special()


def get_missing_rules(rule_map: dict):
    if HAS_NUMBER_RULE not in rule_map:
        return HAS_NUMBER_RULE
    elif HAS_UPPER_RULE not in rule_map:
        return HAS_UPPER_RULE
    elif HAS_LOWER_RULE not in rule_map:
        return HAS_LOWER_RULE
    elif HAS_SPECIAL_RULE not in rule_map:
        return HAS_SPECIAL_RULE


def check_rule(char_to_verify: str):
    if check_number(char_to_verify):
        return HAS_NUMBER_RULE

    elif check_upper(char_to_verify):
        return HAS_UPPER_RULE

    elif check_lower(char_to_verify):
        return HAS_LOWER_RULE

    elif check_special(char_to_verify):
        return HAS_SPECIAL_RULE


def complete_password(password: str, missing_len: int):
    letters = string.ascii_letters + string.digits + '[@_!#$%^&*()<>?/\|}{~:]'

    random_password = "".join(random.choice(letters)
                              for i in range(missing_len))

    return password+random_password


def check_number(character: str):
    return character.isdigit()


def check_upper(character: str):
    return character.isupper()


def check_lower(character: str):
    return character.islower()


def check_special(character: str):
    return bool(re.match('[@_!#$%^&*()<>?/\|}{~:]', character))


def generate_number():
    return str(random.randint(0, 9))


def generate_upper():
    return random.choice(string.ascii_uppercase)


def generate_lower():
    return random.choice(string.ascii_lowercase)


def generate_special():
    return random.choice('[@_!#$%^&*()<>?/\|}{~:]')
