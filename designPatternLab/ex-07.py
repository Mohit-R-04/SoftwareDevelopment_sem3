import re

# Class for password validation
class PasswordValidator:
    def validate(self, password):
        """
        Validates the password based on the following criteria:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one digit
        - Contains at least one special character (@$!%*?&)
        """
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if re.match(pattern, password):
            return "Valid Password."
        else:
            return "Invalid Password."

# Class for variable name validation
class VariableValidator:
    def validate(self, variable):
        """
        Validates variable names:
        - Must start with a letter or underscore
        - Can contain letters, digits, and underscores
        """
        pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
        if re.match(pattern, variable):
            return "Valid"
        else:
            return "Invalid"

# Class for binary number validation
class BinaryNumberValidator:
    def validate(self, number):
        """
        Validates if the input string is a binary number.
        Only '0' and '1' are allowed.
        """
        pattern = r'^[01]+$'
        if re.match(pattern, number):
            return "Valid"
        else:
            return "Invalid"

# Class for sentence validation
class SentenceValidator:
    # Defined verbs, subjects, and objects for sentence structure
    verbs = ["cut", "cuts", "sing", "sings", "dance", "dances", "fell", "falls", "beat", "beats", "ate", "eats", "drink", "drinks"]
    subjects = ["He", "She", "People", "boys", "girls", "Ram", "Mohan", "A child", "Milk"]
    objects = ["tree", "Kavin", "Lollypop", "milk", "cat", "the tree", "the milk"]

    def validate(self, sentence):
        """
        Validates if the sentence follows the pattern:
        Subject + Verb + Object + '.'
        """
        subject_pattern = r'|'.join(re.escape(subject) for subject in SentenceValidator.subjects)
        verb_pattern = r'|'.join(re.escape(verb) for verb in SentenceValidator.verbs)
        object_pattern = r'|'.join(re.escape(obj) for obj in SentenceValidator.objects)

        # Sentence pattern: Subject Verb Object.
        pattern = rf'^({subject_pattern})\s+({verb_pattern})\s+({object_pattern})\.$'
        if re.match(pattern, sentence, re.IGNORECASE):
            return "Valid"
        else:
            return "Invalid"

# Testing the validators
if __name__ == "__main__":
    # 1. Password validation
    password = input("Enter the password: ")
    password_validator = PasswordValidator()
    print(password_validator.validate(password))

    # 2. Variable validation
    variable = input("Enter the variable name: ")
    variable_validator = VariableValidator()
    print(variable_validator.validate(variable))

    # 3. Binary number validation
    binary_number = input("Enter the binary number: ")
    binary_validator = BinaryNumberValidator()
    print(binary_validator.validate(binary_number))

    # 4. Sentence validation with predefined test cases
    test_sentences = [
        "Ram Cuts the tree.",    # Valid
        "Mohan beat Kavin.",     # Invalid
        "A child ate Lollypop.", # Valid
        "Drink milk cat.",       # Invalid
        "Milk drinks cat."       # Valid (Syntactically Valid)
    ]

    sentence_validator = SentenceValidator()
    for sentence in test_sentences:
        print(f'{sentence}: {sentence_validator.validate(sentence)}')
