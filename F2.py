import flet as ft

class NumberChecker:
    def __init__(self):
        self.N = 0

    def multiples_four_and_seven(self):
        return (self.N % 4 == 0) or (self.N % 7 == 0)

    def multiples_five_no_end_zero(self):
        return (self.N % 5 == 0) and (self.N % 10 != 0)

def main(page: ft.Page):
    page.title = "Практическая работа 6"
    
    n_input = ft.TextField(label="Введите число N", keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("")
    
    checker = NumberChecker()
    
    def check_numbers(e):
        try:
            checker.N = int(n_input.value)
            
            multiples_four_or_seven = checker.multiples_four_and_seven()
            multiples_five_no_end_zero = checker.multiples_five_no_end_zero()
            
            result_text.value = (
                f"N кратно четырем или семи: {multiples_four_or_seven}\n"
                f"N кратно 5 и не оканчивается на 0: {multiples_five_no_end_zero}"
            )
            result_text.update()  # Обновляем текстовое поле с результатами
        except ValueError:
            result_text.value = "Пожалуйста, введите корректное целое число."
            result_text.update()  # Обновляем текстовое поле с ошибкой

    check_button = ft.ElevatedButton('Проверить', on_click=check_numbers)
    
    page.add(n_input, check_button, result_text)

ft.app(target=main)