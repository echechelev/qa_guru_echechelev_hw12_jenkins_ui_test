from dataclasses import dataclass


# Добавление класса
@dataclass
class User:
	phone: str
	name: str
	password: str
	date: str
