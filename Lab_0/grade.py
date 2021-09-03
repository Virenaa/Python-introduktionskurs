def grades(grade):
    switcher={
                0:'F',
                1:'F',
                2:'D',
                3:'C',
                4:'B',
                [90-100]:'A',
             }
    return switcher.get(grade,"Invalid day of week")


def main():
    grades(91)


main()