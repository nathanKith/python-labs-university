from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
import docx


def main():
    doc = docx.Document()

    rectangle = Rectangle("серо-буро-малинового", 2, 2)
    circle = Circle("бардового", 2)
    square = Square("бирюзового", 2)

    content = [
        'ИУ5-51Б Толпаров Натан',
        str(rectangle),
        str(circle),
        str(square),
    ]

    for item in content:
        doc.add_paragraph(item)

    doc.save('Report.docx')

    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()
