# Функции – это многократно используемые фрагменты программы. Они позволяют дать
# имя определённому блоку команд с тем, чтобы в последствии запускать этот блок по
# указанному имени в любом месте программы и сколь угодно много раз.
# Это называетсявызовом функции

# Функции определяются при помощи зарезервированного слова def. После этого слова
# указывается имя функции, за которым следует пара скобок, в которых можно указать
# имена некоторых переменных, и заключительное двоеточие в конце строки.
# Далее следует блок команд, составляющих функцию

def sayHello():
    print('Привет, Мир!') # блок, принадлежащий функции
# Конец функции

sayHello() # вызов функции
sayHello() # ещё один вызов функции