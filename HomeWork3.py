def happy_ticket(number):
    if len(str(number)) != 6:
        return False

    number_str = str(number)
    first_half = int(number_str[:3])
    second_half = int(number_str[3:])

    sum_first_half = sum(int(digit) for digit in number_str[:3])
    sum_second_half = sum(int(digit) for digit in number_str[3:])
    return sum_first_half == sum_second_half


ticket_number = 385916
if happy_ticket(ticket_number):
    print("Билет счастливый")
else:
    print("обычный билет")
