import random
import re
import string

# Gloabl rules
HAS_NUMBER_RULE = "has_number"
HAS_UPPER_RULE = "has_upper"
HAS_LOWER_RULE = "has_lower"
HAS_SPECIAL_RULE = "has_special"

NUMBER_OF_RULES = 4



def strongify_password(password: str, target_size=8):
    """
    This function will receive a password and check it fits is all of these criteria

    1. A minimum size of 8 characters
    2. At least one uppercase letter
    3. At least one lowercase letter
    4. At least one especial character
    5. At least one number

    :params password: The password to be analyzed 
    :params target_size: The minimum password length

    return: A strong password based on given password
    """

    rules_map = {}
    password_size = len(password)
    remaining_size = password_size
    password_to_verify = password

    # If the original password is less than target_size 
    # they will complete the password with random characters
    if (password_size < target_size):
        missing_len = target_size - password_size

        # They will call complete_password passing the original password 
        # and the missing_len, which is basically
        # the length left for this password to reach the target_size
        password = complete_password(password, missing_len)

        password_to_verify = password
        remaining_size = len(password_to_verify)


    while len(rules_map) < NUMBER_OF_RULES and remaining_size > 0:

        # Choose a randomic char
        pivot = random.randint(0, remaining_size-1)
        char_to_verify = password_to_verify[pivot]

        # Get the remain password 
        password_to_verify = password_to_verify[0:pivot] + \
            password_to_verify[pivot + 1:]
        remaining_size = len(password_to_verify)

        # Get missing rules to update the password
        missing_rules = NUMBER_OF_RULES - len(rules_map)

        if (remaining_size <= missing_rules):
            match_rule = check_rule(char_to_verify)
            if match_rule in rules_map:

                # get the first missing rule and update the character with this rule
                first_missing_rule = get_missing_rules(rules_map)
                char_with_rule = get_char_by_rule(first_missing_rule)
                password = password.replace(char_to_verify, char_with_rule, 1)
                rules_map[first_missing_rule] = True

            else:
                rules_map[match_rule] = True
        else:
            match_rule = check_rule(char_to_verify)
            rules_map[match_rule] = True

    # If all rules have been verified return the password
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
