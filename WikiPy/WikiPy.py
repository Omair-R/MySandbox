import argparse
from wiki_page import WikiPage
from util import color


def main():

    parser = argparse.ArgumentParser(
        description=f"""
{color.format("purple", "bold")}                   +++++++++++ WikiPy +++++++++++ {color.PURPLE} 

This project was developed for the purpose of practicing webscraping. 
There are other wikipedia frameworks that has far more sophisticated functionality, if you're looking for 
a wikipedia API, then go for them instead. This was fun to program though :3. {color.ENDC}
    """,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "Title",
        type=str,
        help="Enter the title you with to find an article for.")

    parser.add_argument("--summary",
                        action="store_true",
                        help="this provides summary of an articale.")
    parser.add_argument("--related",
                        action="store_true",
                        help="Finds related articles to the same topic.")
    parser.add_argument("--reference",
                        action="store_true",
                        help="Find the reference links used in the article.")
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=10,
        help=
        "The number of related articles or reference links you which to retrieve, default is 10."
    )
    parser.add_argument("-l",
                        "--language",
                        default="English",
                        choices=["English", "Arabic", "French"],
                        help="set the language (experimental)")
                        
    args = parser.parse_args()

    page = WikiPage(args.Title, lang=args.language)
    print("==== " + color.BOLD + page.title + color.ENDC + " ====\n")

    if args.summary:
        print("==== " + color.format("yellow", "bold") + "Summary" +
              color.ENDC + " ====")
        print(color.YELLOW + "\n" + page.summary + color.ENDC)

    if args.related:
        print("==== " + color.format("green", "bold") + "Related articles" +
              color.ENDC + " ====")
        print(color.GREEN + "\n" +
              "\n".join(page.related(n_titles=args.number)) + "\n" +
              color.ENDC)

    if args.reference:
        print("==== " + color.format("blue", "bold") +
              "References used in the article" + color.ENDC + " ====")
        print(color.BLUE + "\n" +
              "\n".join(page.references(n_ref=args.number)) + "\n" +
              color.ENDC)


if __name__ == "__main__":
    main()