import allure
from selene.support.shared import browser
from selene import browser, have
from pages.practice_form import FormPage
from pages.users import User


# Тест без использования POM
def test_inputs_form_without_using_pom():
	with allure.step('Открываем страницу сайта'):
		browser.open('https://practice.expandtesting.com/inputs')

	with allure.step('Заполняем поля'):
		browser.element("#input-number").type(89500000000)
		browser.element("#input-text").type('Evgeniy Chechelev')
		browser.element("#input-password").type('0000')
		browser.driver.execute_script(
			"arguments[0].value = '1988-10-06';",
			browser.element('#input-date').locate()
		)
		browser.element("#btn-display-inputs").click()

	with allure.step('Проверяем заполненые поля'):
		browser.element('#output-number').should(have.text('89500000000'))
		browser.element('#output-text').should(have.text('Evgeniy Chechelev'))
		browser.element('#output-password').should(have.text('0000'))
		browser.element('#output-date').should(have.text('1988-10-06'))


# Тест c использованием POM
def test_inputs_form_with_pom():
	# Инициализируем объект
	f = FormPage()
	f.open()

	# Заполняем поля
	f.fill_number('89500000000')
	f.fill_text('Evgeniy Chechelev')
	f.fill_password('0000')
	f.fill_date('1988-10-06')

	# Жмем display inputs
	f.click_display_inputs()

	# Проверяем заполненные поля
	f.should_display_outputs()

	# Жмем clear inputs
	f.click_clear_inputs()

	# Проверяем что все поля очищены
	f.should_be_empty()


def test_inputs_form_with_high_level_method():
	evgeniy = User(
		phone='89500000000',
		name='Evgeniy Chechelev',
		password='0000',
		date='1988-06-10'
	)
	form = FormPage()
	form.open() \
		.register(evgeniy) \
		.should_have_registered(evgeniy) \
		.click_clear_inputs() \
		.should_be_empty()
