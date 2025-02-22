from decimal import Decimal, ROUND_HALF_UP

def calculate_gross_salary(net_monthly_salary):

    if not isinstance(net_monthly_salary, (int, Decimal)):
        print("Ошибка: Зарплата должна быть числом.")
        return None

    if net_monthly_salary < 0:
        print("Ошибка: Зарплата не может быть отрицательной.")
        return None

    net_annual_salary = net_monthly_salary * 12

    gross_annual_salary = Decimal("0.00")

    # Расчет "грязного" дохода для случая, когда весь доход облагается по ставке 13%
    if net_annual_salary <= Decimal("2400000") * Decimal("0.87"):
        gross_annual_salary = net_annual_salary / Decimal("0.87")
    else:
        # Рассчитываем, какая часть дохода облагается по ставке 13%
        tax13 = Decimal("2400000") * Decimal("0.13")
        remaining_net = net_annual_salary - (Decimal("2400000") * Decimal("0.87"))

        # Рассчитываем, какая часть дохода облагается по ставке 15%
        if remaining_net <= (Decimal("5000000") - Decimal("2400000")) * Decimal("0.85"):
            gross_annual_salary = Decimal("2400000") + (remaining_net / Decimal("0.85"))
        else:
            tax15 = (Decimal("5000000") - Decimal("2400000")) * Decimal("0.15")
            remaining_net -= (Decimal("5000000") - Decimal("2400000")) * Decimal("0.85")

            # Рассчитываем, какая часть дохода облагается по ставке 18%
            if remaining_net <= (Decimal("20000000") - Decimal("5000000")) * Decimal("0.82"):
                gross_annual_salary = Decimal("5000000") + (remaining_net / Decimal("0.82"))
            else:
                tax18 = (Decimal("20000000") - Decimal("5000000")) * Decimal("0.18")
                remaining_net -= (Decimal("20000000") - Decimal("5000000")) * Decimal("0.82")
                gross_annual_salary = Decimal("20000000") + (remaining_net / Decimal("0.80")) #20%

    gross_monthly_salary = gross_annual_salary / Decimal("12")

    # Округляем по правилам ROUND_HALF_UP (обычное арифметическое округление)
    rounded_salary = gross_monthly_salary.quantize(Decimal("0"), rounding=ROUND_HALF_UP)

    return rounded_salary


# Проверка на корректный ввод значения
net_salary_str = input("Введите месячную зарплату после налогообложения: ")
try:
    net_salary = Decimal(net_salary_str)
except:
    print("Некорректный ввод. Введите число.")
    net_salary = None

if net_salary is not None:
    gross_salary = calculate_gross_salary(net_salary)

    if gross_salary is not None:
        print(f"Годовая зарплата после налогообложения: {net_salary*12}")
        print(f"Месячная зарплата до налогообложения: {gross_salary}")
        print(f"Годовая зарплата после налогообложения: {gross_salary*12}")
        print(f"Годовой налог: {gross_salary*12-net_salary*12}")