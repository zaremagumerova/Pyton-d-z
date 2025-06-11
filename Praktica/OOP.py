from user import User #так VSCode поймет, где класс для пользователя
from card import Card #так VSCode поймет, где класс для карточки
from email import Email # так VSCode поймет, где класс для почты

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()


card = Card("1234 5678 8765 4321", "03/28", "Alex F")
card.pay(1000) #из карточки вызвали метод и указали сумму
email = Email("zarema@mail.ru")
email("zarema@mail.ru")
alex.addCard(card) #добавили карточку
alex.getCard().pay(1000) #пользователь оплачивает карточкой из своего класса