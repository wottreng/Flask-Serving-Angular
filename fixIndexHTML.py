import os


def find_all(html: str, sub: str):
    start = 0
    indexList = []
    while True:
        location = html.find(sub, start)
        # print(location)
        start = location + 1
        if location == -1: break
        indexList.append(location)
    return indexList


def fixIndexHTMLdoc():
    staticIndex = []
    offset = 0
    staticURLref = ["href=\"", "src=\""]
    with open(f"{os.getcwd()}/app/dist/app/index.html", "r") as main:
        indexHTML = main.read()
    # print(indexHTML)
    for staticRef in staticURLref:
        indexes = find_all(indexHTML, staticRef)  # find all static urls
        staticIndex += indexes
    staticIndex.pop(0)  # remove base reference
    # print(staticIndex)
    for index in staticIndex:
        if indexHTML[index + 5 + offset] == "?" or indexHTML[index + 6 + offset] == "?":
            pass
            # print(f"already done: {index}")
        else:
            # print(f"add ? here: {index}")
            # print(indexHTML.find(staticURLref[0],index))
            if indexHTML.find(staticURLref[0], index) != -1:
                # fix href tags
                indexHTML = indexHTML[0:index + 6 + offset] + "?" + indexHTML[index + 6 + offset:]
                offset += 1
            else:
                # fix src tags
                indexHTML = indexHTML[0:index + 5 + offset] + "?" + indexHTML[index + 5 + offset:]
                offset += 1

    with open(f"{os.getcwd()}/app/dist/app/index.html", "w") as main:
        indexHTML = main.write(indexHTML)
