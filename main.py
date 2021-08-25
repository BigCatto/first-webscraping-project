from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    data = html_file.read()

    soup = BeautifulSoup(data, 'lxml')
    course_cards = soup.find_all('div', class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f"This website offers {course_name} for the price of {course_price}")
        print()
