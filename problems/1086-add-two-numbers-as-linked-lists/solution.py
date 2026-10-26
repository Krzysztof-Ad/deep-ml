def add_two_numbers(l1, l2):
    result = []
    carry = 0
    for i in range(min(len(l1), len(l2))):
        part = l1[i] + l2[i] + carry
        if (part >= 10):
            carry = part // 10
            part %= 10
        else:
            carry = 0
        result.append(part)
    
    for i in range(min(len(l1), len(l2)), max(len(l1), len(l2))):
        part = (l1[i] if i < len(l1) else l2[i]) + carry
        carry = part // 10
        result.append(part % 10)
    
    if (carry != 0):
        result.append(carry)
    
    return result