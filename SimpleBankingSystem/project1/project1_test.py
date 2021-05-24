
import string
from random import choice
# chars = string.digits
# random =  ''.join(choice(chars) for _ in range(4))
# print(random)

id_index = 0
inn = '400000'      # Issuer Identification Number (IIN)
can_length = 9      # Customer Identification Number
checksum = '5'      # any value is okay for now
logged_in = False   # logged in


accounts = []       # card_num, pin, balance, logged_in
# accounts.append(['4000004938320895', '1234'])
# accounts.append(['4000004938320896', '1234'])

# id_index = 0
# id_index = id_index + 1
# can_str = f"{id_index:09d}"
# print(can_str)

value = 4
a = [[1,2],[3,4],[5,6]]
x = [x for x in a if value in x][0]
print('The index is (%d,%d)'%(a.index(x),x.index(value)))

def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

tl = [[1,2,3],[4,5,6],[7,8,9]]

print(find(tl, 6)) # (1,2)
print(find(tl, 1)) # (0,0)
print(find(tl, 9)) # (2,2)
print(find(tl, 12)) # -1

def find_account(account_id):
    global accounts

    for index, row in enumerate(accounts):
        try:
            column = row.index(account_id)
        except ValueError:
            continue
        # return row, index, column
        return row

    return [-1]
#
# account_id = '4000000000000015'
# for index, row in enumerate(accounts):
#     try:
#         column = row.index(account_id)
#     except ValueError:
#         continue
#
#     print(index, row, account_id)

# tl = [[1,2,3],[4,5,6],[7,8,9]]
# print(find_account(tl, 6)) # (1,2)

# account
account = find_account('4000000000000015')

pin = 1234

if account[0] != -1 and account[1] == pin:
    logged_in = True


if account[0] is not -1:
    print('not -1')
else:
    print('-1')

if account[1] is pin:
    print('pin')
else:
    print('not pin')

found = find_account('4000000000000015')

if found[0] > -1:
    index = found[0]
    account = found[1]
    logged_in = account[3]

    print(account, logged_in)


def _generate_checksum(self, digits_in_str):
    _sum = 0
    alt = False
    for d in reversed(digits_in_str):
        d = int(d)
        assert 0 <= d <= 9
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        _sum += d
        alt = not alt
    return str(10 - (_sum % 10))


def tax(user_income):
    tax_dict = {15528: 15, 42708: 25, 132407: 28}
    tax_percent = 0
    if user_income >= 15528:
        tax_percent = tax_dict[15528]
        if user_income >= 42708:
            tax_percent = tax_dict[42708]
            if user_income >= 132407:
                tax_percent = tax_dict[132407]
    return tax_percent


