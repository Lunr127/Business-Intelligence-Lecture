import bs4
import re
import urllib.request
import urllib.error
import xlwt

findLink = re.compile(r'<a href="(.*)">')
findImgsrc = re.compile(r'<img.*src="(.*)" width="100"/>', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findNum = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = "商务智能豆瓣爬虫.xls"
    saveData(datalist, savepath)


def getData(baseurl):
    print("开始")
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)

        soup = bs4.BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            imgsrc = re.findall(findImgsrc, item)[0]
            data.append(imgsrc)

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                etitle = titles[1].replace("/", "")
                data.append(etitle)
            else:
                data.append(titles[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            num = re.findall(findNum, item)[0]
            data.append(num)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)
            bd = re.sub("/", " ", bd)
            data.append(bd.strip())

            datalist.append(data)

    return datalist


def askURL(url):
    print("正在爬取...")
    head = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist, savepath):
    print("正在保存..")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ("电影链接", "图片", "中文名", "英文名", "评分", "评价数", "概括", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])

    book.save("商务智能豆瓣爬虫.xls")
    print("完成")


if __name__ == "__main__":
    main()
