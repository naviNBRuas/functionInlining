import re

# Read the source code
with open('source.c', 'r') as file:
    code = file.read()

# Define regular expressions to find function definitions and calls
func_def_pattern = re.compile(r'\b(\w+)\s+(\w+)\s*\(([^)]*)\)\s*{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)}', re.DOTALL)
func_call_pattern = re.compile(r'\b(\w+)\s*\(([^)]*)\);')

# Create a dictionary to store function definitions
functions = {}

# Extract function definitions
for match in func_def_pattern.finditer(code):
    return_type, func_name, params, body = match.groups()
    functions[func_name] = (params, body)

# Function to format and replace function calls with function bodies
def replace_func_calls(code):
    def replace_func_call(match):
        func_name, args = match.groups()
        if func_name in functions:
            params, body = functions[func_name]
            param_list = [param.strip() for param in params.split(',')]
            arg_list = [arg.strip() for arg in args.split(',')]
            for param, arg in zip(param_list, arg_list):
                body = re.sub(r'\b' + re.escape(param) + r'\b', arg, body)
            return '{' + body + '}'
        else:
            return match.group(0)

    return func_call_pattern.sub(replace_func_call, code)

# Inline functions in the source code
inlined_code = replace_func_calls(code)

# Write the inlined code to a new file
with open('inlined_source.c', 'w') as file:
    file.write(inlined_code)

print("Inlining complete. Check the 'inlined_source.c' file.")