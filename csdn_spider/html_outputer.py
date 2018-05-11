import pymysql

class HtmlOutPuter():

    # def __init__(self):
    #     self.datas = []

    # def collect_data(self,data):
    #     if data is None:
    #         return
    #     self.datas.append(data)

    def output_html(self):
        db = pymysql.connect("localhost", "root", "123456", "tptest", use_unicode=True, charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select * from spider"
        try:
            # 执行sql语句
            cursor.execute(sql)
            data = cursor.fetchall()
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚'
            db.rollback()
        finally:
            cursor.close()
            db.close()

        file = open('output.html','w', encoding='utf-8')
        file.write("<html>")
        file.write("<body>")
        file.write("<table  border='1' width='100%'>")
        for index, data in enumerate(data):
            file.write("<tr>")
            index = index+1
            file.write("<td>%s</td>" % index)
            file.write("<td><a href='%s'>%s<a></td>" % (data[4],data[4]))
            file.write("<td>%s</td>" % data[1])
            file.write("<td>%s</td>" % data[2])
            file.write("<td>%s</td>" % data[3])
            file.write("</tr>")
        file.write("</table>")
        file.write("</body>")
        file.write("</html>")
        file.close()
