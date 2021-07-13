import requests
from bs4 import BeautifulSoup
from exceptions import LanguageException, MayReferException, LackReferenceException
from util import language_dict


def wiki_request(base_url, page_name):

    page = requests.get(base_url + page_name)

    return page


class WikiPage:
    def __init__(self, page_name, lang="English"):

        if not (lang in language_dict.keys()):
            raise LanguageException

        self.page_name = page_name
        self.base_url = "https://" + language_dict[
            lang] + ".wikipedia.org/wiki/"

        page = wiki_request(self.base_url, page_name)

        self.content = BeautifulSoup(page.content, "html.parser")
        self.URL = self.base_url + page_name

    def __str__(self) -> str:
        return self.title

    def set_lang(self, lang):
        """needs work"""
        self.__init__(self.page_name, lang=lang)

    @property
    def title(self):

        title = self.content.find(id="firstHeading").text
        return title

    @property
    def summary(self):

        container = self.content.find(class_="mw-parser-output")

        paragraphs = list(container.find_all("p"))
        content = []

        for p in paragraphs:
            if p.text == '\n': continue

            else:
                if "may refer to" in p.text: raise MayReferException(self)

                content.append(p.text)

            if len(content) == 2: break

        return "\n".join(content)

    def related(self, n_titles=10, type_of="titles"):

        links = list(self.content.find_all("a"))

        related_titles = []
        for link in links:
            if link.text == link.get("title"):
                if type_of == "titles": related_titles.append(link.text)
                if type_of == "pages":
                    related_titles.append(WikiPage(link.text))
            if len(related_titles) == n_titles:
                break

        return related_titles

    def references(self, n_ref=10):

        reflist = self.content.find(class_="mw-references-columns")

        try:
            source = list(reflist.find_all("span", class_="reference-text"))
            refs = []
            for i, s in enumerate(source[:n_ref]):
                refs.append(f"{i+1}. " + s.text)
        except:
            raise LackReferenceException

        return refs
