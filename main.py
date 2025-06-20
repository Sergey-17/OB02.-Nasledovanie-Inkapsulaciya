class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._access_level = "user"

    # Геттеры
    def get_user_id(self) -> int:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_access_level(self) -> str:
        return self._access_level

    # Сеттер для имени
    def set_name(self, new_name: str) -> None:
        self._name = new_name


class Admin(User):
    _user_list = []  # Общий список всех пользователей

    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self._access_level = "admin"  # Переопределяем уровень доступа

    # Метод для добавления пользователя
    def add_user(self, user: User) -> bool:
        if not isinstance(user, User):
            raise TypeError("Можно добавлять только объекты User")

        # проверка наличия пользователя в списке по заданному ID
        if any(u.get_user_id() == user.get_user_id() for u in Admin._user_list):
            print(f"Ошибка: Пользователь с ID {user.get_user_id()} уже существует")
            return False

        Admin._user_list.append(user)
        print(f"Пользователь {user.get_name()} (ID: {user.get_user_id()}) добавлен")
        return True

    # Метод для удаления пользователя
    def remove_user(self, user_id: int) -> bool:
        for user in Admin._user_list:
            if user.get_user_id() == user_id:
                Admin._user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален")
                return True
        print(f"Ошибка: Пользователь с ID {user_id} не найден")
        return False

    # Статический метод для просмотра пользователей
    @staticmethod
    def list_users() -> None:
        if not Admin._user_list:
            print("Список пользователей пуст")
            return

        print("\nСписок пользователей:")
        for user in Admin._user_list:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень: {user.get_access_level()}")

# Создаем администратора
admin = Admin(1, "Иван Петров")

# Создаем обычных пользователей
user1 = User(2, "Мария Сидорова")
user2 = User(3, "Алексей Иванов")

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(admin)  # Администратор может добавить себя

# Выводим список пользователей
Admin.list_users()

# Изменяем имя пользователя
user1.set_name("Мария Николаева")
print(f"\nНовое имя пользователя ID 2: {user1.get_name()}")

# Удаляем пользователя
admin.remove_user(2)

# Пытаемся удалить несуществующего пользователя
admin.remove_user(99)

# Итоговый список
Admin.list_users()