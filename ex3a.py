MAX_SIZE = 5
stack = []
top = -1

def push(book_title):
    global top
    if top >= MAX_SIZE - 1:
        print("Stack overflow! Cannot push more books.")
    else:
        top += 1
        stack.append(book_title)
        print(f"Book {book_title} pushed onto the stack")

def pop():
    global top
    if top == -1:
        print("Stack underflow! Cannot pop any book.")
    else:
        remove_book = stack.pop()
        print(f"Book {remove_book} pooped from the stack")
        top -= 1

def peek():
    if top == -1:
        print("Stack is empty, No book to peek.")
    else:
        print(f"Top book on the stack:" ,stack[top])

def display():
    if top == -1:
        print("Stack is empty.")
    else:
        print("Book in stack(Top to bottom): ")
        for i in range(top, -1, -1):
            print(stack[i])

push("Money")
push("Harry Potter")
push("Zeus")
push("Hera")
display()
peek()
pop()
display()
peek()


    
