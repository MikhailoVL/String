import re
import random
"""
1..--Даны две строки. Определите, можно ли из некоторых символов первой строки составить вторую строку.
2.--Строка состоит из слов, разделенных одним или несколькими пробелами. Поменяйте местами наибольшее по длине слово и наименьшее.
3..---Дана строка. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.
4.Дан текст. Найдите наибольшее количество идущих подряд цифр.
5..---Удалить в строке все цифры.
6..--Вывести слова, в которых заменить каждую большую букву одно-именной малой; удалить все символы, не являющиеся буквами или цифрами; вывести в алфавитном порядке все гласные буквы, входящие в каждое слово строки.
7.---Написать генерацию строк длины 10, причем первые 4 символа - цифры, следующие два символы - различные буквы, следующие 4 символа - нули или единицы, причем одна единица точно присутствует.
8..---Дана строка, состоящая из слов, разделенных пробелами. Определите количество слов в строке.
9..---Замените в строке все вхождения 'word' на 'letter'.
10..---Даны две строки. Удалить в первой строке первое вхождение второй строки."

"""
string_firs = "velvet vol transportvet vol"						#string for 1-func, 10-func
string_secon = "vol"											#string for 1-func, 10-func
str_func_oneO = "u The first stringgg nouu" 					#string for 2-func
string_abc = "ffrugork" 										#string for 3-func
string_al = "23fjsggh12" 										#string for 4-func
strings_vs_num = "The firs12t stringe rt123" 					#string for 5-func
str_cheng = "Sdf,We.T i?O word in my string and word in my"		#string for 6-func
string_word = "word bold cow slou"								#string for 8-func
string_v_word="word in my string and word in my"				#string for 9-func


def in_string(string_in_first, string_in_second):
	"""1
	#1-Даны две строки. 
	 Определите, можно ли из некоторых символов первой строки составить вторую строку.

	"""
	for key in string_in_second:
		if key not in string_in_first:
			return False
	return True

def bigOrLitle(String_long_short):
	dict_my = {}
	long_ =""
	short = ""
	new_str =""

	for word in String_long_short.split():
		dict_my[word] = len(word)

	print(dict_my)
	long_ = max(dict_my.keys())
	short = min(dict_my.keys())

	print(long_, short,"_______")
		
	for keys , value in dict_my.items():		
		if keys == long_:
			new_str += short + " "
		elif keys == short :
			new_str += long_ + " "
		else:
			new_str += keys + " "
	
	print(new_str)

def abc(string_vs_abc):
	"""#3 Дана строка. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'. """
	print("Строка: "+string_vs_abc)
	print((string_vs_abc+"zzz") if not string_vs_abc.find("abc")==0 else string_vs_abc.replace("abc","www"))

def replace_number(string_all):
	"""#5 replace all number"""
	string_not_didgit = ""
	for letter in string_all:
		if not letter.isdigit():
			string_not_didgit +=letter
	print("Строка с цифрами: " + string_all)
	print("Строка без цифр: " + string_not_didgit)

def int_count(string_vs_num):
	"""4.Дан текст.
	 Найдите наибольшее количество идущих подряд цифр.
	"""
	max_count = 0
	num_count = 0
	for num in string_vs_num.split():
		for key in num:
			if key.isdigit():
				num_count += 1
			if max_count < num_count:
				max_count = num_count
		num_count = 0
	print(max_count)

def chenge_string(str_chenge):
	"""#6
	Вывести слова, в которых заменить каждую большую букву одно-именной малой; 
	удалить все символы, не являющиеся буквами или цифрами;
	 вывести в алфавитном порядке все гласные буквы, входящие в каждое слово строки.

	"""
	vowels = "aeiuo"
	print("youre string:	 		" + str_chenge)
	print("lower all words: 		" + str_chenge.lower())
	print("replace all simbol: 		"+ "".join(re.findall(r'\w+', str_chenge.lower())))
	list_vs_aeiuo =[letter for letter in str_chenge.lower() if letter in vowels]
	list_vs_aeiuo.sort()
	print("vowels in alphabetical order:	",list_vs_aeiuo)

def generate_string():
	"""(7)генерацию строк длины 10
	причем первые 4 символа - цифры
	следующие два символы - различные буквы
	, следующие 4 символа - нули или единицы, причем одна единица точно присутствует.

	"""
	ppp = 'abcdefghijklmnopqrstuvwxyz'
	string_=""
	lent = 10 

	for item in range(lent):
			if item < 3:
				string_+= str(random.randint(0, lent))			
			elif item > 3 and item <6:
				string_+= ppp[random.randint(0, len(ppp))]
			else:
				string_+= str(random.randint(0, 1))	
	print(string_)
	
def how_many_words(string_words):
	"""#8function for count word in string"""
	print("В строке слов: ", len((string_words.split())))

def change_word_to_letter(string_vs_word):
	"""#-9 This function replace "word" to "letter"
	--string_vs_word - some string 

	"""
	print(string_vs_word)
	print(string_vs_word.replace("word","letter"))

def Delete_Second_string_in_first(string_first, string_second):
	"""#10 Удаление 1 вхождения

		ПРОГРАММА ПРОВЕРЯЕТ ПЕРВОЕ ВХОЖДЕНИЕ СТРОКИ. ЕСЛИ ЕСТЬ ТАКОВОЕ, ТО УДАЛЯЕТ ЕГО 
	--string_one, string_second  - Строки
	"""
	print("this program removes the first occurrence of a substring from a string.")
	print(f"my string: -{string_first} \nmy substring: -{string_second}")
	if string_first.find(string_second) == -1:
		print(f"В этой строке нет подстроки {string_first}")
	else:
		if string_first.find(string_second) == "0":
			print(string_first[(len(string_second)):])
		else:
			print(string_first[:(string_first.find(string_second))] + string_first[string_first.find(string_second)+len(string_second):])
	
def main():
	print("1________________")
	print(in_string(string_firs, string_secon))
	print("2________________")
	bigOrLitle(str_func_oneO)
	print("3________________")
	abc(string_abc)
	print("4________________")
	replace_number(string_al)
	print("5________________")
	int_count(strings_vs_num)
	print("6________________")
	chenge_string(str_cheng)
	print("7________________")
	generate_string()
	print("8________________")
	how_many_words(string_word)
	print("9________________")
	change_word_to_letter(string_v_word)
	print("10_______________")
	Delete_Second_string_in_first(string_firs, string_secon)


if __name__ == '__main__':
    main()