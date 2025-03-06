import flet as ft

class NumberCondition:
    def __init__(self, n, m, k, l):
        self.n = n
        self.m = m
        self.k = k
        self.l = l

    def check_conditions(self):
        condition1 = (self.n + self.m * self.k > 0)
        condition2 = (self.n <= self.k) or (self.m < self.l)

        result = condition1 and condition2
        return result

def main(page: ft.Page):
    page.title = "Проверка условий"

    # Создаем текстовые поля для ввода значений
    n_input = ft.TextField(label="Введите значение n", keyboard_type=ft.KeyboardType.NUMBER)
    m_input = ft.TextField(label="Введите значение m", keyboard_type=ft.KeyboardType.NUMBER)
    k_input = ft.TextField(label="Введите значение k", keyboard_type=ft.KeyboardType.NUMBER)
    l_input = ft.TextField(label="Введите значение l", keyboard_type=ft.KeyboardType.NUMBER)

    result_text = ft.Text("")

    def check_numbers(e):
        try:
            n = int(n_input.value)
            m = int(m_input.value)
            k = int(k_input.value)
            l = int(l_input.value)

            number_condition = NumberCondition(n, m, k, l)

            result = number_condition.check_conditions()

            result_text.value = f"Результат проверки условий: {result}"
            result_text.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные целые числа."
            result_text.update()

    check_button = ft.ElevatedButton('Проверить', on_click=check_numbers)

    page.add(n_input, m_input, k_input, l_input, check_button, result_text)

ft.app(target=main)