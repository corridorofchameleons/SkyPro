from functions import get_student_by_pk, get_profession_by_title, check_suitability


def main():

    student_pk = input('Enter student number\n')

    # validates input data
    if student_pk.isdecimal():
        student_pk = int(student_pk)
    else:
        student_pk = -1

    student = get_student_by_pk(student_pk)

    # checks if student exists. If true, prints his/her info, otherwise exits
    if student:
        print(f"Student: {student.get('full_name')}")
        print(f"Knows: {', '.join(student.get('skills'))}")
        print()

        profession_title = input("Enter profession title\n")
        profession = get_profession_by_title(profession_title)
        print()

        # checks if profession exists. If true, prints score, otherwise exits
        if profession:
            score = check_suitability(student, profession)
            knows = 'knows ' + (', '.join(score.get('has')) if score.get('has') else 'nothing')
            not_knows = 'does not know ' + ', '.join(score.get('lacks')) if score.get('lacks') else 'knows everything'

            print(f"Suitability: {score.get('fit_percent')}")
            print(f"{student.get('full_name')} {knows}")
            print(f"{student.get('full_name')} {not_knows}")

        else:
            print('Sorry, the profession could not be found')

    else:
        print('Sorry, no such student')


if __name__ == '__main__':
    main()
