import flet as ft

class NumberCondition:
    def __init__(self, n, m, k, l):
        self.n = n
        self.m = m
        self.k = k
        self.l = l

    def check_conditions(self):
        condition1 = (self.n > 1)
        condition2 = (self.m <= self.l + self.k == 0)
        if self.n > 2:
            self.m ** 2 > self.l ** 2

        result = condition1 and condition2
        return result

def main(page: ft.Page):
    n_input = ft.TextField(label="Введите значение n", autofocus=True)
    m_input = ft.TextField(label="Введите значение m")
    k_input = ft.TextField(label="Введите значение k")
    l_input = ft.TextField(label="Введите значение l")

    result_label = ft.Text()

    def on_check_click(e):
        try:
            n = int(n_input.value)
            m = int(m_input.value)
            k = int(k_input.value)
            l = int(l_input.value)

            number_condition = NumberCondition(n, m, k, l)

            result = number_condition.check_conditions()
            result_label.value = f"Результат проверки условий: {result}"
        except ValueError:
            result_label.value = "Пожалуйста, введите корректные числа."

        page.update()

    check_button = ft.ElevatedButton("Проверить условия", on_click=on_check_click)

    page.add(n_input, m_input, k_input, l_input, check_button, result_label)

ft.app(target=main)
