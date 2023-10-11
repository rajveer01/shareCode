def calculate_average_grade(grades):
    """
    Calculate the average grade from a list of grades.

    :param grades: A list of numeric grades (int or float).
    :type grades: list
    :return: The average grade.
    :rtype: float
    """
    if not grades:
        raise ValueError("The list of grades is empty.")

    total_grades=sum(grades)
    average_grade=total_grades /len(grades)
    return average_grade


def main():
    try:
        grade_list = [85, 92, 78, 90, 88]
        average_grade = calculate_average_grade(grade_list)
        print(f"The average grade is: {average_grade:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
