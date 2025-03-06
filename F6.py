import flet as ft

class MyClassTask:
    def __init__(self, deposit):
        self.deposit = deposit

    def calculate_payout(self):
        if self.deposit < 50000:
            rate = 0.16
        elif self.deposit <= 100000:
            rate = 0.18
        else:
            rate = 0  
        
        return self.deposit * (1 + rate)

def main(page: ft.Page):
    deposit_input = ft.TextField(label="Введите сумму вклада", autofocus=True)

    result_label = ft.Text()

    def on_calculate_click(e):
        try:
            deposit = float(deposit_input.value)

            my_task = MyClassTask(deposit)

            payout = my_task.calculate_payout()

            result_label.value = f"Сумма выплаты по депозиту: {payout:.2f} руб."
        except ValueError:
            result_label.value = "Пожалуйста, введите корректную сумму."

        page.update()

    calculate_button = ft.ElevatedButton("Рассчитать выплату", on_click=on_calculate_click)

    page.add(deposit_input, calculate_button, result_label)

ft.app(target=main)
