from translate import Translator
translator = Translator(to_lang="de")
try:
    with open('Test1.txt', mode='r') as my_file1:
        text = my_file1.read()
        translation = translator.translate(text)
        print(translation)
    with open('Test2.txt', mode='w') as my_file2:
        my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path!')