# coding=utf-8

def deleteLeftParentheses(string):
    if string.__contains__('('):
        left_col = string.find('(')
        string = string[:left_col] + string[left_col + 1:]
        return string


def deleteRightParentheses(string):
    if string.__contains__(')'):
        right_col = string.find(')')
        string = string[:right_col] + string[right_col + 1:]
        return string


def deleteDot(string):
    if string.__contains__('.'):
        dot = string.find('.')
        string = string[:dot] + string[dot + 1:]
        return string


def deleteSingleQuoteMark(string):
    if string.__contains__('`'):
        pie = string.find('`')
        string = string[:pie] + string[pie + 1:]
        return string


def deleteLeftDoubleQuoteMark(string):
    if string.__contains__('“'):
        left_double = string.find('“')
        string = string[:left_double] + string[left_double + 3:]
        return string


def deleteRightDoubleQuoteMark(string):
    if string.__contains__('”'):
        right_double = string.find('”')
        string = string[:right_double] + string[right_double + 3:]
        return string


def deleteDunHao(string):
    if string.__contains__('、'):
        dun = string.find('、')
        string = string[:dun] + string[dun + 3:]
        return string


def deleteLeftBracket(string):
    if string.__contains__('['):
        left_bracket = string.find('[')
        string = string[:left_bracket] + string[left_bracket + 1:]
        return string


def deleteRightBracket(string):
    if string.__contains__(']'):
        right_bracket = string.find(']')
        string = string[:right_bracket] + string[right_bracket + 1:]
        return string


def deleteAdd(string):
    if string.__contains__('+'):
        right_bracket = string.find('+')
        string = string[:right_bracket] + string[right_bracket + 1:]
        return string


def deleteAnd(string):
    if string.__contains__('&'):
        right_bracket = string.find('&')
        string = string[:right_bracket] + string[right_bracket + 1:]
        return string


def replaceDunHao(string, replace):
    if string.__contains__('、'):
        dun = string.find('、')
        string = string[:dun] + replace + string[dun + 3:]
        return string


def replaceSharp(string, replace):
    if string.__contains__('#'):
        dun = string.find('#')
        string = string[:dun] + replace + string[dun + 1:]
        return string


def replaceSpace(string, replace):
    if string.__contains__(' '):
        dun = string.find(' ')
        string = string[:dun] + replace + string[dun + 1:]
        return string


def replaceColon(string, replace):
    if string.__contains__('：'):
        dun = string.find('：')
        string = string[:dun] + replace + string[dun + 3:]
        return string


def getTitle(raw_str):
    # 1.分离#与标题内容，并确定标题等级
    res = raw_str.split(' ')
    level = res[0].count('#')
    title = ""
    for i in range(1, res.__len__()):
        title = title + " " + res[i]
    # print(title)
    title = title.lstrip()
    title = title.strip('\n')
    title_for_show = title

    # 2.删除特殊字符
    while title.__contains__('.'):
        title = deleteDot(title)
        # print(title)
    while title.__contains__('('):
        title = deleteLeftParentheses(title)
        # print(title)
    while title.__contains__(')'):
        title = deleteRightParentheses(title)
        # print(title)
    while title.__contains__('`'):
        title = deleteSingleQuoteMark(title)
        # print(title)
    while title.__contains__('、'):
        title = deleteDunHao(title)
        # print(title)
    while title.__contains__('“'):
        title = deleteLeftDoubleQuoteMark(title)
        # print(title)
    while title.__contains__('”'):
        title = deleteRightDoubleQuoteMark(title)
        # print(title)
    while title.__contains__('['):
        title = deleteLeftBracket(title)
        # print(title)
    while title.__contains__(']'):
        title = deleteRightBracket(title)
        # print(title)
    while title.__contains__('+'):
        title = deleteAdd(title)
    while title.__contains__('&'):
        title = deleteAnd(title)
    while title.__contains__(' '):
        title = replaceSpace(title, '-')

    # 3.英文大写变小写
    res = title.lower()

    # print(res)
    return level, title_for_show, res


def getLink(base, string):
    while string.__contains__('、'):
        string = replaceDunHao(string, '-')
    while string.__contains__('#'):
        string = replaceSharp(string, '-')
    while string.__contains__(' '):
        string = replaceSpace(string, '-')
    while string.__contains__('：'):
        string = replaceColon(string, '-')
    return base + "#" + string


def getBase(year, month, day, filename):
    part1 = "http://zhaoxuhui.top/blog"
    res = part1 + "/" + year + "/" + month + "/" + day + "/" + filename + ".html"
    return res


def splitInfo(file_path):
    index = file_path.rfind('\\')
    path = file_path[:index]
    filename = file_path[index + 1:]
    temp = filename.split('-')
    year = temp[0]
    month = temp[1]
    day = temp[2]
    filename = temp[3].split('.')[0]
    return year, month, day, filename


def generateTOC(level, content):
    if level == 0:
        content = "- " + content
    elif level == 1:
        content = "\t- " + content
    elif level == 2:
        content = "\t\t- " + content
    elif level == 3:
        content = "\t\t\t- " + content
    elif level == 4:
        content = "\t\t\t\t- " + content
    elif level == 5:
        content = "\t\t\t\t\t- " + content
    elif level == 6:
        content = "\t\t\t\t\t\t- " + content
    return content


b_path = "F:\\Blog\\zhaoxuhui.github.io\\_posts\\"
files = []
f_path = raw_input("Input path of markdown file:\n")
files.append(f_path)
for fname in files:

    path = b_path + fname

    f = open(path.decode('utf8'), 'r')
    headers = []
    lines = []
    line = f.readline()
    lines.append(line)
    while line:
        # print line
        line = f.readline()
        lines.append(line)
        if line.__contains__("##"):
            headers.append(line.decode('utf-8').encode('utf-8'))
    f.close()
    if headers.__len__() == 0:
        print("No title.")
        continue

    year, month, day, name = splitInfo(path)
    base = getBase(year, month, day, name)
    print(base)

    formatted_title = []
    links = []
    bookmarks = []
    format_mark = []
    levels = []
    for item in headers:
        lev, show, res = getTitle(item)
        formatted_title.append(res)
        link = getLink(base, res)
        links.append(link)
        levels.append(lev)
        content = "[" + show + "](" + link + ")"
        bookmarks.append(content)

    min_level = (min(levels))
    for i in range(levels.__len__()):
        levels[i] = levels[i] - min_level

    for i in range(bookmarks.__len__()):
        format_mark.append(generateTOC(levels[i], bookmarks[i]))

    new_lines = []
    new_lines.append(lines[0])
    new_lines.append(lines[1])
    new_lines.append(lines[2])
    new_lines.append(lines[3])
    new_lines.append(lines[4])
    new_lines.append(lines[5])
    new_lines.append(lines[6])
    new_lines.append(lines[7])
    new_lines.append(lines[8])
    new_lines.append(lines[9])
    new_lines.append(lines[10])
    new_lines.append(lines[11])

    new_lines.append("#### Content\n")

    for item in format_mark:
        new_lines.append(item + "\n")

    new_lines.append("<hr>\n")

    for i in range(11, lines.__len__()):
        new_lines.append(lines[i])

    for item in new_lines:
        print(item)

    out_toc = ""
    for item in new_lines:
        out_toc = out_toc + item
    fout = open(path.decode('utf8'), 'w')
    fout.writelines(out_toc)
    fout.close()
