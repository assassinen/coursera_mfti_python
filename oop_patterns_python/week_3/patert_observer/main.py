from abc import ABC, abstractmethod


class Engine:
    pass

class ObservableEngine(Engine):  # Наблюдаемая система
    def __init__(self):
        self.__subscribers = set()  # При инициализации множество подписчиков звдвется пустым

    def subscribe(self, subscriber):
        self.__subscribers.add(
            subscriber)  # Для того чтобы подмисать пользователя, он добавляется во множество подписчиков

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)  # Удаление подписчика из списка

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)  # Отправка уведомления всем подписчикам


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):  # Абстрактный наблюдатель задает метод update
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        # self.__name = name
        self.achievements = set()

    def update(self, message):  # Конкретная реализация метода update
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        # self.__name = name
        self.achievements = []

    def update(self, message):  # Конкретная реализация метода update
        if message not in self.achievements:
            self.achievements.append(message)


def main():
    message = {"title": "Покоритель",
               "text": "Дается при выполнении всех заданий в игре"}
    message1 = {"title": "Покоритель1",
                "text": "Дается при выполнении всех заданий в игре1"}

    observable_engine = ObservableEngine()

    short_notification_printer = ShortNotificationPrinter()
    full_notification_printer = FullNotificationPrinter()

    observable_engine.subscribe(short_notification_printer)
    observable_engine.subscribe(full_notification_printer)
    observable_engine.notify(message)
    observable_engine.notify(message)
    observable_engine.notify(message1)
    print(short_notification_printer.achievements)
    print(full_notification_printer.achievements)

if __name__ == "__main__":
    main()
