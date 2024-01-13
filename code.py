import base64
import hashlib
import random
import string

def shuffle_characters(string_to_shuffle):
    characters_list = list(string_to_shuffle)
    random.shuffle(characters_list)
    return ''.join(characters_list)

def substitute_variables(code):
    variables = list(string.ascii_lowercase)
    for variable in variables:
        code = code.replace(variable, ''.join(random.sample(variables, len(variables))))
    return code

def hash_code(code):
    sha256 = hashlib.sha256()
    sha256.update(code.encode('utf-8'))
    return sha256.hexdigest()

def obfuscate_malicious_code(code):
    code = shuffle_characters(code)
    code = substitute_variables(code)
    code_base64 = base64.b64encode(code.encode('utf-8')).decode('utf-8')
    code_hash = hash_code(code)
    obfuscated_code = f"""
        {code}
        
        def obfuscated_code():
            code_base64 = '{code_base64}'
            code_hash = '{code_hash}'
            obfuscated_code = base64.b64decode(code_base64).decode('utf-8')
            if hashlib.sha256(obfuscated_code.encode('utf-8')).hexdigest() == code_hash:
                {obfuscated_code}
            else:
                print("Integrity compromised in the obfuscated code.")
    """

    return obfuscated_code

# Exemple d'usage
malicious_code = """
    # Code Suspect
"""

obfuscated_code = obfuscate_malicious_code(malicious_code)

print("Original malicious code:\n", malicious_code)
print("\nObfuscated malicious code:\n", obfuscated_code)