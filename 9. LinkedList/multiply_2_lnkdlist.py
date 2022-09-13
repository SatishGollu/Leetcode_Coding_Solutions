def multiplyTwoList(head1, head2):
    # Code here
    num1 = 0
    num2 = 0
    first_head = head1
    second_head = head2
    while first_head or second_head:
        if first_head != None:
            num1 = ((num1 * 10) + first_head.data)%1000000007
            first_head = first_head.next
        if second_head != None:
            num2 = ((num2 * 10) + second_head.data)%1000000007
            second_head = second_head.next
    return (num1 * num2)%1000000007