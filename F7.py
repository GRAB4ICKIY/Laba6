import flet as ft

class Task:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def is_divisible_by_7(self):
        return self.number % 7 == 0

    def is_not_divisible_by_11(self):
        return self.number % 11 != 0

    def is_not_divisible_by_13(self):
        return self.number % 13 != 0

    def check_conditions(self):
        return (self.is_even() and
                self.is_divisible_by_7() and
                self.is_not_divisible_by_11() and
                self.is_not_divisible_by_13())

def main(page: ft.Page):
    number_input = ft.TextField(label="Введите число", autofocus=True)

    result_label = ft.Text()

    def on_check_click(e):
        try:
            number = int(number_input.value)

            task = Task(number)

            if task.check_conditions():
                result_label.value = f"Число {number} удовлетворяет всем условиям."
            else:
                result_label.value = f"Число {number} не удовлетворяет всем условиям."
        except ValueError:
            result_label.value = "Пожалуйста, введите корректное число."

        page.update()

    check_button = ft.ElevatedButton("Проверить число", on_click=on_check_click)

    page.add(number_input, check_button, result_label)

ft.app(target=main)
