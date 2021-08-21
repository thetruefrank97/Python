class Course:
    def __init__(self, title, instructor, price, lectures):
        self.__title = title
        self.__instructor = instructor
        self.__price = price
        self.__lectures = lectures
        self.__users = []
        self.__ratings = 0
        self.__avg_rating = 0

    def _str_(self):
        return f"{self.__title} by {self.__instructor}"

    def new_user(self, user):
        self.__users.append(user)

    def received_a_rating(self, new_rating):
        self.__avg_rating = (self.__avg_rating * self.__ratings + new_rating)/(self.__ratings + 1)
        self.__ratings += 1

    def show_details(self):
        print("Course Title: ", self.__title)
        print("Instructor: ", self.__instructor)
        print("Price: ", self.__price)
        print("Number of Lectures: ", self.__lectures)
        print("Users: ", self.__users)
        print("Average rating: ", self.__avg_rating)


class VideoCourse(Course):
    def __init__(self, title, instructor,  price, lectures,  length_video):
        super().__init__(title, instructor, price, lectures)
        self.__length_video = length_video

    def show_details(self):
        super().show_details()
        print("Video length: ", self.__length_video)


class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.__pages = pages

    def show_details(self):
        super().show_details()
        print("Number of pages: ", self.pages)


def main():
    vc = VideoCourse("Learn genshin", "Geranimo", 50, 10, 20)
    vc.new_user("Kaisa")
    vc.new_user("Ashe")
    vc.new_user("Draven")
    vc.received_a_rating(3)
    vc.received_a_rating(4)
    vc.received_a_rating(5)
    vc.show_details()


main()
