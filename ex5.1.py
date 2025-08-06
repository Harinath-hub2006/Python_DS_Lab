class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def append(self, coeff, exp):
        new_node = Node(coeff, exp)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def printPolynomial(self):
        temp =self.head
        result = []
        while temp:
            result.append(f"{temp.coeff}x^{temp.exp}")
            temp = temp.next
        return "+".join(result)

    def addPolynomial(self, p1, p2):
        a = p1
        b = p2
        new_node1 = Node(0, 0)
        c = new_node1
        while a is not None or b is not None:
            if a is None:
                c.next = b
                break
            elif b is None:
                c.next = a
                break
            elif a.exp == b.exp:
                c.next = Node(a.coeff + b.coeff, a.exp)
                a = a.next
                b = b.next
            elif a.exp > b.exp:
                c.next = Node(a.coeff, a.exp)
                a = a.next
            else:
                c.next = Node(b.coeff, b.exp)
                b = b.next
            c = c.next
        return new_node1.next

poly1 = Polynomial()
poly1.append(3, 3)
poly1.append(4, 2)
poly1.append(5, 1)
poly1.append(6, 0)
poly2 = Polynomial()
poly2.append(8, 2)
poly2.append(7, 1)
poly2.append(6, 0)
print("Polynomial 1: ", poly1.printPolynomial())
print("Polynomial 2: ", poly2.printPolynomial())
result = Polynomial()
result.head = result.addPolynomial(poly1.head, poly2.head)
print("Resultant Polynomial: ", result.printPolynomial())
            
