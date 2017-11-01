from mongoengine import *
from faker import Faker
import mlab
mlab.connect()

class Question(Document): #Collection
    question = StringField()
    answerA = StringField()
    answerB = StringField()
    answerC = StringField()
    answerD = StringField()
    correct_answer = StringField()
class Stress(Document): #Collection
    # = StringField()
    answerA = StringField()
    answerB = StringField()
    answerC = StringField()
    answerD = StringField()
    correct_answer = StringField()

class Vocab(Document):
    word = StringField()
    wordA = StringField()
    wordB = StringField()
    wordC = StringField()
    wordD = StringField()
    correct_word = StringField()

#task = Vocab(word = "reactor", wordA = "steel", wordB = "device", wordC = "rocket", wordD = "law", correct_word = "device")
#task = Question(question = "If x^1/2 = x/10 and x > 0, what is the value of x?", answerA = "10", answerB = "1000", answerC = "100", answerD = "1", correct_answer = "100")
#task.save()
