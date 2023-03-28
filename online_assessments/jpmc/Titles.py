class SolutionTitles:
    """
        string.title() method is a very simple and straightforward method of generating titles for strings.
        As the titles for string have a default structure where the first letter is always in upper case,
        this method helps us capitalize the first letter of every word and change the others to lowercase,
        thus giving the desired output. This method is also useful for formatting strings in HTML and
        formatting strings in JavaScript and other programming languages.
        """

    @staticmethod
    def generate_titles(text: str) -> str:
        return text.title()

    @staticmethod
    def cap_sentence(text: str) -> str:
        words = [word[0].upper() + word[1:].lower() for word in text.split()]
        return ' '.join(words)

if __name__ == '__main__':
    text = "view the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN.com."
    print(SolutionTitles.generate_titles(text))
    print(SolutionTitles.cap_sentence(text))
