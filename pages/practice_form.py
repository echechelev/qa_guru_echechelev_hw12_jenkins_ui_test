import allure
from selene import browser, be, have
from pages.users import User


class FormPage:
	# 1 Константы
	URL = 'https://practice.expandtesting.com/inputs'

	# 2 Поля для заполнения

	# Поле "Номер"
	@property
	def field_number(self):
		return browser.element('#input-number')

	# Поле "Текст"
	@property
	def field_text(self):
		return browser.element('#input-text')

	# Поле "Пароль"
	@property
	def field_password(self):
		return browser.element('#input-password')

	# Поле "Дата"
	@property
	def field_date(self):
		return browser.element('#input-date')

	# 3 Поля для проверки

	# Поле "Номер"
	@property
	def output_number(self):
		return browser.element('#output-number')

	# Поле "Текст"
	@property
	def output_text(self):
		return browser.element('#output-text')

	# Поле "Пароль"
	@property
	def output_password(self):
		return browser.element('#output-password')

	# Поле "Дата"
	@property
	def output_date(self):
		return browser.element('#output-date')

	# 4 Кнопки

	# Кнопка "display inputs"
	@property
	def btn_display_inputs(self):
		return browser.element('#btn-display-inputs')

	# Кнопка "clear inputs"
	@property
	def btn_clear_inputs(self):
		return browser.element('#btn-clear-inputs')

	# 5 Методы

	@allure.step("Открываем сайт")
	def open(self):
		browser.open(self.URL)
		browser.should(have.url_containing(self.URL))
		self.field_number.should(be.visible)
		return self

	@allure.step("Заполняем поле Номер")
	def fill_number(self, number):
		self.field_number.type(number)
		return self

	@allure.step("Заполняем поле Текст")
	def fill_text(self, text):
		self.field_text.type(text)
		return self

	@allure.step("Заполняем поле Пароль")
	def fill_password(self, password):
		self.field_password.type(password)
		return self

	@allure.step("Заполняем поле Дата")
	def fill_date(self, date_str: str):
		browser.driver.execute_script(
			"arguments[0].value = arguments[1];",
			self.field_date.locate(),
			date_str
		)
		return self

	@allure.step("Жмем кнопку Display")
	def click_display_inputs(self):
		self.btn_display_inputs.click()
		return self

	@allure.step("Жмем кнопку Clear inputs")
	def click_clear_inputs(self):
		self.btn_clear_inputs.click()
		return self

	@allure.step("Проверяем заполненные поля")
	def should_display_outputs(self, number=None, text=None, password=None, date=None):
		from selene import have

		if number is not None:
			self.output_number.should(have.text(number))
		if text is not None:
			self.output_text.should(have.text(text))
		if password is not None:
			self.output_password.should(have.text(password))
		if date is not None:
			self.output_date.should(have.text(date))

		return self

	@allure.step("Проверяем что все поля очищены")
	def should_be_empty(self):

		self.field_number.should(have.value(''))
		self.field_text.should(have.value(''))
		self.field_password.should(have.value(''))
		self.field_date.should(have.value(''))

		return self

	@allure.step("Заполняем поля на форме")
	def register(self, user: 'User'):
		self.fill_number(user.phone)
		self.fill_text(user.name)
		self.fill_password(user.password)
		self.fill_date(user.date)
		self.click_display_inputs()
		return self

	@allure.step("Проверяем заполненные поля")
	def should_have_registered(self, user: 'User'):
		return self.should_display_outputs(
			number=user.phone,
			text=user.name,
			password=user.password,
			date=user.date
		)
