from PyQt5. QtWidgets import QApplication
from random import choice, shuffle
from time import sleep
app = QApplication([])

from m2 import *
from m3 import *

class Question:
    def __init__(self,question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
q1 = Question('Де знаходиться вавилон?', 'Ірак', 'Іран', 'Індія','Франція' )
q2 = Question('Коли почалася перша світова війна', 'В 1914 р.','В 1913 р.', 'В 1924 р.', 'В 1916')
q3 = Question('Що можна утримувати не торкаючись його руками','Дихання', 'Мовчання', 'Світло', '')
q4 = Question('З якого посуду нічого не можна їсти','З порожнього','З перевернутого', 'З гарячого', "З кам'яного")
q5 = Question('','','','','')
q6 = Question('','','','','')
q7 = Question('','','','','')
q8 = Question('','','','','')
q9 = Question('','','','','')
q10 = Question('','','','','')
def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)
def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()
