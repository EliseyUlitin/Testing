import tkinter as tk
from tkinter import ttk, messagebox

class TestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тестирование")
        self.root.geometry("800x600")  # Увеличенное окно
        
        self.levels = {
            "Легкий": [
                {"question": "Столица Франции?", "choices": ["Париж", "Лондон", "Берлин", "Мадрид"], "answer": "Париж"},
                {"question": "Столица Германии?", "choices": ["Берлин", "Рим", "Вена", "Мадрид"], "answer": "Берлин"},
                {"question": "Столица Италии?", "choices": ["Рим", "Париж", "Афины", "Берлин"], "answer": "Рим"},
                {"question": "Столица Испании?", "choices": ["Мадрид", "Барселона", "Лиссабон", "Валенсия"], "answer": "Мадрид"},
                {"question": "Столица Великобритании?", "choices": ["Лондон", "Берлин", "Париж", "Рим"], "answer": "Лондон"},
            ],
            "Базовый": [
                {"question": "Столица Португалии?", "choices": ["Лиссабон", "Мадрид", "Париж", "Берлин"], "answer": "Лиссабон"},
                {"question": "Столица Нидерландов?", "choices": ["Амстердам", "Брюссель", "Берлин", "Рим"], "answer": "Амстердам"},
                {"question": "Столица Греции?", "choices": ["Афины", "Рим", "Париж", "Берлин"], "answer": "Афины"},
                {"question": "Столица Бельгии?", "choices": ["Брюссель", "Берлин", "Амстердам", "Париж"], "answer": "Брюссель"},
                {"question": "Столица Австрии?", "choices": ["Вена", "Берлин", "Рим", "Париж"], "answer": "Вена"},
                {"question": "Столица Венгрии?", "choices": ["Будапешт", "Прага", "Бухарест", "Варшава"], "answer": "Будапешт"},
                {"question": "Столица Чехии?", "choices": ["Прага", "Братислава", "Будапешт", "Варшава"], "answer": "Прага"},
                {"question": "Столица Польши?", "choices": ["Варшава", "Берлин", "Прага", "Вена"], "answer": "Варшава"},
                {"question": "Столица Швейцарии?", "choices": ["Берн", "Цюрих", "Женева", "Базель"], "answer": "Берн"},
                {"question": "Столица Швеции?", "choices": ["Стокгольм", "Осло", "Копенгаген", "Хельсинки"], "answer": "Стокгольм"},
            ],
            "Сложный": [
                {"question": "Столица Норвегии?", "choices": ["Осло", "Стокгольм", "Копенгаген", "Хельсинки"], "answer": "Осло"},
                {"question": "Столица Дании?", "choices": ["Копенгаген", "Осло", "Стокгольм", "Хельсинки"], "answer": "Копенгаген"},
                {"question": "Столица Финляндии?", "choices": ["Хельсинки", "Осло", "Стокгольм", "Копенгаген"], "answer": "Хельсинки"},
                {"question": "Столица Исландии?", "choices": ["Рейкьявик", "Осло", "Стокгольм", "Копенгаген"], "answer": "Рейкьявик"},
                {"question": "Столица Литвы?", "choices": ["Вильнюс", "Рига", "Таллин", "Минск"], "answer": "Вильнюс"},
                {"question": "Столица Латвии?", "choices": ["Рига", "Вильнюс", "Таллин", "Минск"], "answer": "Рига"},
                {"question": "Столица Эстонии?", "choices": ["Таллин", "Рига", "Вильнюс", "Минск"], "answer": "Таллин"},
                {"question": "Столица Украины?", "choices": ["Киев", "Минск", "Вильнюс", "Москва"], "answer": "Киев"},
                {"question": "Столица Беларуси?", "choices": ["Минск", "Москва", "Киев", "Вильнюс"], "answer": "Минск"},
                {"question": "Столица Болгарии?", "choices": ["София", "Бухарест", "Афины", "Белград"], "answer": "София"},
                {"question": "Столица Румынии?", "choices": ["Бухарест", "София", "Белград", "Афины"], "answer": "Бухарест"},
                {"question": "Столица Сербии?", "choices": ["Белград", "София", "Бухарест", "Афины"], "answer": "Белград"},
                {"question": "Столица Хорватии?", "choices": ["Загреб", "Любляна", "Сараево", "София"], "answer": "Загреб"},
                {"question": "Столица Словении?", "choices": ["Любляна", "Загреб", "Сараево", "Белград"], "answer": "Любляна"},
                {"question": "Столица Боснии и Герцеговины?", "choices": ["Сараево", "Загреб", "Любляна", "Белград"], "answer": "Сараево"},
            ]
        }

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 18))  # Увеличенный текст
        self.style.configure("TButton", font=("Arial", 18))
        self.style.configure("TRadiobutton", font=("Arial", 18))

        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.label = ttk.Label(self.root, text="Выберите уровень теста:")
        self.label.pack(pady=20)
        
        self.level_var = tk.StringVar()
        for level in self.levels.keys():
            rb = ttk.Radiobutton(self.root, text=level, variable=self.level_var, value=level)
            rb.pack(anchor="w")
        
        self.start_button = ttk.Button(self.root, text="Начать", command=self.start_test)
        self.start_button.pack(pady=20)
    
    def start_test(self):
        level = self.level_var.get()
        if not level:
            messagebox.showwarning("Предупреждение", "Пожалуйста, выберите уровень.")
            return
        
        self.questions = self.levels[level]
        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.question_label = ttk.Label(self.root, text=self.questions[self.current_question]["question"])
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        
        self.choices = []
        for choice in self.questions[self.current_question]["choices"]:
            rb = ttk.Radiobutton(self.root, text=choice, variable=self.var, value=choice)
            rb.pack(anchor="w")
            self.choices.append(rb)
        
        self.next_button = ttk.Button(self.root, text="Далее", command=self.next_question)
        self.next_button.pack(pady=20)
    
    def next_question(self):
        if self.var.get() == self.questions[self.current_question]["answer"]:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.root.after(500, self.show_question)  # Задержка 500 мс перед показом следующего вопроса
        else:
            self.show_result()
    
    def show_result(self):
        messagebox.showinfo("Результат", f"Ваш результат: {self.score} из {len(self.questions)}")
        self.main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = TestApp(root)
    root.mainloop()
