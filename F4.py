import flet as ft

class NumberCondition:
    def __init__(self, N):
        self.N = N

    def condition_number(self):
        condition1 = (self.N % 3 == 0) and (self.N % 9 != 0)
        condition2 = (self.N % 4 == 0) and (self.N % 5 == 0) and (self.N % 24 == 0)
        return condition1 and (not (self.N % 4 == 0) or condition2)

def main(page: ft.Page):
    page.title = "Проверка числа"

    def check_number(e):
        try:
            N = int(input_field.value)
            number_condition = NumberCondition(N)
            result = number_condition.condition_number()
            result_text.value = f"Число {N} {'удовлетворяет' if result else 'не удовлетворяет'} условиям."
        except ValueError:
            result_text.value = "Введите корректное число."
        page.update()

    input_field = ft.TextField(label="Введите число N")
    check_button = ft.ElevatedButton(text="Проверить", on_click=check_number)
    result_text = ft.Text()

    page.add(input_field, check_button, result_text)

ft.app(target=main)
