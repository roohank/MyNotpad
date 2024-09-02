file_name = 'Output.txt'

def write_to_file(file_name, text):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(text + '\n')

def replace_spaces_with_tabs(text):
    return text.replace('    ', '\t')

def replace_tabs_with_spaces(line):
    # تبدیل هر تب به ۴ فاصله
    return line.replace('\t', '    ')



# دریافت کد پایتون به عنوان ورودی
input_code = '''
def example_function():
    """test"""
    if True:
        print("""This is a test with multiple spaces    and should not be replaced""")
        x = 10    # اینجا 4 فاصله برای نمایش کامنت داریم
    else:
        print("Another example")    # باز هم 4 فاصله
'''

if __name__ == '__main__':
    lines = input_code.split('\n')
    processed_lines = [replace_spaces_with_tabs(line) for line in lines]
    output_code = '\n'.join(processed_lines)
    
#    print("کد پردازش شده:")
#    print(output_code)
    
    write_to_file(file_name, output_code)
