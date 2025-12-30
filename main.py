import sys # Потрібно, щоб "сказати" Docker-у про помилку

def arithmetic_progression_element(n):
    if n < 0:
        raise ValueError("n не може бути від'ємним444444")

    a = 5
    d = 2
    return a + (n - 1) * d

# --- ЦЕЙ РЯДОК ВАЖЛИВИЙ ДЛЯ ТЕСТІВ ---
if __name__ == "__main__":
    try:
        n = int(input("Введіть n: "))
        result = arithmetic_progression_element(n)
        print(f"{n}-й елемент арифметичної прогресії: {result}")
    except ValueError as e:
        print("Помилка:", e)
        sys.exit(1) # Це щоб CI/CD зрозумів, що сталася помилка
