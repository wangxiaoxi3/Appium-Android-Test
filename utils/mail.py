# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午3:17
# @Author  : WangJuan
# @File    : mail.py

import smtplib, time, os
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils import L, tools
import zipfile
from utils.config import Config


class Mail:

    @staticmethod
    def report_zip(startdir):

        """
        :param startdir: 要压缩的文件夹路径
        :return: 压缩后的.zip文件
        """

        # 压缩后文件夹的名字
        file_news = startdir + '.zip'

        # 文件夹名
        z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)

        for dirpath, dirnames, filenames in os.walk(startdir):
            # 这一句很重要，不replace的话，就从根目录开始复制
            fpath = dirpath.replace(startdir, '')
            # 实现当前文件夹以及包含的所有文件的压缩
            fpath = fpath and fpath + os.sep or ''

            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                # print ('压缩成功')
        z.close()
        return file_news

    BASE_PATH_DIR = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    dir = BASE_PATH_DIR + '/report/html'
    report_html = report_zip(dir)

    def __init__(self):
        self.config = Config()

    def sendMail(self):
        msg = MIMEMultipart()
        boby = """
        <h3>Hi，all</h3>
        <p>附件为本次FM_自动化测试报告。</p>
        <p>请解压zip，并使用Firefox打开index.html查看本次自动化测试报告结果。</p>
        <p>注：如运行失败请看如下截图，如运行成功请忽略。</p> 
        <p>
        错误截图一：
        <br><img src="cid:image1"></br> 
        </p>
        <p>
        错误截图二：
        <br><img src="cid:image2"></br> 
        </p>
        <p>
        错误截图三：
        <br><img src="cid:image3"></br> 
        </p>
        """
        mail_body = MIMEText(boby, _subtype='html', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        file = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data/result.txt")))
        f = open(file, 'r')
        # 按行读出文件内容
        sourceInLines = f.readlines()
        f.close()
        # 定义一个空列表，用来存储结果
        new = []
        for line in sourceInLines:
            temp1 = line.strip('\n')  # 去掉每行最后的换行符'\n'
            temp2 = temp1.split(',')  # 以','为标志，将每行分割成列表
            new.append(temp2)  # 将上一步得到的列表添加到new中

        if new.count(['failed']) == 0:
            Subject = '[Passed]'
        else:
            Subject = '[Failed]'

        msg['Subject'] = Header(Subject+" "+"FM_Android_自动化测试报告"+"_"+tm, 'utf-8')
        msg['From'] = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        print(msg['To'])
        msg.attach(mail_body)

        # 添加report附件
        att = MIMEText(open(self.report_html, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        times = time.strftime("%m_%d_%H_%M", time.localtime(time.time()))
        filename_report = 'FM_Android_Report'+'_'+times+'.zip'
        # print(filename_report)
        att["Content-Disposition"] = 'attachment; filename= %s ' %filename_report
        msg.attach(att)

        # 获取最新的错误截图
        error_file_count = new.count(['failed'])+1
        dir_image = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "screenshot")))
        image_dir = tools.Find.find_new_file(dir_image, error_file_count)
        #
        for i in range(1,error_file_count):
            fp = open(image_dir[i-1], 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            msgImage.add_header('Content-ID', '<image%i>' % i)
            msg.attach(msgImage)

        # 登陆并发送邮件
        try:
            smtp = smtplib.SMTP()
            # 打开调试模式
            # smtp.set_debuglevel(1)
            smtp.connect(self.config.smtpserver)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
        except Exception as e:
            print(e)
            L.d("邮件发送失败！！")
        else:
            L.d("邮件发送成功")

        finally:
            smtp.quit()


