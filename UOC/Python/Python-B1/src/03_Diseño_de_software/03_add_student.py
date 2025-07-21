# add_student.py

import os

def add_student_by_value(list_students: list, new_student: str) -> list:
    """ Devuelve una nueva lista con el estudiante añadido (new_student) """

    # Copiamos la lista original:
    list_students_copy = list_students.copy()

    # Agregamos el nuevo estudiante:
    list_students_copy.append(new_student)

    return list_students_copy


def add_student_by_reference(list_students: list, new_student: str) -> list:
    """ Añade el estudiante a la lista original (por referencia) y la retorna."""

    # Agregamos el nuevo estudiante directamente a la lista:
    list_students.append(new_student)



def main(list_students: list, new_student_by_value, new_student_by_reference) -> None:
    """ Ejecuta ejemplos de adición de estudiantes por valor y por referencia """

    # Lista original:
    print("Original student list:", list_students)

    # Paso por valor:
    list_x_val = add_student_by_value(list_students, new_student_by_value)
    print("Studen list by value:", list_x_val)

    # Paso por referencia:
    add_student_by_reference(list_students, new_student_by_reference)
    print("Student list by reference:", list_students)



if __name__ == "__main__":
    os.system("cls")

    list_students = ["Alice", "Bob", "Juan"]
    new_student_by_value = "Maria"
    new_student_by_reference = "Sofia"

    main(list_students, new_student_by_value, new_student_by_reference)