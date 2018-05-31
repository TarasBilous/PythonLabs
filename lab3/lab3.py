import re


def search():
    images = 0

    file = open('access_log')
    for line in file:
        if re.search(
                '2004:((01:59)|(0[2-9]:[0-6}[0-6])|(1[0-2]:[0-6][0-6])|(13:5[0-5])|(13:[0-4][0-9]))'
                '.*\w*GET.*\w*\.((gif)|(jpeg)|(png)|(jpg)).*\w*200',
                str(line)):
            images += 1
            print(line)
    print(images)
    file.close()


if __name__ == "__main__":
    search()