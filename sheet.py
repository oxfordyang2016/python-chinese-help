# -*- coding: utf-8 -*-
# 此处的目的是在与直接在交互屏幕上显示对我们友好的帮助信息
#2016年3月6日10:23:36
#作者：杨明
#版本：0.0（nt）
#邮箱：756260386@qq.com    yang756260386@gmail.com

#项目地址：
#使用方法：nt中 将此模块文件放在python的目录下。然后在python解释器环境下使用import cheat，假如要获取for 的帮助信息，键入sheet.show('for')

#保护版权，从你我做起
#屏幕截图参见我的github地址




import random
import color
yangming=5
test='''

i love python
'''
type(test)
helpdict={'yangming':yangming}
color.cp('''

                                                 人生苦短，必须性感
                                                 如果一件事情你觉得难的完不成，你可以把它分为若干步,并不断寻找合适的方法。
                                                 最后你发现你会是个超人。不要给自己找麻烦，但遇到麻烦绝不怕，更不要退缩。
                                                 电工查找电路不通点的最快方法是：分段诊断排除，快速定位。你有什么启示吗？
                                                 求知若饥，虚心若愚。 当你对一个事情掌控不足的时候，你需要做的就是“梳理”，
                                                 并制定相应的规章制度，并使资源各司其职。

''')
def ym(k):#这里2016年4月9日17:35:50是我想进一步升级文档系统,我的初步想法是在任何位置插入变量内容，然后让我输入ym(k)的时候就打印出我想要的内容
    show(k)

    print type(k)
    color.cp(k)
    #这里的难点在于我函数里面的参数是字符串，另外一个就是我打印的时候，传入的参数是变量
    
def help():
    k=raw_input('please enter:')
    show(k)
def exp(k):

    if k in helpdict:
        print helpdict(k)
def show(k):
	if k=='all':
	    h= '''
                      3月*

                      author 打印开发者信息
                      class 展示类的相关信息
                      concept     展示python中一些常见概念
                      datastruc   展示常用的数据结构的简明格式
                      for   展示循环相关的信息
                      print 展示打印相关格式
                      sys   这里展示python的sys模块
                      try   这里展示所有try系列的用法
                      os    展示python的操作系统os 模块
                      import  说明import函数的作用
                      write 这里将展示如何写入文件
                      read  这里将展示如何读文件
                      urllib 解释urllib模块
                      pachong 展示妖娆的爬虫系统
                      lxml   解释xpath模块,这是一个网页处理模块
                      ifname   if __name__ == '__main__':      展示这句话的常见用法
                      list   展示常见的列表知识与操作
                      xpath.exp 显示xpath成功的实验
                      urljoin  展示url拼接的技术
                      string  展示字符串常见的用法
                      type   展示获取对象信息的方法



                      3月22日
                      color  展示颜色的输出
                      random 展示如何惨生随机数
                      3月23日
                      ipython 这里即将展示ipython相关的东西
                      scicompute  python数据分析入门
                      range  展示range的内容
                      dict   展示字典里面的内容
                      myidea 我目前的idea
                      import  import再次的使用
                      tupe   展示元组
                      3月24日
                      obj    展示面向对象变成的基本概念
                      file   处理文件的常见需求
                      3月28日
                      install vmtools
                      3月29日
                      lambda 表达式
                      json   对json数据的解释

                      4月1日
                      ipython 的一些细节
                      grep 函数的熟悉
                      4月2日
                      去上海自然博物馆玩耍了一天，然后从外滩朝工商银行走，一直走到尽头，
                      给漂亮的姑娘拍照拍了照片，然后去福州路的上海书城买了linux，晚上写代码
                      4月5日
                      python 展示python配置环境的时候的细节
                      input  展示获取用户输入的办法
                      jiaoben 展示python的脚本如何像一个普通程序运行

                      4月6日
                      import 了解import的所有细节
                      fuzhi  了解赋值的一些特定操作
                      if      展示if的一些常见用法
                      in      成员资格运算符
                      assert     展示断言的常见用法
                      break   表示跳出循环的详细信息
                      4月7日
                      continue 展示这个代码中常见的困惑
                      decode   来解决python中常见的编码问题
                      xshell   展示xshell的一些常见快捷键
                      n        解释python中常见的名词
                      vim      解释vim编辑器的常见用法
                      cmd      展示常见的windows cmd 中的用法
                      windows  展示windows常见的快捷键
                      4月8日
                      encode   解决python中棘手的编码问题
                      help     常见帮助信息的调用方法
                      moudle   展现一个模块常见的知识
                      4月9日
                      comment  注释的使用办法
                      huanhang 换行的使用办法     
                      4月10日
                      codestyle python编码风格的介绍
                      cron      unix的计划任务学习
                      git       linux 下git工具的使用
                 

                     




'''



            color.cp(h)
        if k=='git':
            h='''



                        1 Linux下Git和GitHub环境的搭建
                        
                        第一步： 安装Git，使用命令 “sudo apt-get install git”
                        
                        第二步： 创建GitHub帐号
                        
                        第三步： 生成ssh key，使用命令 “ssh-keygen -t rsa -C "your_email@youremail.com"”，your_email是你的email
                        
                        第四步： 回到github，进入Account Settings，左边选择SSH Keys，Add SSH Key,title随便填，粘贴key。
                                (这里的选项也许会发生变化)
                        
                        第五步： 测试ssh key是否成功，使用命令“ssh -T git@github.com”，
                        如果出现You’ve successfully authenticated, but GitHub does not provide shell access 。这就表示已成功连上github。
                        
                        第六步： 配置Git的配置文件，username和email
                        
                        git config --global user.name "your name" //配置用户名
                        
                        git config --global user.email "your email" //配置email

          2 利用Git从本地上传到GitHub
          
          第一步： 进入要所要上传文件的目录输入命令 “git init”
          
          第二步： 创建一个本地仓库origin，使用命令 “git remote add origin git@github.com:yourName/yourRepo.git”
          youname是你的GitHub的用户名，yourRepo是你要上传到GitHub的仓库
          
          第三步： 比如你要添加一个文件xxx到本地仓库，使用命令 “git add xxx”，可以使用“git add .”自动判断添加哪些文件
          
          然后把这个添加提交到本地的仓库，使用命令 ”git commit -m ”说明这次的提交“ “
          
          最后把本地仓库origin提交到远程的GitHub仓库，使用命令 ”git push origin master“

          这里已经有一种报错信息。处理方法如下       
             To prevent you from losing history, non-fast-forward updates were rejected
             Merge the remote changes before pushing again.  See the 'non-fast forward'
             section of 'git push --help' for details.
             问题（Non-fast-forward）的出现原因在于：git仓库中已经有一部分代码，
             所以它不允许你直接把你的代码覆盖上去。于是你有2个选择方式：
             1，强推，即利用强覆盖方式用你本地的代码替代git仓库内的内容
             git push -f


                                  3 从GitHub克隆项目到本地
                                  
                                  第一步： 到GitHub的某个仓库，然后复制右边的有个“HTTPS clone url”
                                  
                                  第二步： 回到要存放的目录下，使用命令 "git clone https://github.com/chenguolin/scrapy.git"，红色的url只是一个例子
                                  
                                  第三步： 如果本地的版本不是最新的，可以使用命令 “git fetch origin”，origin是本地仓库
                                  
                                  第四步： 把更新的内容合并到本地分支，可以使用命令 “git merge origin/master”
                                  
                                  如果你不想手动去合并，那么你可以使用： git pull <本地仓库> master // 这个命令可以拉去最新版本并自动合并
                                  
                                  4 GitHub的分支管理
                                  
                                  创建
                                  
                                  1 创建一个本地分支： git branch <新分支名字>
                                  
                                  2 将本地分支同步到GitHub上面： git push <本地仓库名> <新分支名>
                                  
                                  3 切换到新建立的分支： git checkout <新分支名>
                                  
                                  4 为你的分支加入一个新的远程端： git remote add <远程端名字> <地址>
                                  
                                  5 查看当前仓库有几个分支: git branch
                                  
                                  删除
                                  
                                  1 从本地删除一个分支： git branch -d <分支名称>
                                  
                                  2 同步到GitHub上面删除这个分支： git push <本地仓库名> :
                                  
                                  5 常见错误
                                  
                                  1 如果出现报错为ERROR: Repository not found.fatal: The remote end hung up unexpectedly
                                  则代表你的 origin 的url 链接有误，可能是创建错误，
                                  也可能是这个 git@github.com:xxx/new-project.git url 指定不正确。重新创建。
                                  

                                  


'''       
            color.cp(h)
        if k=='codestyle':
            h='''
                              主要介绍python 模块编码的基本风格
                               1..起始行 ：通常只有unix环境才能使用起始行，有起始行就能够仅仅输入脚本名来执行脚本。举例#/usr/bin/env python
                               2.模块文档  ''this is test moudle''可以通过moudle.__doc__来访问这些内容
                                           这个可以参见cgi模块的写法  """ """这种写法还是蛮常见的
                               3.模块导入    import sys
                               4.（全局）变量定义 a=3   
                               5.类定义      class Foocalass  通过class.__doc__来访问类的文档
                               6.函数定义    def   函数的文档可以通过function.__doc__来访问
                               7.主程序    if __name__=='__main__'  主程序只是作为测试使用，核心编程上面讲的有些和我的理解不同
                               


'''
            color.cp(h)
        if k=='keyword':
            h='''
                  0.目前对关键字的理解为python中一些内置的词语
                  1.关键字，使用import keyword ，然后使用import keyword ，然后keyword？？
                    就可以看见python的关键字体
                 
                    







'''
            color.cp(h)
        if k=='huanhang':
            h='''
             1.当一句话还没有在一行输入完成的的时候，可以使用\来完成换行书写
                 比如： if k=='ipython'\
                        or k=='or': #这样和其写在一行的效果是一样的
             2.采用像这种（）的符号来完成换行书写
            3.采用print (tupe ')

                          (tupe ')的方式来完成换行书写（注意这里是三引号）    







'''
            color.cp(h)

        if k=='comment':
            h='''
              1.使用#来作为注释的起始符，可以放在任何位置




'''
            color.cp(h)
        if k=='moudle':

            h='''
                     0.记住绝大多数模块的目的是为了import而不是作为脚本去执行
                     1.访问以一个模块的变量可以如下，如：假如sheet模块中有一个变量a=5，
                       那么应该是sheet.a就可以访问到这个变量
                     2.模块函数的访问可以通过shee.show（）这种方式来访问
                     3.模块没有缩进的代码再导入的时候，无论如何都会被执行，所以在写代码的时候除非必要，请把代码
                       写入到函数当中
                     4.通常主程序模块中含有大量可以被执行的顶级代码（没有缩进的），其他被导入的模块应该只有很少的
                       顶级执行代码，所有的功能应该被放在函数中或者类当中。 
                     5.通常只有一个模块被用python .py的方式或批处理等其他方式执行，其他的模块被作为导入。 
                                         



'''
        if k=='help':
            h='''

               1. 使用help（函数名）即将能调用python内嵌的帮助说明
               2. dir(obj) 展示对象的属性
               3.len(obj)   展示对象的长度
           

'''
            color.cp(h)
        if k=='encode':
            h='''
                    Python字符编码详解
                      本文简单介绍了各种常用的字符编码的特点，并介绍了在python2.x中如何与编码问题作战 ：）
                      请注意本文关于Python的内容仅适用于2.x，3.x中str和unicode有翻天覆地的变化，请查阅其他相关文档。
                      尊重作者的劳动，转载请注明作者及原文地址 >.<
                      1. 字符编码简介1.1. ASCIIASCII(American Standard Code for Information Interchange)，是一种单字节的编码。
                      计算机世界里一开始只有英文，而单字节可以表示256个不同的字符，
                      可以表示所有的英文字符和许多的控制符号。不过ASCII只用到了其中的一半（\x80以下），
                      这也是MBCS得以实现的基础。
                      1.2. MBCS然而计算机世界里很快就有了其他语言，单字节的ASCII已无法满足需求。后来每个语言就制定了一套自己的编码，
                      由于单字节能表示的字符太少，而且同时也需要与ASCII编码保持兼容，所以这些编码纷纷使用了多字节来表示字符，
                      如GBxxx、BIGxxx等等，他们的规则是，如果第一个字节是\x80以下，则仍然表示ASCII字符；
                      而如果是\x80以上，则跟下一个字节一起（共两个字节）表示一个字符，然后跳过下一个字节，继续往下判断。
                      这里，IBM发明了一个叫Code Page的概念，将这些编码都收入囊中并分配页码，GBK是第936页，也就是CP936。
                      所以，也可以使用CP936表示GBK。
                      MBCS(Multi-Byte Character Set)是这些编码的统称。目前为止大家都是用了双字节，
                      所以有时候也叫做DBCS(Double-Byte Character Set)。必须明确的是，MBCS并不是某一种特定的编码，
                      Windows里根据你设定的区域不同，MBCS指代不同的编码，而Linux里无法使用MBCS作为编码。
                      在Windows中你看不到MBCS这几个字符，因为微软为了更加洋气，使用了ANSI来吓唬人，
                      记事本的另存为对话框里编码ANSI就是MBCS。同时，在简体中文Windows默认的区域设定里，指代GBK。
                      1.3. Unicode后来，有人开始觉得太多编码导致世界变得过于复杂了，让人脑袋疼，于是大家坐在一起拍脑袋想出来一个方法：
                      所有语言的字符都用同一种字符集来表示，这就是Unicode。
                      最初的Unicode标准UCS-2使用两个字节表示一个字符，所以你常常可以听到Unicode使用两个字节表示一个字符的说法。
                      但过了不久有人觉得256*256太少了，还是不够用，于是出现了UCS-4标准，它使用4个字节表示一个字符，不过我们用的最多的仍然是UCS-2。
                      UCS(Unicode Character Set)还仅仅是字符对应码位的一张表而已，比如"汉"这个字的码位是6C49。
                      字符具体如何传输和储存则是由UTF(UCS Transformation Format)来负责。
                      一开始这事很简单，直接使用UCS的码位来保存，这就是UTF-16，比如，"汉"直接使用\x6C\x49保存(UTF-16-BE)，
                      或是倒过来使用\x49\x6C保存(UTF-16-LE)。但用着用着美国人觉得自己吃了大亏，以前英文字母只需要一个字节就能保存了，
                      现在大锅饭一吃变成了两个字节，空间消耗大了一倍……于是UTF-8横空出世。
                      UTF-8是一种很别扭的编码，具体表现在他是变长的，并且兼容ASCII，ASCII字符使用1字节表示。
                      然而这里省了的必定是从别的地方抠出来的，你肯定也听说过UTF-8里中文字符使用3个字节来保存吧？
                      4个字节保存的字符更是在泪奔……（具体UCS-2是怎么变成UTF-8的请自行搜索）
                      另外值得一提的是BOM(Byte Order Mark)。我们在储存文件时，文件使用的编码并没有保存，
                      打开时则需要我们记住原先保存时使用的编码并使用这个编码打开，这样一来就产生了许多麻烦。
                      （你可能想说记事本打开文件时并没有让选编码？不妨先打开记事本再使用文件 -> 打开看看）
                      而UTF则引入了BOM来表示自身编码，如果一开始读入的几个字节是其中之一，则代表接下来要读取的文字使用的编码是相应的编码：
                      BOM_UTF8 '\xef\xbb\xbf'
                      BOM_UTF16_LE '\xff\xfe'
                      BOM_UTF16_BE '\xfe\xff'
                      并不是所有的编辑器都会写入BOM，但即使没有BOM，Unicode还是可以读取的，
                      只是像MBCS的编码一样，需要另行指定具体的编码，否则解码将会失败。
                      你可能听说过UTF-8不需要BOM，这种说法是不对的，只是绝大多数编辑器在没有BOM时都是以UTF-8作为默认编码读取
                      。即使是保存时默认使用ANSI(MBCS)的记事本，在读取文件时也是先使用UTF-8测试编码，
                      如果可以成功解码，则使用UTF-8解码。记事本这个别扭的做法造成了一个BUG：
                      如果你新建文本文件并输入"姹塧"然后使用ANSI(MBCS)保存，再打开就会变成"汉a"，你不妨试试 ：）
                      

                 2. Python2.x中的编码问题
                      
                 2.1. str和unicodestr和unicode都是basestring的子类。
                      严格意义上说，str其实是字节串，它是unicode经过编码后的字节组成的序列。
                      对UTF-8编码的str'汉'使用len()函数时，结果是3，因为实际上，UTF-8编码的'汉' == '\xE6\xB1\x89'。
                      unicode才是真正意义上的字符串，对字节串str使用正确的字符编码进行解码后获得，并且len(u'汉') == 1。
                      再来看看encode()和decode()两个basestring的实例方法，理解了str和unicode的区别后，这两个方法就不会再混淆了：
                      
                      # coding: UTF-8
                       
                      u = u'汉'
                      print repr(u) # u'\u6c49'
                      s = u.encode('UTF-8')
                      print repr(s) # '\xe6\xb1\x89'
                      u2 = s.decode('UTF-8')
                      print repr(u2) # u'\u6c49'
                       
                      # 对unicode进行解码是错误的
                      # s2 = u.decode('UTF-8')
                      # 同样，对str进行编码也是错误的
                      # u2 = s.encode('UTF-8')
                      需要注意的是，虽然对str调用encode()方法是错误的，但实际上Python不会抛出异常，
                      而是返回另外一个相同内容但不同id的str；对unicode调用decode()方法也是这样。
                      很不理解为什么不把encode()和decode()分别放在unicode和str中而是都放在basestring中，但既然已经这样了，我们就小心避免犯错吧。
                  2.2. 字符编码声明源代码文件中，如果有用到非ASCII字符，则需要在文件头部进行字符编码的声明，如下：
                      1
                      #-*- coding: UTF-8 -*-
                      实际上Python只检查#、coding和编码字符串，其他的字符都是为了美观加上的。
                      另外，Python中可用的字符编码有很多，并且还有许多别名，还不区分大小写，
                      比如UTF-8可以写成u8。参见http://docs.python.org/library/codecs.html#standard-encodings。
                      另外需要注意的是声明的编码必须与文件实际保存时用的编码一致，
                      否则很大几率会出现代码解析异常。现在的IDE一般会自动处理这种情况
                      ，改变声明后同时换成声明的编码保存，但文本编辑器控们需要小心 ：）
                  2.3. 读写文件内置的open()方法打开文件时，read()读取的是str，
                      读取后需要使用正确的编码格式进行decode()。write()写入时，如果参数是unicode，
                      则需要使用你希望写入的编码进行encode()，如果是其他编码格式的str，则需要先用该str的编码进行decode()，
                      转成unicode后再使用写入的编码进行encode()。如果直接将unicode作为参数传入write()方法，Python将先使用源代码文件声明的字符编码进行编码然后写入。
                      
                      # coding: UTF-8
                       
                      f = open('test.txt')
                      s = f.read()
                      f.close()
                      print type(s) # <type 'str'>
                      # 已知是GBK编码，解码成unicode
                      u = s.decode('GBK')
                       
                      f = open('test.txt', 'w')
                      # 编码成UTF-8编码的str
                      s = u.encode('UTF-8')
                      f.write(s)
                      f.close()
                      另外，模块codecs提供了一个open()方法，可以指定一个编码打开文件，
                      使用这个方法打开的文件读取返回的将是unicode。写入时，如果参数是unicode，
                      则使用open()时指定的编码进行编码后写入；如果是str，则先根据源代码文件声明的字符编码，
                      解码成unicode后再进行前述操作。相对内置的open()来说，这个方法比较不容易在编码上出现问题。
                      
                      # coding: GBK
                       
                      import codecs
                       
                      f = codecs.open('test.txt', encoding='UTF-8')
                      u = f.read()
                      f.close()
                      print type(u) # <type 'unicode'>
                       
                      f = codecs.open('test.txt', 'a', encoding='UTF-8')
                      # 写入unicode
                      f.write(u)
                       
                      # 写入str，自动进行解码编码操作
                      # GBK编码的str
                      s = '汉'
                      print repr(s) # '\xba\xba'
                      # 这里会先将GBK编码的str解码为unicode再编码为UTF-8写入
                      f.write(s)
                      f.close()
                      2.4. 与编码相关的方法sys/locale模块中提供了一些获取当前环境下的默认编码的方法。
                      
                      # coding:gbk
                       
                      import sys
                      import locale
                       
                      def p(f):
                          print '%s.%s(): %s' % (f.__module__, f.__name__, f())
                       
                      # 返回当前系统所使用的默认字符编码
                      p(sys.getdefaultencoding)
                       
                      # 返回用于转换Unicode文件名至系统文件名所使用的编码
                      p(sys.getfilesystemencoding)
                       
                      # 获取默认的区域设置并返回元祖(语言, 编码)
                      p(locale.getdefaultlocale)
                       
                      # 返回用户设定的文本数据编码
                      # 文档提到this function only returns a guess
                      p(locale.getpreferredencoding)
                       
                      # \xba\xba是'汉'的GBK编码
                      # mbcs是不推荐使用的编码，这里仅作测试表明为什么不应该用
                      print r"'\xba\xba'.decode('mbcs'):", repr('\xba\xba'.decode('mbcs'))
                       
                      #在笔者的Windows上的结果(区域设置为中文(简体, 中国))
                      #sys.getdefaultencoding(): gbk
                      #sys.getfilesystemencoding(): mbcs
                      #locale.getdefaultlocale(): ('zh_CN', 'cp936')
                      #locale.getpreferredencoding(): cp936
                      #'\xba\xba'.decode('mbcs'): u'\u6c49'
                      3.一些建议3.1. 使用字符编码声明，并且同一工程中的所有源代码文件使用相同的字符编码声明。
                      这点是一定要做到的。
                      3.2. 抛弃str，全部使用unicode。按引号前先按一下u最初做起来确实很不习惯而且经常会忘记再跑回去补，
                      但如果这么做可以减少90%的编码问题。如果编码困扰不严重，可以不参考此条。
                      3.3. 使用codecs.open()替代内置的open()。如果编码困扰不严重，可以不参考此条。
                      3.4. 绝对需要避免使用的字符编码：MBCS/DBCS和UTF-16。这里说的MBCS不是指GBK什么的都不能用，
                      而是不要使用Python里名为'MBCS'的编码，除非程序完全不移植。
                      Python中编码'MBCS'与'DBCS'是同义词，指当前Windows环境中MBCS指代的编码。
                      Linux的Python实现中没有这种编码，所以一旦移植到Linux一定会出现异常！另外，
                      只要设定的Windows系统区域不同，MBCS指代的编码也是不一样的。分别设定不同的区域运行2.4小节中的代码的结果：
                      
                      #中文(简体, 中国)
                      #sys.getdefaultencoding(): gbk
                      #sys.getfilesystemencoding(): mbcs
                      #locale.getdefaultlocale(): ('zh_CN', 'cp936')
                      #locale.getpreferredencoding(): cp936
                      #'\xba\xba'.decode('mbcs'): u'\u6c49'
                       
                      #英语(美国)
                      #sys.getdefaultencoding(): UTF-8
                      #sys.getfilesystemencoding(): mbcs
                      #locale.getdefaultlocale(): ('zh_CN', 'cp1252')
                      #locale.getpreferredencoding(): cp1252
                      #'\xba\xba'.decode('mbcs'): u'\xba\xba'
                       
                      #德语(德国)
                      #sys.getdefaultencoding(): gbk
                      #sys.getfilesystemencoding(): mbcs
                      #locale.getdefaultlocale(): ('zh_CN', 'cp1252')
                      #locale.getpreferredencoding(): cp1252
                      #'\xba\xba'.decode('mbcs'): u'\xba\xba'
                       
                      #日语(日本)
                      #sys.getdefaultencoding(): gbk
                      #sys.getfilesystemencoding(): mbcs
                      #locale.getdefaultlocale(): ('zh_CN', 'cp932')
                      #locale.getpreferredencoding(): cp932
                      #'\xba\xba'.decode('mbcs'): u'\uff7a\uff7a'
                      可见，更改区域后，使用mbcs解码得到了不正确的结果，所以，
                      当我们需要使用'GBK'时，应该直接写'GBK'，不要写成'MBCS'。
                      UTF-16同理，虽然绝大多数操作系统中'UTF-16'是'UTF-16-LE'的同义词，
                      但直接写'UTF-16-LE'只是多写3个字符而已，
                      而万一某个操作系统中'UTF-16'变成了'UTF-16-BE'的同义词，
                      就会有错误的结果。实际上，UTF-16用的相当少，但用到的时候还是需要注意。
                      --END--
                      刚好碰到编码问题，谢谢了！整理的相当到位
                      支持(0)反对(0)
                        
                      #2楼 2010-12-16 10:42 iTech  
                      顶,我用过str.decode
                      支持(0)反对(0)
                        
                      #3楼 2011-05-04 10:06 fykknd  
                      太专业了，看不懂啊
                      支持(0)反对(0)
                        
                      #4楼 2011-11-14 17:42 XueM  
                      楼主好：
                      请教您一个问题：像这样的"&#20320;"这样的字符串，怎样转换成汉字呢？
                      支持(0)反对(0)
                        
                      #5楼[楼主] 2011-11-14 22:30 AstralWind  
                      @XueM
                      弄清楚"&#20320;"这样的HTML转义符使用的是Unicode码表就很容易了：
                      
                      >>> hex(20320)
                      '0x4f60'
                      >>> u'你'
                      u'\u4f60'
                      >>> unichr(int("&#20320;"[2:-1]))
                      u'\u4f60'
                      支持(0)反对(0)
                        
                      #6楼 2011-11-24 17:24 XueM  
                      @AstralWind
                      您好，上次请教的问题非常感谢，我在编码这方面还是有很多疑问：
                      比如下面这几种：
                      旅行，
                      '\xe6\x97\x85\xe8\xa1\x8c'，
                      u'\u65c5\u884c'
                      \u65c5\u884c
                      怎样将这些编码转换成中文呢？
                      支持(0)反对(0)
                        
                      #7楼 2011-12-29 15:58 YuxuanWang  
                      楼主讲真不错
                      简单清晰
                      很多年都搞不清楚编码问题，这个清楚了，多谢
                      支持(0)反对(0)
                        
                      #8楼 2012-01-17 19:35 鸪斑兔  
                      Solaris上是这样，能否解释一下？
                      >>> u = u'汉'
                      >>> print repr(u)
                      u'\xba\xba'
                      >>> s = u.encode('UTF-8')
                      >>> print repr(s)
                      '\xc2\xba\xc2\xba'
                      >>>
                      支持(0)反对(0)
                        
                      #9楼[楼主] 2012-02-04 00:21 AstralWind  
                      引用XueM：
                      @AstralWind
                      您好，上次请教的问题非常感谢，我在编码这方面还是有很多疑问：
                      比如下面这几种：
                      旅行，
                      '\xe6\x97\x85\xe8\xa1\x8c'，
                      u'\u65c5\u884c'
                      \u65c5\u884c
                      怎样将这些编码转换成中文呢？
                      
                      你还是没有明白意思，字节串本身是不带编码信息的，所以必须你事先知道字节串使用的编码才能进行正确的解码。
                      解码得到的就是unicode了，在码表中对应的就是中文。
                      但是两种不同的编码一般会存在一些互相不同的“真空区域”，如果字节串中包含这里面的字节，解
                      码时会抛出异常。中文我们一般都是使用GBK和UTF-8居多，所以有一个方法就是依次使用这两种编码尝试解码，
                      哪个没有抛出异常就认为是哪种编码格式。
                      这个方法并不是完全准确。比如我文章里有写到的记事本bug，
                      演示的就是同样的字节串使用不同的编码格式进行解码得到了不同的结果，很难说哪种编码格式是正确的。
                      支持(1)反对(0)
                        
                      #10楼[楼主] 2012-02-04 00:27 AstralWind  
                      引用tuzkee：
                      Solaris上是这样，能否解释一下？
                      >>> u = u'汉'
                      >>> print repr(u)
                      u'\xba\xba'
                      >>> s = u.encode('UTF-8')
                      >>> print repr(s)
                      '\xc2\xba\xc2\xba'
                      >>>
                      
                      这种情况确实有问题，不过我的suse linux和windows上都没有重现
                      >>> u = u'汉'
                      >>> u
                      u'\u6c49'
                      >>> repr(u)
                      "u'\\u6c49'"
                      >>>
                      我没有使用过solaris环境，初步估计可能是输入法写入了 \xba\xba（GBK编码而不是unicode)，
                      终端上却显示为 汉 的缘故。
                      支持(0)反对(0)
                        
                      #11楼 2012-03-11 21:30 松下裤腰带  
                      楼主请看下我这是什么情况：
                      >>> #coding:utf-8
                      >>> u = u'汉'
                      >>> print repr(u)
                      u'\xba\xba'
                      >>> s = u.encode('utf-8')
                      >>> print repr(s)
                      '\xc2\xba\xc2\xba'
                      >>> u2 = s.decode('utf-8')
                      >>> print repr(u2)
                      u'\xba\xba'
                      >>>
                      我用的是Xp。python2.7
                      支持(0)反对(0)
                        
                      #12楼[楼主] 2012-03-13 21:21 AstralWind  
                      @scncpb
                      你这个问题与楼上一位用solaris的同学一模一样……
                      但我在我的xp坏境下跑了一遍没有这个问题。
                      我不一定能解决这个问题，只能试试看：
                      如果你方便的话请贴一下
                      sys.getdefaultencoding()
                      locale.getdefaultlocale()
                      locale.getpreferredencoding()
                      这几个方法的结果（需要引入相关模块）
                      支持(0)反对(0)
                        
                      #13楼 2012-03-13 22:48 松下裤腰带  
                      >>> print sys.getdefaultencoding()
                      ascii
                      >>> print locale.getdefaultlocale()
                      ('zh_CN', 'cp936')
                      >>> print locale.getpreferredencoding()
                      cp936
                      >>>
                      谢谢。。。
                      支持(0)反对(0)
                        
                      #14楼[楼主] 2012-03-14 00:06 AstralWind  
                      @scncpb
                      这个问题我搞不定…… 我会转给大牛们去分析的，有结论以后再通知你
                      支持(0)反对(0)
                        
                      #15楼[楼主] 2012-03-14 01:06 AstralWind  
                      @scncpb
                      你再试试看print u'\xba\xba'会有什么结果?
                      支持(0)反对(0)
                        
                      #16楼 2012-03-14 16:17 松下裤腰带  
                      >>> print u'\xba\xba'
                      ºº
                      >>>
                      谢谢哈。。。
                      支持(0)反对(0)
                        
                      #17楼[楼主] 2012-03-15 00:25 AstralWind  
                      @scncpb
                      这个问题与python没有关系，你可以试试看把这些代码写入文件中执行，结果应该是正确的。
                      具体问题由于不在现场不好判断…
                      支持(0)反对(0)
                        
                      #18楼 2012-03-30 11:27 ade921068180  
                      楼主好：
                      像上面说的'\xe6\x97\x85\xe8\xa1\x8c'
                      直接print 就可以正常显示“旅行”
                      而我的系统默认编码是ascii，
                      sys.getdefaultencoding()
                      显示:acsii
                      我能不能理解为上面的字符串编码格式就是ascii呀？
                      
                      还有，像这种情况，直接打印显示正常，但是我写到.html文件中，
                      打开的时候，就显示乱码，是什么意思，怎么办呀？
                      楼主赐教~
                      支持(0)反对(0)
                        
                      #19楼 2012-04-02 10:28 ade921068180  
                      楼主，#为什么第一组总是4个字符呢"hell"呢
                      
                      import re
                      pattern=re.compile(r'(\w+)(\w+)(?P<sign>.*)')
                      m=pattern.match('hello beautiful world! sdf asdf aaa bbb')
                      i=1
                      print m.groups()
                      while i<=len(m.groups()):
                      print m.group(i)
                      i=i+1
                      
                      我感觉自己还是对(?P<sign>.*)不明白
                      支持(0)反对(0)
                        
                      #20楼 2012-04-21 10:45 mimicom  
                      UCS和Unicode是一回事么?
                      怎么看到, (Universal Character Set，UCS) 这样的.
                      UCS的U不是Unicode ?
                      支持(0)反对(0)
                        
                      #21楼 2012-05-21 20:48 Jesse_Luo  
                      @ade921068180
                      大约是html需要指定字符集是utf-8，head里加上
                      <meta charset="UTF-8">
                      支持(0)反对(0)
                        
                      #22楼 2012-10-25 14:10 mimicom  
                      我又来看了一遍... 呵呵...
                      支持(0)反对(0)
                        
                      #23楼 2012-12-24 17:25 Honghe  
                      引用而Linux里无法使用MBCS作为编码
                      
                      为何？
                      支持(0)反对(0)
                        
                      #24楼 2013-09-06 20:42 itatkakaxi2  
                      大牛说话真幽默，很好，很强大
                      支持(0)反对(0)
                        
                      #25楼 2013-09-16 15:54 自加吧，少年  
                      非常有价值！
                      支持(0)反对(0)
                        
                      #26楼 2013-12-17 15:50 Arts&Crafts  
                      
                      s = '汉'
                      u = u'汉'
                      s2 = u.encode('UTF-8')
                      print repr(s)       #输出   '\xe6\xb1\x89'
                      print repr(s2)     #输出   '\xe6\xb1\x89'
                      
                      
                      我有一个疑问：Python中默认的编码集为ASCII。如你所说 str 实际上是一个字节串,
                      也就是说 s 指向的是一个 unicode 编码后的字节串。u 进行 UTF-8编码后出的字节串是
                      '\xe6\xb1\x89', 可是Python自动对 s 进行编码后字节串也是 '\xe6\xb1\x89'
                      也就是说Python自动按照UTF-8对'汉'进行编码,可是Python默认的编码集明明是ASCII这不是有点矛盾吗？
                      支持(0)反对(1)
                        
                      #27楼 2014-06-03 19:24 唔知叫咩名  
                      很好，感谢。
                      支持(0)反对(0)
                        
                      #28楼 2014-10-10 15:18 neter_zeng  
                      @Arts&Crafts
                      你可以在编辑器中显示汉字而不报错，说明你已经在文件头已经声明成为utf-8的编码了。
                      在有的编辑器中，如果是这样声明，相应的文件编码就也默认为utf-8，所以你这个s就是utf-8编码过。
                      这样和你 u‘汉' 先变成unicode码，然后再转成utf-8是一样的。
                      支持(1)反对(0)
                        
                      #29楼 2014-10-22 14:11 死侍  
                      写的好 ！！！
                      支持(0)反对(0)
                        
                      #30楼 2014-10-23 10:14 唔知叫咩名  
                      非常好。
                      支持(0)反对(0)
                        
                      #31楼 2014-12-03 17:42 reyleon  
                      写的真不错, 学习了
                      支持(0)反对(0)
                        
                      #32楼 2015-05-17 12:42 平和的心  
                      学习了，在Py2中用unicode，我用from __future__ import unicode_literals，这样不用在字符串前面加u了
                      支持(1)反对(0)
                        
                      #33楼 2015-10-30 17:06 ferraborghini  
                      赞一个，python使用的pymssql也出现解码错误的问题。还有2.7.9出现编码问题，在其它版本就没有，头疼
                      支持(0)反对(0)
                        
                      #34楼 2016-01-25 12:01 偷包贼  
                      太太太太给力了！谢谢博主
                      支持(0)反对(0)
                        
                      #35楼 2016-03-09 16:18 l33k  
                      专门注册了一个账户来点赞，博主说得太好了，一解多年的疑惑
 
'''
            color.cp(h)
        if k=='cmd':
            h='''
            1.dir 展示目录下面的内容
            2.cd 跳转到想要的目录    

'''  
            color.cp(h)

        if k=='windows':
            h='''
            1.在winr 中输入taskmgr 打开任务管理器
            2.mstc ip 远程连接常见的主机      



'''
            color.cp(h)
        if k=='vim':

            h='''


                            # 文件管理
                            
                            
                            :e              重载这个文件
                            :q              退出
                            :q!             退出并不保存
                            :w              写文件
                            :w {file}       写新文件
                            :x              写文件并退出
                            :wq             退出并保存
                            
                            # 整块选中，复制与删除
                            1.shift +v  先选中（上下移动）
                            2.然后按Y（按d进行删除）
                            3.然后在需要位置进行按 p 粘贴
                            
                            #关于python的设置
                            #
                            
                            
                            #块操作
                                shift+v 进行选中
                                (实在不行就使用ctrl +v来控制，但记得将光标移动到相应位置,目前看来ctrl+v更靠谱)
                            
                                shift+i 选中后进行挪动位置
                                直接操作
                                esc
                                然后按下键
                            
                            
                            
                            # 移动
                            
                                k
                              h   l         基本的按键
                                j
                            
                            w               下一个单词开始的头部
                            W               next start of whitespace-delimited word
                            e               下一个单词的尾部
                            E               next end of whitespace-delimited word
                            b               前一个单词的头部
                            B               previous start of whitespace-delimited word
                            0               从这一行的开头开始
                            $               从这一行末尾开始
                            gg              去这个文件的第一行
                            G               去这个文件的末尾
                            
                            
                            # 插入
                            #   退出插入模式使用 Esc or Ctrl-C
                            #   以下模式进入插入模式并作相应修改:
                            
                            a               在光标后面进行追加
                            A               在这一行后面进行追加
                            i               在光标前面插入
                            I               在这一行的开头开始插入
                            o               在光标下创建新的一行
                            O               在光标上面创建新的一行
                            R               enter insert mode but replace instead of inserting chars
                            :r {file}       insert from file
                            
                            # 编辑
                            
                            u               撤销
                            yy              复制一行
                            y{motion}       yank text that {motion} moves over
                            p               在光标后面粘贴
                            P               在光标前粘贴
                            <Del> or x      删除一个单词
                            dd              删除一行
                            d{motion}       delete text that {motion} moves over
                            
                            
                            # Preceding a motion or edition with a number repeats it n times
                            # Examples:
                            50k         moves 50 lines up
                            2dw         删除2单词
                            5yy         复制5行
                            42G         去42行


'''
            color.cp(h)
        if k=='n':
            h='''
                 对象
                 多态
                 代码组：我们把缩进相同的语句称为一个代码块或一个代码组
                 封装
                 继承
                 方法：当我们在谈方法的时候，我们在说 类中像函数一样的东西
                 脚本
                 特性   
                 属性：从目前看来指的是类里面直接带的属性。y1=em('yangming',55)  或则说括号里的东西 def __init__(self, name, salary) 
                 类变量                    
                 命名空间
                 主体：我么把没有缩进的代码块是最层次的，被称为脚本的主体部分
                 模块：我们目前的理解是以.py文件结束的是模块
                 主程序模块：目前的理解为包含ifname那块的模块
                 顶级代码：一般我们称没有缩进的代码为顶级代码
                 引用计数：当一个对象（整数，字符串，或其他的类型）创建并被赋值给变量的时候，那么他的引用计数就变为1
                           当同一个对象又被赋值给其他变量，或作为参数传递给函数，方法，或实例的时候，则该对象的一个新的引用就被创建了
                           该对象的应用引用计数自动加1.  这里会有垃圾回收机制，注意这一点
              




'''

            
            color.cp(h)
            
        if k=='xshell':
            h='''
                shift +上 向上移动
                shift +下 向下移动
                alt+1     切换至第一个选项卡（其他的类似）
                shift+pgdn 向上翻页
                shift+pgdn  向下翻页  





'''
            color.cp(h)
        if k=='continue':
            h='''



'''  
        if k=='break':
            h='''
              这立即将展示如何跳出循环
              from amth import sqrt
              for n in range(99,0,-1):
                  root =sqrt(n)
                  if root==int(root):
                      print n
                      break    





'''
            color.cp(h) 
        if k=='assert':
            h='''
                 #这样的代码产生的时候，就是让错误条件出现的时候早点崩溃
                   age=-1
                   assert 0<age<100.'you should do' 
                  这样做系将会残生报错信息
'''

            color.cp(h)  
        if k=='in':
            h='''
          1.    x in y #这是判断关系的一种，记住和x==y是一样的道理
                      这里表示x是y容器（序列）的成员 x not in y 内推就行
              #x is y  表示x和y是同一个对象
          2. 成员资格运算符的解释
              name=raw_input('what your name?')
              if 's' in  name:
                  print 'your name contain letter ''s''              
    







'''
            ccolor.cp(h) 
        if k=='fuzhi':
            h='''
              1.同时进行多个赋值操作
                 x,y,z=1,2,3# 两边其实都是元组，最好加上元组符号(x,y)=(1,'yangming')
                 print x,y,z#同时打印多个表达式
                 x=y=z=1 这种也极为常见 
             2.简易赋值模式
               x=x+1  可以写为    
               x+=1
             3.python 不支持x++ 这一类的操作
             4.交换两个变量里面的值很简单 x,y=y,x                 
 
             


'''
            color.cp(h)
        if k=='if':
            h='''
            A.elif主要用于多重判断
                if a:
                    do 
                elif b:
                    do
                else:
                    do      
           B.嵌套代码块(if 语句里面嵌套使用if语句)
               if a:
                   if b:
                       do
                   elif c:
                       do
                   elif d:
                       do
                   else:
                       do
               else:
                   do    


'''
            color.cp(h)
        if k=='jiaoben':
            h='''
                           #!/usr/bin/env python
                           #上面这一句话在只有一个python环境中可以这样使用
                           print 'heelo'
                           保存好后使用./hello来运行程序（必不可少）
                           然后改变他的模式chmod 777 hello 
                           当然python sth.py更好




  
'''
            color.cp(h) 
        if k=='python':

            h='''
                     在shell当中，使用python -V 命令即将获得python版本信息
                     >>> 这个是py的提示符号
                   

 
'''

            color.cp(h)
        if k=='input':
            h='''
            k= input('you wan to express:')
             这个函数即将接受一个赋值，然后可以用变量做事情
            L=raw_input('you can')
             这里即便你输入yangmng 也会被当作字符窜，而上面必须加入引号
  
            


'''
            color.cp(h)
        if k=='json':

            h='''
Json概述以及python对json的相关操作
什么是json：

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。易于人阅读和编写
。同时也易于机器解析和生成。它基于JavaScript Programming Language, 
Standard ECMA-262 3rd Edition - December 1999的一个子集。
JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯
（包括C, C++, C#, Java, JavaScript, Perl, Python等）。这些特性使JSON成为理想的数据交换语言。
JSON建构于两种结构：
“名称/值”对的集合（A collection of name/value pairs）。不同的语言中，它
被理解为对象（object），纪录（record），结构（struct），字典（dictionary），
哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。
值的有序列表（An ordered list of values）。在大部分语言中，它被理解为数组（array）。
这些都是常见的数据结构。事实上大部分现代计算机语言都以某种形式支持它们。
这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
jso官方说明参见：http://json.org/
Python操作json的标准api库参考：http://docs.python.org/library/json.html
对简单数据类型的encoding 和 decoding：
使用简单的json.dumps方法对简单数据类型进行编码，例如：

import json
 
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print repr(obj)
print encodedjson
输出：
[[1, 2, 3], 123, 123.123, 'abc', {'key2': (4, 5, 6), 'key1': (1, 2, 3)}]
[[1, 2, 3], 123, 123.123, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]
通过输出的结果可以看出，简单类型通过encode之后跟其原始的repr()输出结果非常相似，
但是有些数据类型进行了改变，例如上例中的元组则转换为了列表。在json的编码过程中，
会存在从python原始类型向json类型的转化过程，具体的转化对照如下：

json.dumps()方法返回了一个str对象encodedjson，我们接下来在对encodedjson进行decode，
得到原始数据，需要使用的json.loads()函数：

decodejson = json.loads(encodedjson)
print type(decodejson)
print decodejson[4]['key1']
print decodejson
输出：
<type 'list'>
[1, 2, 3]
[[1, 2, 3], 123, 123.123, u'abc', {u'key2': [4, 5, 6], u'key1': [1, 2, 3]}]
loads方法返回了原始的对象，但是仍然发生了一些数据类型的转化。
比如，上例中‘abc’转化为了unicode类型。从json到python的类型转化对照如下：

json.dumps方法提供了很多好用的参数可供选择，比较常用的有sort_keys
（对dict对象进行排序，我们知道默认dict是无序存放的），separators，indent等参数。
排序功能使得存储的数据更加有利于观察，也使得对json输出的对象进行比较，例如：
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2,sort_keys=True)
print d1
print d2
print d3
print d1==d2
print d1==d3
输出：
{"a": 123, "b": 789, "c": 456}
{"a": 123, "c": 456, "b": 789}
{"a": 123, "b": 789, "c": 456}
False
True
上例中，本来data1和data2数据应该是一样的，但是由于dict存储的无序特性，造成两者无法比较。
因此两者可以通过排序后的结果进行存储就避免了数据比较不一致的情况发生，但是排序后再进行存储，
系统必定要多做一些事情，也一定会因此造成一定的性能消耗，所以适当排序是很重要的。
indent参数是缩进的意思，它可以使得数据存储的格式变得更加优雅。

data1 = {'b':789,'c':456,'a':123}
d1 = json.dumps(data1,sort_keys=True,indent=4)
print d1
输出：
{
    "a": 123,
    "b": 789,
    "c": 456
}
输出的数据被格式化之后，变得可读性更强，但是却是通过增加一些冗余的空白格来进行填充的。
json主要是作为一种数据通信的格式存在的，而网络通信是很在乎数据的大小的，
无用的空格会占据很多通信带宽，所以适当时候也要对数据进行压缩。
separator参数可以起到这样的作用，该参数传递是一个元组，包含分割对象的字符串。
print 'DATA:', repr(data)
print 'repr(data)             :', len(repr(data))
print 'dumps(data)            :', len(json.dumps(data))
print 'dumps(data, indent=2)  :', len(json.dumps(data, indent=4))
print 'dumps(data, separators):', len(json.dumps(data, separators=(',',':')))
输出：
DATA: {'a': 123, 'c': 456, 'b': 789}
repr(data)             : 30
dumps(data)            : 30
dumps(data, indent=2)  : 46
dumps(data, separators): 25
通过移除多余的空白符，达到了压缩数据的目的，而且效果还是比较明显的。
另一个比较有用的dumps参数是skipkeys，默认为False。 dumps方法存储dict对象时
，key必须是str类型，如果出现了其他类型的话，那么会产生TypeError异常，如果开启该参数，设为True的话，则会比较优雅的过度。
data = {'b':789,'c':456,(1,2):123}
print json.dumps(data,skipkeys=True)
输出：
{"c": 456, "b": 789}
 
处理自己的数据类型
json模块不仅可以处理普通的python内置类型，也可以处理我们自定义的数据类型，而往往处理自定义的对象是很常用的。
首先，我们定义一个类Person。
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'Person Object name : %s , age : %d' % (self.name,self.age)
if __name__  == '__main__':
    p = Person('Peter',22)
    print p
如果直接通过json.dumps方法对Person的实例进行处理的话，会报错，因为json无法支持这样的自动转化。
通过上面所提到的json和python的类型转化对照表，可以发现，
object类型是和dict相关联的，所以我们需要把我们自定义的类型转化为dict，然后再进行处理。这里，有两种方法可以使用。
方法一：自己写转化函数

Created on 2011-12-14
@author: Peter

import Person
import json
 
p = Person.Person('Peter',22)
 
def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d
 
def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = class_(**args) #create new instance
    else:
        inst = d
    return inst
 
d = object2dict(p)
print d
#{'age': 22, '__module__': 'Person', '__class__': 'Person', 'name': 'Peter'}
 
o = dict2object(d)
print type(o),o
#<class 'Person.Person'> Person Object name : Peter , age : 22
 
dump = json.dumps(p,default=object2dict)
print dump
#{"age": 22, "__module__": "Person", "__class__": "Person", "name": "Peter"}
 
load = json.loads(dump,object_hook = dict2object)
print load
#Person Object name : Peter , age : 22
上面代码已经写的很清楚了，实质就是自定义object类型和dict类型进行转化。object2dict函数将对象模块名、类名以及__dict__存储在dict对象里，并返回。dict2object函数则是反解出模块名、类名、参数，创建新的对象并返回。在json.dumps 方法中增加default参数，该参数表示在转化过程中调用指定的函数，同样在decode过程中json.loads方法增加object_hook,指定转化函数。
方法二：继承JSONEncoder和JSONDecoder类，覆写相关方法
JSONEncoder类负责编码，主要是通过其default函数进行转化，我们可以override该方法。同理对于JSONDecoder。

import Person
import json
 
p = Person.Person('Peter',22)
 
class MyEncoder(json.JSONEncoder):
    def default(self,obj):
        #convert object to a dict
        d = {}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d
 
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=self.dict2object)
    def dict2object(self,d):
        #convert dict to object
        if'__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module,class_name)
            args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
            inst = class_(**args) #create new instance
        else:
            inst = d
        return inst
 
 
d = MyEncoder().encode(p)
o =  MyDecoder().decode(d)
 
print d
print type(o), o
 
对于JSONDecoder类方法，稍微有点不同，但是改写起来也不是很麻烦。看代码应该就比较清楚了。



'''
            color.cp('h')
        if k=='vmtools':
            vmtools='''

                 1.点击选项卡里面安装vmtools
        2.cd / media/Vm*
        3.cp *tar.gz  /tmp/
        4.cd /tmp/
        5.tar *tar.gz
        6.cd distribute*

	1. ./*.pl
	2. 然后按需求确定
	3. reboot


'''

            color.cp(vmtools)
    

			
        if k=='file':

            file='''
                         总是记不住API。昨晚写的时候用到了这些，但是没记住，于是就索性整理一下吧：
                         
                         python中对文件、文件夹（文件操作函数）的操作需要涉及到os模块和shutil模块。
                         
                         得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
                         
                         返回指定目录下的所有文件和目录名:os.listdir()
                         
                         函数用来删除一个文件:os.remove()
                         
                         删除多个目录：os.removedirs（r“c：\python”）
                         
                         检验给出的路径是否是一个文件：os.path.isfile()
                         
                         检验给出的路径是否是一个目录：os.path.isdir()
                         
                         判断是否是绝对路径：os.path.isabs()
                         
                         检验给出的路径是否真地存:os.path.exists()
                         
                         返回一个路径的目录名和文件名:os.path.split()  
                            eg os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt')
                         
                         
                         分离扩展名：os.path.splitext()
                         
                         获取路径名：os.path.dirname()
                         
                         获取文件名：os.path.basename()
                         
                         运行shell命令: os.system()
                         
                         读取和设置环境变量:os.getenv() 与os.putenv()
                         
                         给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
                         
                         指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
                         
                         重命名：os.rename（old， new）
                         
                         创建多级目录：os.makedirs（r“c：\python\test”）
                         
                         创建单个目录：os.mkdir（“test”）
                         
                         获取文件属性：os.stat（file）
                         
                         修改文件权限与时间戳：os.chmod（file）
                         
                         终止当前进程：os.exit（）
                         
                         获取文件大小：os.path.getsize（filename）
                         
                         
                         文件操作：
                         os.mknod("test.txt")        创建空文件
                         fp = open("test.txt",w)     直接打开一个文件，如果文件不存在则创建文件
                         
                         关于open 模式：
                         
                         w     以写方式打开，
                         a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
                         r+     以读写模式打开
                         w+     以读写模式打开 (参见 w )
                         a+     以读写模式打开 (参见 a )
                         rb     以二进制读模式打开
                         wb     以二进制写模式打开 (参见 w )
                         ab     以二进制追加模式打开 (参见 a )
                         rb+    以二进制读写模式打开 (参见 r+ )
                         wb+    以二进制读写模式打开 (参见 w+ )
                         ab+    以二进制读写模式打开 (参见 a+ )
                         



                        fp.read([size])                     #size为读取的长度，以byte为单位

                   fp.readline([size])     
                        #读一行，如果定义了size，有可能返回的只是一行的一部分

                     fp.readlines([size])   
             #把文件每一行作为一个list的一个成员，并返回这个list。
           其实它的内部是通过循环调用readline()来实现的。
             如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。

                       fp.write(str)    
                  #把str写到文件中，write()并不会在str后加上一个换行符

                  fp.writelines(seq)     
       #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。

                      fp.close()        
                #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证
              ，最好还是养成自己关闭的习惯。  如果一个文件在关闭后还对其进行操作会产生ValueError

                          fp.flush()    
                                  #把缓冲区的内容写入硬盘

                      fp.fileno()             
                         #返回一个长整型的”文件标签“

                       fp.isatty()           
                           #文件是否是一个终端设备文件（unix系统中的）

                          fp.tell()              
                           #返回文件操作标记的当前位置，以文件的开头为原点

                          fp.next()                 
                      #返回下一行，并将文件操作标记位移到下一行。
                  把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。

                  fp.seek(offset[,whence])  
            #将文件打操作标记移到offset的位置。
                  这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了
                     ，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。
                2表示以文件末尾为原点进行计算。
              需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。

                fp.truncate([size])    
                   #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
             如果size比文件的大小还要大，依据系统的不同可能是不改变文件，
              也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。



目录操作：
os.mkdir("file")  
 创建目录
复制文件：
shutil.copyfile("oldfile","newfile") 
      oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")  
 oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
复制文件夹：
shutil.copytree("olddir","newdir") 
       olddir和newdir都只能是目录，且newdir必须不存在
重命名文件（目录）
os.rename("oldname","newname")   
    文件或目录都是使用这条命令
移动文件（目录）
shutil.move("oldpos","newpos")
删除文件
os.remove("file")
删除目录
os.rmdir("dir")只能删除空目录
shutil.rmtree("dir")    空目录、有内容的目录都可以删
转换目录
os.chdir("path")   换路径



相关例子

 1 将文件夹下所有图片名称加上'_fc'

python代码:

# -*- coding:utf-8 -*-
import re
import os
import time
#str.split(string)分割字符串
#'连接符'.join(list) 将列表组成字符串
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
            i+=1 #注意这里的i是一个陷阱
        #或者
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        #if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用


                  img_dir = 'D:\\xx\\xx\\images'
                  img_dir = img_dir.replace('\\','/')
                  start = time.time()
                  i = 0
                  change_name(img_dir)
                  c = time.time() - start
                  print('程序运行耗时:%0.2f'%(c))
                  print('总共处理了 %s 张图片'%(i))
                  
                  输出结果：
                  
                  程序运行耗时:0.11
                  总共处理了 109 张图片


'''
            color.cp(file)
        if k=='obj':
            obj='''


OOP术语概述

类: 用户定义的原型对象，它定义了一套描述类的任何对象的属性。属性是数据成员(类变量和实例变量)和方法，通过点符号访问。

类变量：这是一个类的所有实例共享的变量。类变量在类，但外面的任何类的方法定义。类变量不被用作经常作为实例变量。

数据成员：保存与类和对象关联的数据的类变量或实例变量。

函数重载：一个以上的行为特定功能的分配。执行的操作所涉及的对象(自变量)的类型不同而不同。

实例变量：所定义的方法内，只属于一个类的当前实例的变量。

继承：类的特点，即都是由它派生其他类的转移。

实例：某一类的一个单独对象。属于类Circle一个obj对象，例如，是类Circle的一个实例。

实例化：创建一个类的实例。

Method : 一种特殊的函数，函数在类定义中定义。

对象：这是由它的类中定义的数据结构的唯一实例。一个对象包括两个数据成员(类变量和实例变量)和方法。

运算符重载：一个以上的函数功能，特定的操作符分配。




创建类：
                             类语句将创建一个新的类定义。类的名称紧跟在关键字class后跟一个冒号，如下所示：


                          class ClassName:
                             'Optional class documentation string'
                             class_suite
                          类有一个文档字符串，它可以通过类名.__ doc__访问。

                          class_suite由所有定义的类成员，数据属性与函数组件的语句。

                          例子
                          下面是一个简单的Python类的例子：

                          class Employee:
                              'Common base class for all employees'
                              empCount = 0

                              def __init__(self, name, salary):
                                  self.name = name
                                  self.salary = salary
                                  Employee.empCount += 1

                              def displayCount(self):
                                  print "Total Employee %d" % Employee.empCount

                              def displayEmployee(self):
                                  print "Name : ", self.name,  ", Salary: ", self.salary
                          empCount是一个类变量，其值将是这个类的所有实例共享。这可以从类中或外部进行访问，访问形式为 Employee.empCount。

                          第一个方法__init__()是一种特殊的方法，这就是所谓的类构造函数或当创建该类的一个新实例Python调用的初始化方法。

                          声明就像正常函数中一样，不同的是第一个参数到每个方法是类的方法。 Python增加了self参数列表;不需要把调用的方法都它列入。

                          创建实例对象：
                          要创建一个类的实例，调用类名并传递任何参数给__init__方法接收。

                          "This would create first object of Employee class"
                          emp1 = Employee("Zara", 2000)
                          "This would create second object of Employee class"
                          emp2 = Employee("Manni", 5000)
                          访问属性：
                          可以访问使用点运算符来访问对象的属性。而类变量使用类名来访问，如下所示：

                          emp1.displayEmployee()
                          emp2.displayEmployee()
                          print "Total Employee %d" % Employee.empCount
                          现在，把所有的概念放在一起：

                          #!/usr/bin/python

                          class Employee:
                             'Common base class for all employees'
                             empCount = 0

                             def __init__(self, name, salary):
                                self.name = name
                                self.salary = salary
                                Employee.empCount += 1

                             def displayCount(self):
                               print "Total Employee %d" % Employee.empCount

                             def displayEmployee(self):
                                print "Name : ", self.name,  ", Salary: ", self.salary

                          "This would create first object of Employee class"
                          emp1 = Employee("Zara", 2000)
                          "This would create second object of Employee class"
                          emp2 = Employee("Manni", 5000)
                          emp1.displayEmployee()
                          emp2.displayEmployee()
                          print "Total Employee %d" % Employee.empCount
                          当执行上面的代码，产生以下结果：

                          Name :  Zara ,Salary:  2000
                          Name :  Manni ,Salary:  5000
                          Total Employee 2
                          在任何时候可以添加，删除或修改类和对象的属性：

                          emp1.age = 7  # Add an 'age' attribute.
                          emp1.age = 8  # Modify 'age' attribute.
                          del emp1.age  # Delete 'age' attribute.
                          除了使用正常的语句来访问属性，可以使用以下函数：

                          getattr(obj, name[, default]) : 访问对象的属性。

                          hasattr(obj,name) : 检查一个属性是否存在。

                          setattr(obj,name,value) : 设置一个属性。如果属性不存在，那么它将被创建。

                          delattr(obj, name) : 要删除一个属性。

                          hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
                          getattr(emp1, 'age')    # Returns value of 'age' attribute
                          setattr(emp1, 'age', 8) # Set attribute 'age' at 8
                          delattr(empl, 'age')    # Delete attribute 'age'
                          内置的类属性：
                          每个Python类会继续并带有内置属性，他们可以使用点运算符像任何其他属性一样来访问：

                          __dict__ : 字典包含类的命名空间。

                          __doc__ : 类的文档字符串，或None如果没有定义。

                          __name__: 类名称。

                          __module__: 在类中定义的模块名称。此属性是在交互模式其值为“__main__”。

                          __bases__ : 一个可能是空的元组包含了基类，其在基类列表出现的顺序。

                          对于上面的类，尝试访问这些属性：

                          #!/usr/bin/python

                          class Employee:
                             'Common base class for all employees'
                             empCount = 0

                             def __init__(self, name, salary):
                                self.name = name
                                self.salary = salary
                                Employee.empCount += 1

                             def displayCount(self):
                               print "Total Employee %d" % Employee.empCount

                             def displayEmployee(self):
                                print "Name : ", self.name,  ", Salary: ", self.salary

                          print "Employee.__doc__:", Employee.__doc__
                          print "Employee.__name__:", Employee.__name__
                          print "Employee.__module__:", Employee.__module__
                          print "Employee.__bases__:", Employee.__bases__
                          print "Employee.__dict__:", Employee.__dict__
                          当执行上面的代码，产生以下结果：

                          Employee.__doc__: Common base class for all employees
                          Employee.__name__: Employee
                          Employee.__module__: __main__
                          Employee.__bases__: ()
                          Employee.__dict__: {'__module__': '__main__', 'displayCount':
                          <function displayCount at 0xb7c84994>, 'empCount': 2,
                          'displayEmployee': <function displayEmployee at 0xb7c8441c>,
                          '__doc__': 'Common base class for all employees',
                          '__init__': <function __init__ at 0xb7c846bc>}





                          销毁对象（垃圾回收）：

                             Python的删除不需要的对象（内建类型或类的实例），自动释放内存空间。
                             由Python定期回收的内存块不再使用的过程被称为垃圾收集。

                             Python的垃圾回收器在程序执行过程中运行，当一个对象的引用计数为零时触发。
                             一个对象的引用计数改变为指向它改变别名的数量。

                             当它分配一个新的名字或放置在容器（列表，元组或字典）的对象的引用计数增加。
                             当对象的引用计数减少使用 del 删除，其基准被重新分配，或者它的引用超出范围。
                             当一个对象的引用计数变为零，Python会自动地收集它。

                             a = 40      # Create object <40>
                             b = a       # Increase ref. count  of <40>
                             c = [b]     # Increase ref. count  of <40>

                             del a       # Decrease ref. count  of <40>
                             b = 100     # Decrease ref. count  of <40>
                             c[0] = -1   # Decrease ref. count  of <40>
                             当垃圾回收器销毁孤立的实例，并回收其空间一般不会注意到。但是，一个类可以实现特殊方法__del__()，
                             称为析构函数被调用时，该实例将被摧毁。这个方法可以用于清理所用的一个实例的任何非内存资源。


                             例子：
                             __del__()析构函数打印实例，它即将被销毁的类名：

                             #!/usr/bin/python

                             class Yiibai:
                                def __init( self, x=0, y=0):
                                   self.x = x
                                   self.y = y
                                def __del__(self):
                                   class_name = self.__class__.__name__
                                   print class_name, "destroyed"

                             pt1 = Yiibai()
                             pt2 = pt1
                             pt3 = pt1
                             print id(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
                             del pt1
                             del pt2
                             del pt3
                             当执行上面的代码，它产生以下结果：

                             3083401324 3083401324 3083401324
                             Yiibai destroyed
                             注意：理想情况下，应该定义类的单独的文件，那么应该使用import语句将其导入主程序文件。
                             详细请查看Python- 模块章节，导入模块和类的更多细节。

类继承：
                 不用从头开始，可以通过上面列出的括号父类的新类名后，从一个已经存在的类派生它创建一个类。

                 子类继承父类的属性，可以使用父类的这些属性，就好像它们是在子类中定义的一样。
                 子类也可以覆盖父类的数据成员和方法。

                 语法
                 派生类的声明很像它们的父类; 从基类的列表后给出类名继承：

                 class SubClassName (ParentClass1[, ParentClass2, ...]):
                    'Optional class documentation string'
                    class_suite
                 例子
                 #!/usr/bin/python

                 class Parent:        # define parent class
                     parentAttr = 100
                     def __init__(self):
                         print "Calling parent constructor"

                     def parentMethod(self):
                         print 'Calling parent method'

                     def setAttr(self, attr):
                         Parent.parentAttr = attr

                     def getAttr(self):
                         print "Parent attribute :", Parent.parentAttr

                 class Child(Parent): # define child class
                     def __init__(self):
                         print "Calling child constructor"

                     def childMethod(self):
                         print 'Calling child method'

                 c = Child()          # instance of child
                 c.childMethod()      # child calls its method
                 c.parentMethod()     # calls parent's method
                 c.setAttr(200)       # again call parent's method
                 c.getAttr()          # again call parent's method
                 当执行上面的代码，产生以下结果：

                 Calling child constructor
                 Calling child method
                 Calling parent method
                 Parent attribute : 200
                 类似的方式，可以按如下继承多个父类的类：

                 class A:        # define your class A
                 .....

                 class B:         # define your calss B
                 .....

                 class C(A, B):   # subclass of A and B
                 .....
                 可以使用issubclass()或isinstance()函数来检查两个类和实例的关系。

                 issubclass(sub, sup) 如果给定的子类子确实是超sup的子类布尔函数返回true。

                 isinstance(obj, Class) 如果obj是Class类的实例，或者是类的一个子类的实例布尔函数返回true

重写方法：
                 可以覆盖父类的方法。原因之一重写父的方法，因为可能想在子类特殊或实现不同的功能。

                 例子
                 #!/usr/bin/python

                 class Parent:        # define parent class
                     def myMethod(self):
                         print 'Calling parent method'

                 class Child(Parent): # define child class
                     def myMethod(self):
                         print 'Calling child method'

                 c = Child()          # instance of child
                 c.myMethod()         # child calls overridden method
                 当执行上面的代码，产生以下结果：

                 Calling child method
                 基础重载方法：
                 下表列出了一些通用的功能，可以在类重写中：

                 SN	方法，说明与调用示例
                 1	__init__ ( self [,args...] )
                 构造函数（任何可选参数）
                 简单调用 : obj = className(args)
                 2	__del__( self )
                 析构函数，删除一个对象
                 简单调用 : del obj
                 3	__repr__( self )
                 可求值的字符串表示形式
                 简单调用 : repr(obj)
                 4	__str__( self )
                 可打印字符串表示形式
                 简单调用 : str(obj)
                 5	__cmp__ ( self, x )
                 对象比较
                 简单调用 : cmp(obj, x) 重载运算符：
                 假设要创建了一个Vector类来表示二维向量，当使用加运算符来增加他们发生了什么？最有可能是Python会屌你。

                 可以，但是定义__add__方法在类中进行矢量相加，再加上操作符的行为会按预期：

                 例子：
                 #!/usr/bin/python

                 class Vector:
                    def __init__(self, a, b):
                        self.a = a
                        self.b = b

                    def __str__(self):
                        return 'Vector (%d, %d)' % (self.a, self.b)


                    def __add__(self,other):
                        return Vector(self.a + other.a, self.b + other.b)

                 v1 = Vector(2,10)
                 v2 = Vector(5,-2)
                 print v1 + v2
                 当执行上面的代码，产生以下结果：

                 Vector(7,8)
                 数据隐藏：
                 对象的属性可以是或可以不在类定义外部可见。
                 对于这些情况，可以命名以双下划线前缀属性，这些属性将无法直接让外部可视。

                 例子：
                 #!/usr/bin/python

                 class JustCounter:
                     __secretCount = 0

                     def count(self):
                         self.__secretCount += 1
                         print self.__secretCount


                 counter = JustCounter()
                 counter.count()
                 counter.count()
                 print counter.__secretCount
                 当执行上面的代码，产生以下结果：

                 1
                 2
                 Traceback (most recent call last):
                   File "test.py", line 12, in <module>
                     print counter.__secretCount
                 AttributeError: JustCounter instance has no attribute '__secretCount'
                 Python的保护成员通过内部更改名称以包含类名。
                 可以访问这些属性通过object._className__attrName。如果想更换最后一行，那么它会工作如下：

                 .........................
                 print counter._JustCounter__secretCount
                 当执行上面的代码，产生以下结果：

                 1
                 2
                 2


'''
            color.cp(obj)
        if k=='tupe':
            h='''Python 元组
                 Python的元组与列表类似，不同之处在于元组的元素不能修改。
                 元组使用小括号，列表使用方括号。
                 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
                 如下实例：
                 tup1 = ('physics', 'chemistry', 1997, 2000);
                 tup2 = (1, 2, 3, 4, 5 );
                 tup3 = "a", "b", "c", "d";
                 创建空元组
                 tup1 = ();
                 元组中只包含一个元素时，需要在元素后面添加逗号
                 tup1 = (50,);
                 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
                 访问元组
                 元组可以使用下标索引来访问元组中的值，如下实例:
                 #!/usr/bin/python

                 tup1 = ('physics', 'chemistry', 1997, 2000);
                 tup2 = (1, 2, 3, 4, 5, 6, 7 );

                 print "tup1[0]: ", tup1[0]
                 print "tup2[1:5]: ", tup2[1:5]
                 以上实例输出结果：
                 tup1[0]:  physics
                 tup2[1:5]:  (2, 3, 4, 5)
                 修改元组
                 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
                 #!/usr/bin/python
                 # -*- coding: UTF-8 -*-

                 tup1 = (12, 34.56);
                 tup2 = ('abc', 'xyz');

                 # 以下修改元组元素操作是非法的。
                 # tup1[0] = 100;

                 # 创建一个新的元组
                 tup3 = tup1 + tup2;
                 print tup3;
                 以上实例输出结果：
                 (12, 34.56, 'abc', 'xyz')
                 删除元组
                 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
                 #!/usr/bin/python

                 tup = ('physics', 'chemistry', 1997, 2000);

                 print tup;
                 del tup;
                 print "After deleting tup : "
                 print tup;
                 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
                 ('physics', 'chemistry', 1997, 2000)
                 After deleting tup :
                 Traceback (most recent call last):
                   File "test.py", line 9, in <module>
                     print tup;
                 NameError: name 'tup' is not defined
                 元组运算符
                 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
                 Python 表达式	结果	描述
                 len((1, 2, 3))	3	计算元素个数
                 (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
                 ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制
                 3 in (1, 2, 3)	True	元素是否存在
                 for x in (1, 2, 3): print x,	1 2 3	迭代
                 元组索引，截取
                 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
                 元组：
                 L = ('spam', 'Spam', 'SPAM!')
                 Python 表达式	结果	描述
                 L[2]	'SPAM!'	读取第三个元素
                 L[-2]	'Spam'	反向读取；读取倒数第二个元素
                 L[1:]	('Spam', 'SPAM!')	截取元素
                 无关闭分隔符
                 任意无符号的对象，以逗号隔开，默认为元组，如下实例：
                 #!/usr/bin/python

                 print 'abc', -4.24e93, 18+6.6j, 'xyz';
                 x, y = 1, 2;
                 print "Value of x , y : ", x,y;
                 以上实例允许结果：
                 abc -4.24e+93 (18+6.6j) xyz
                 Value of x , y : 1 2
                 元组内置函数
                 Python元组包含了以下内置函数
                 序号	方法及描述
                 1	cmp(tuple1, tuple2)
                 比较两个元组元素。
                 2	len(tuple)
                 计算元组元素个数。
                 3	max(tuple)
                 返回元组中元素最大值。
                 4	min(tuple)
                 返回元组中元素最小值。
                 5	tuple(seq)
                 将列表转换为元组。

'''
            color.cp(h)

        if k=='myidea':
            h='''

                     3.23 建立一个大字典，来实现个性化搜索
                     3.26 在python里面添加一个词典，然后就可以在本地查单词语
'''
            color.cp(h)

        if k=='range':
            h='''
                    range(5)=[0,1,2,3,4]

'''
            color.cp(h)

        if k=='dict':

            h='''
                 python学习笔记——字典

                 A.创建

                 方法一:

                 >>> dict1 = {}
                 >>> dict2 = {'name': 'earth', 'port': 80}
                 >>> dict1, dict2
                 ({}, {'port': 80, 'name': 'earth'})
                 方法二:从Python 2.2 版本起，可以使用一个工厂方法，传入一个元素是列表的元组作为参数

                 >>> fdict = dict((['x', 1], ['y', 2]))
                 >>> fdict
                 {'x': 1,'y': 2 }
                 方法三:

                 从Python 2.3 版本起, 可以用一个很方便的内建方法fromkeys() 来创建一个"默认"字典,

                  字典中元素具有相同的值 (如果没有给出， 默认为None，这个有点像我框架的oneObject方法):

                 >>> ddict = {}.fromkeys(('x', 'y'), -1)
                 >>> ddict
                 {'y': -1, 'x': -1}
                 >>>
                 >>> edict = {}.fromkeys(('foo', 'bar'))
                 >>> edict
                 {'foo': None, 'bar': None}


                B. 访问字典中的值
                 想遍历一个字典(一般用键), 你只需要循环查看它的键, 像这样:

                 >>> dict2 = {'name': 'earth', 'port': 80}
                 >>>
                 >>>> for key in dict2.keys():
                 ... print 'key=%s, value=%s' % (key, dict2[key])
                 ...
                 key=name, value=earth
                 key=port, value=80
                 从Python 2.2 开始，可以直接在 for 循环里遍历字典。

                 >>> dict2 = {'name': 'earth', 'port': 80}
                 >>>
                 >>>> for key in dict2:
                 ... print 'key=%s, value=%s' % (key, dict2[key])
                 ...
                 key=name, value=earth
                 key=port, value=80
                 想判定其是否存在某个键值对，可以使用has_key()或 in 、 not in 操作符

                 >>> 'server' in dict2 # 或 dict2.has_key('server')
                 False
                 >>> 'name' in dict # 或 dict2.has_key('name')
                 True
                 >>> dict2['name']
                 'earth'
                 一个字典中混用数字和字符串的例子：

                 >>> dict3 = {}
                 >>> dict3[1] = 'abc'
                 >>> dict3['1'] = 3.14159
                 >>> dict3[3.2] = 'xyz'
                 >>> dict3
                 {3.2: 'xyz', 1: 'abc', '1': 3.14159}


                c. 更新字典


                 采取覆盖更新

                 上例中 dict2['name']='earth';

                 更新 dict2['name']='abc';

                 删除字典元素和字典

                 del dict2['name'] # 删除键为“name”的条目

                 dict2.clear() # 删除dict2 中所有的条目

                 del dict2 # 删除整个dict2 字典

                 dict2.pop('name') # 删除并返回键为“name”的条目

                 dict2 = {'name': 'earth', 'port': 80}
                 >>> dict2.keys()
                 ['port', 'name']
                 >>>
                 >>> dict2.values()
                 [80, 'earth']
                 >>>
                 >>> dict2.items()
                 [('port', 80), ('name', 'earth')]
                 >>>
                 >>> for eachKey in dict2.keys():
                 ... print 'dict2 key', eachKey, 'has value', dict2[eachKey]
                 ...
                 dict2 key port has value 80
                 dict2 key name has value earth
                 update()方法可以用来将一个字典的内容添加到另外一个字典中


                 dict3 = {'server': 'http', 'port': 80, 'host': 'venus'}
                 >>> dict3.clear()
                 >>> dict3
                 {}
                 映射类型相关的函数

                 >>> dict(x=1, y=2)
                 {'y': 2, 'x': 1}
                 >>> dict8 = dict(x=1, y=2)
                 >>> dict8
                 {'y': 2, 'x': 1}
                 >>> dict9 = dict(**dict8)
                 >>> dict9
                 {'y': 2, 'x': 1}

                 dict9 = dict8.copy()
'''
            color.cp(h)

        if k=='ipython':

            h='''
                A.tab 补全系列
                     1.tab 键盘自动补全

                     2.在任何对象后面加一个.然后按下tab键就可以完成方法和属性的输入
                       例如：d=[q,2,3,4] d.<tab> 就会出现相应的东西
                             import datetime
                             datetime.<tab>
                     3.当在输入路径的时候，按tab也可以完成自动补全
                 B.内省
                     1.在变量的前面或后面加上？，就会显示变量的相关信息
                     2.如果该对象是一个函数，那么他的docstring 部分被显示出来 就是在函数下面“”“ ”“” 引用起来的部分
                     3.在函数向后面使用？？将会把函数的源代码打印出来
                     4.这里有一个搜索命名空间,主要是命名空间没搞懂
                     5.如果是模块，使用 模块名？？即将展示模块代码

                C.%run（ 在python会话环境中运行脚本,并且其中的变量可以访问）
                    %run /usr/lib/ed.py 该脚本中的文件中的变量是可以放问的

                D.按下ctrl+c就可以中断正在执行执行的程序

                E.执行剪切板的代码%paste %cpaste(可以进行持续粘贴)

                f.在python2.6的版本可以使用如下命令安装ipython
                  pip install -v 'ipython<2'
                g.ipython 快捷键
                  ctrl-L 清屏幕
                  ctrl-P 向上搜索输入的以文本开头的命令
                  ctrl-N 向下搜索................的命令
                h.异常和跟踪
                  %xmode 在这这里的讲解非常好
                i. 魔术命令（理解为ipython中的命令行程序）
                  %magic 显示所有魔术命令的文档
                  %hist  打印命令的输入历史
                  %pdb  异常发生后自动进入调试
                  %debug 从最新的异常跟踪的地方进入调试器
                  %quickref 显示ipython的快速参考
                  %page object  分页显示目标
                  %run  sth.py 在ipython中执行一个python脚本
                  注意：还有很多没来的及理解
                J.与系统自带的shell进行交互
                  1. 示意
                     !cal -j 2016
                  2.让其进行赋值 a=!cal -j 2016  然后可以打印a

                  3.
                K.与操作系统进行交互
                 !cmd  在shell中执行cmd
                 %alias command    让系统的命令变成python内置命令 这里一退出当前的命令窗口，就不再有效
                 %alais 展示已经生成的快捷链接
                 %store  name 保存变量 alias 等到ipython的数据库
                 %stroe -r   可以恢复之前的设置

                 %cd  dir   将系统的工作目录改为dir
                 %env  返回当前系统的环境变量
                 %dhis 返回目录访问历史
                  
           
                L.ipython自带的书签系统（目录系统）
                 %bookmark sp /usr/lib/python2.6/site-packages 然后这个将永久存储下来
                 %cd sp  就会直接跳转到该工作目录  
                 %bookmark -l 会展示出所有书签 
                                  
                M. IPyhton HTML notebook
                N.ipython的个性化
                  
                  1.寻找ipython_config.py精心修改可以改动ipython的（颜色，输出，快捷名，alias等等 ）
                  2.对应文件进行修改，就可以获得你需要的东西
                  3.量身定制ipython为某个项目或程序请参考在线文档
                  


'''
            color.cp(h)


        if k=='%store':
            h0='''storemagic
                %store magic for lightweight persistence.
                
                Stores variables, aliases and macros in IPython’s database.
                
                To automatically restore stored variables at startup, add this to your ipython_config.py file:
                
                c.StoreMagics.autorestore = True
                StoreMagics.store(parameter_s='')
                Lightweight persistence for python variables.
                
                Example:
                
                In [1]: l = ['hello',10,'world']
                In [2]: %store l
                In [3]: exit
                
                (IPython session is closed and started again...)
                
                ville@badger:~$ ipython
                In [1]: l
                NameError: name 'l' is not defined
                In [2]: %store -r
                In [3]: l
                Out[3]: ['hello', 10, 'world']
                Usage:
                
                %store - Show list of all variables and their current
                values
                
                %store spam - Store the current value of the variable spam
                to disk
                
                %store -d spam - Remove the variable and its value from storage
                
                %store -z - Remove all variables from storage
                
                %store -r - Refresh all variables from store (overwrite
                current vals)
                
                %store -r spam bar - Refresh specified variables from store
                (delete current val)
                
                %store foo >a.txt - Store value of foo to new file a.txt
                
                %store foo >>a.txt - Append value of foo to file a.txt
                
                It should be noted that if you change the value of a variable, you need to %store it again if you want to persist the new value.
                
                Note also that the variables will need to be pickleable; most basic python types can be safely %store’d.
                
                Also aliases can be %store’d across sessions.
'''
            color.cp(h0)
        if k=='%alias':
            h='''
               Built-in magic commands
               Line magics
               %alias
               Define an alias for a system command.
               
               ‘%alias alias_name cmd’ defines ‘alias_name’ as an alias for ‘cmd’
               
               Then, typing ‘alias_name params’ will execute the system command ‘cmd params’ (from your underlying operating system).
               
               Aliases have lower precedence than magic functions and Python normal variables,
                so if ‘foo’ is both a Python variable and an alias, the alias can not be executed until ‘del foo’ removes the Python variable.
               
               You can use the %l specifier in an alias definition to represent the whole line when the alias is called. For example:
               
               In [2]: alias bracket echo "Input in brackets: <%l>"
               In [3]: bracket hello world
               Input in brackets: <hello world>
               You can also define aliases with parameters using %s specifiers (one per parameter):
               
               In [1]: alias parts echo first %s second %s
               In [2]: %parts A B
               first A second B
               In [3]: %parts A
               Incorrect number of arguments: 2 expected.
               parts is an alias to: 'echo first %s second %s'
               Note that %l and %s are mutually exclusive. You can only use one or the other in your aliases.
               
               Aliases expand Python variables just like system calls using ! or !! do: all expressions prefixed with ‘$’ get expanded.
                For details of the semantic rules, see PEP-215: http://www.python.org/peps/pep-0215.html. 
               This is the library used by IPython for variable expansion. If you want to access a true shell variable,
                an extra $ is necessary to prevent its expansion by IPython:
               
               In [6]: alias show echo
               In [7]: PATH='A Python string'
               In [8]: show $PATH
               A Python string
               In [9]: show $$PATH
               /usr/local/lf9560/bin:/usr/local/intel/compiler70/ia32/bin:...
               You can use the alias facility to acess all of $PATH. See the %rehash and %rehashx functions,
                which automatically create aliases for the contents of your $PATH.
               
               If called with no parameters, %alias prints the current alias table.
               
               %alias_magic
               %alias_magic [-l] [-c] name target
               Create an alias for an existing line or cell magic.
               
               Examples
               
               In [1]: %alias_magic t timeit
               Created `%t` as an alias for `%timeit`.
               Created `%%t` as an alias for `%%timeit`.
               
               In [2]: %t -n1 pass
               1 loops, best of 3: 954 ns per loop
               
               In [3]: %%t -n1
                  ...: pass
                  ...:
               1 loops, best of 3: 954 ns per loop
               
               In [4]: %alias_magic --cell whereami pwd
               UsageError: Cell magic function `%%pwd` not found.
               In [5]: %alias_magic --line whereami pwd
               Created `%whereami` as an alias for `%pwd`.
               
               In [6]: %whereami
               Out[6]: u'/home/testuser'
               positional arguments:
               name Name of the magic to be created. target Name of the existing line or cell magic.
               optional arguments:
               -l, --line	Create a line magic alias.
               -c, --cell	Create a cell magic alias.

'''
            color.cp('h')
        if k=='random':
            h='''
                      random.randint(a, b),返回[a,b]之间的整数

'''
            color.cp(h)
        if k=='platform':
            h='''
                           import platform
                           platform.platform() #获取操作系统名称及版本号，’Windows-7-6.1.7601-SP1′
                           platform.version() #获取操作系统版本号，’6.1.7601′
                           platform.architecture() #获取操作系统的位数，(’32bit’, ‘WindowsPE’)
                           platform.machine() #计算机类型，’x86′
                           platform.node() #计算机的网络名称，’hongjie-PC’
                           platform.processor() #计算机处理器信息，’x86 Family 16 Model 6 Stepping 3, AuthenticAMD’
                           platform.uname() #包含上面所有的信息汇总，uname_result(system=’Windows’, node=’hongjie-PC’,
                           release=’7′, version=’6.1.7601′, machine=’x86′, processor=’x86 Family Model 6 Stepping 3, AuthenticAMD’)
                           还可以获得计算机中python的一些信息：
                           import platform
                           platform.python_build()
                           platform.python_compiler()
                           platform.python_branch()
                           platform.python_implementation()
                           platform.python_revision()
                           platform.python_version()
                           platform.python_version_tuple()


'''   
            color.cp(h)
        if k=='lambda':
            h='''


                                   简单来说，编程中提到的 lambda 表达式，通常是在需要一个函数，
                                   但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
                                   这一用法跟所谓 λ 演算（题目说明里的维基链接）的关系
                                   ，有点像原子弹和质能方程的关系，差别其实还是挺大的。
                                   
                                   不谈形式化的 λ 演算，只说有实际用途的匿名函数。
                                   先举一个普通的 Python 例子：将一个 list 里的每个元素都平方：
                                   map( lambda x: x*x, [y for y in range(10)] )
                                   这个写法要好过
                                   def sq(x):
                                       return x * x
                                   
                                   map(sq, [y for y in range(10)])
                                   ，因为后者多定义了一个（污染环境的）函数，尤其如果这个函数只会使用一次的话。
                                   而且第一种写法实际上更易读，因为那个映射到列表上的函数具体是要做什么，非常一目了然
                                   。如果你仔细观察自己的代码，会发现这种场景其实很常见：
                                   你在某处就真的只需要一个能做一件事情的函数而已，连它叫什么名字都无关紧要。Lambda 表达式就可以用来做这件事。
                                   
                                   进一步讲，匿名函数本质上就是一个函数，它所抽象出来的东西是一组运算。这是什么意思呢？类比
                                   a = [1, 2, 3]
                                   和
                                   f = lambda x : x + 1
                                   ，你会发现，等号右边的东西完全可以脱离等号左边的东西而存在，
                                   等号左边的名字只是右边之实体的标识符。如果你能习惯 [1, 2, 3] 单独存在，
                                   那么 lambda x : x + 1 也能单独存在其实也就不难理解了，它的意义就是给「某个数加一」这一运算本身。
                                   
                                   现在回头来看 map() 函数，它可以将一个函数映射到一个可枚举类型上面。沿用上面给出的 a 和 f，可以写：
                                   map(f, a)
                                   也就是将函数 f 依次套用在 a 的每一个元素上面，获得结果 [2, 3, 4]。现在用 lambda 表达式来替换 f，就变成：
                                   map( lambda x : x + 1, [1, 2, 3] )
                                   会不会觉得现在很一目了然了？尤其是类比
                                   a = [1, 2, 3]
                                   r = []
                                   for each in a:
                                       r.append(each+1)
                                   这样的写法时，你会发现自己如果能将「遍历列表，给遇到的每个元素都做某种运算」
                                   的过程从一个循环里抽象出来成为一个函数 map，
                                   然后用 lambda 表达式将这种运算作为参数传给 map 的话，
                                   考虑事情的思维层级会高出一些来，需要顾及的细节也少了一点。Python 之中，
                                   类似能用到 lambda 表达式的「高级」函数还有 reduce、filter 等等
                                   ，很多语言也都有这样的工具（不过这些特性最好不要在 Python 中用太多，
                                   原因详见 http://www.zhihu.com/question/19794855/answer/12987428 的评论部分）。
                                   这种能够接受一个函数作为参数的函数叫做「高阶函数」（higher-order function），
                                   是来自函数式编程（functional programming）的思想。
                                   
                                   和其他很多语言相比，Python 的 lambda 限制多多，最严重的当属它只能由一条表达式组成。
                                   这个限制主要是为了防止滥用，因为当人们发觉 lambda 很方便，就比较容易滥用，
                                   可是用多了会让程序看起来不那么清晰，毕竟每个人对于抽象层级的忍耐 / 理解程度都有所不同。
                                   
                                   作者：涛吴
                                   链接：http://www.zhihu.com/question/20125256/answer/14058285
                                   来源：知乎
                                   著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
            color.cp(h)

        if k=='color':
            h='''
                     这里是封装的github上的模块，详细地址参见https://github.com/broadinstitute/xtermcolor
                     用法如下
                     import color
                     color.cp('yangming')//前面是string，后面是决定颜色的ascll参数

'''
            color.cp(h)
        if k=='type':

            h= '''
                     这篇文章主要介绍了Python中获取对象信息的方法,是Python学习当中的基础知识,需要的朋友可以参考下
                     当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
                     使用type()
                     首先，我们来判断对象类型，使用type()函数：
                     基本类型都可以用type()判断：
                     >>> type(123)
                     <type 'int'>
                     >>> type('str')
                     <type 'str'>
                     >>> type(None)
                     <type 'NoneType'>

                     如果一个变量指向函数或者类，也可以用type()判断：
                     >>> type(abs)
                     <type 'builtin_function_or_method'>
                     >>> type(a)
                     <class '__main__.Animal'>

                     但是type()函数返回的是什么类型呢？它返回type类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
                     >>> type(123)==type(456)
                     True
                     >>> type('abc')==type('123')
                     True
                     >>> type('abc')==type(123)
                     False

                     但是这种写法太麻烦，Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：
                     >>> import types
                     >>> type('abc')==types.StringType
                     True
                     >>> type(u'abc')==types.UnicodeType
                     True
                     >>> type([])==types.ListType
                     True
                     >>> type(str)==types.TypeType
                     True

                     最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，比如：
                     >>> type(int)==type(str)==types.TypeType
                     True

                     使用isinstance()
                     对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
                     我们回顾上次的例子，如果继承关系是：
                     复制代码 代码如下:
                     object -> Animal -> Dog -> Husky
                     那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
                     >>> a = Animal()
                     >>> d = Dog()
                     >>> h = Husky()

                     然后，判断：
                     >>> isinstance(h, Husky)
                     True

                     没有问题，因为h变量指向的就是Husky对象。
                     再判断：
                     >>> isinstance(h, Dog)
                     True

                     h虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以
                     ，h也还是Dog类型。换句话说，isinstance()判断的是一个对象是否是该类型本身
                     ，或者位于该类型的父继承链上。

                     因此，我们可以确信，h还是Animal类型：
                     >>> isinstance(h, Animal)
                     True

                     同理，实际类型是Dog的d也是Animal类型：
                     >>> isinstance(d, Dog) and isinstance(d, Animal)
                     True

                     但是，d不是Husky类型：
                     能用type()判断的基本类型也可以用isinstance()判断：
                     >>> isinstance('a', str)
                     True
                     >>> isinstance(u'a', unicode)
                     True
                     >>> isinstance('a', unicode)
                     False

                     并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
                     >>> isinstance('a', (str, unicode))
                     True
                     >>> isinstance(u'a', (str, unicode))
                     True

                     由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
                     >>> isinstance(u'a', basestring)
                     True

                     使用dir()
                     如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
                     >>> dir('ABC')
                     ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

                     类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
                     >>> len('ABC')
                     3
                     >>> 'ABC'.__len__()
                     3

                     我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
                     >>> class MyObject(object):
                     ...   def __len__(self):
                     ...     return 100
                     ...
                     >>> obj = MyObject()
                     >>> len(obj)
                     100

                     剩下的都是普通属性或方法，比如lower()返回小写的字符串：
                     >>> 'ABC'.lower()
                     'abc'

                     仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
                     >>> class MyObject(object):
                     ...   def __init__(self):
                     ...     self.x = 9
                     ...   def power(self):
                     ...     return self.x * self.x
                     ...
                     >>> obj = MyObject()

                     紧接着，可以测试该对象的属性：
                     >>> hasattr(obj, 'x') # 有属性'x'吗？
                     True
                     >>> obj.x
                     9
                     >>> hasattr(obj, 'y') # 有属性'y'吗？
                     False
                     >>> setattr(obj, 'y', 19) # 设置一个属性'y'
                     >>> hasattr(obj, 'y') # 有属性'y'吗？
                     True
                     >>> getattr(obj, 'y') # 获取属性'y'
                     19
                     >>> obj.y # 获取属性'y'
                     19

                     如果试图获取不存在的属性，会抛出AttributeError的错误：
                     可以传入一个default参数，如果属性不存在，就返回默认值：
                     >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
                     404

                     也可以获得对象的方法：
                     >>> hasattr(obj, 'power') # 有属性'power'吗？
                     True
                     >>> getattr(obj, 'power') # 获取属性'power'
                     <bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
                     >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
                     >>> fn # fn指向obj.power
                     <bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
                     >>> fn() # 调用fn()与调用obj.power()是一样的
                     81

                     小结
                     通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
                     要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
                     sum = obj.x + obj.y

                     就不要写：
                     sum = getattr(obj, 'x') + getattr(obj, 'y')

                     一个正确的用法的例子如下：
                     def readImage(fp):
                       if hasattr(fp, 'read'):
                         return readData(fp)
                       return None

                     假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
                     如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
                     请注意，在Python这类动态语言中，有read()方法，不代表该fp对象就是一个文件流，
                     它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''

            color.cp(h)
        if k=='ifname':


            h='''
                    核心编程笔记：
                      注：if name 下面是最好跟测试代码的地方
                         这一段被解释为主程序，参见codestyle
                       
                      注： 如果模块是直接被导入，__name__=moudlename
                           如果模块是被直接执行，__name__=__main__




                     解释1：


                        # coding=utf-8
                        sheet.show('all')
                        def do():
                            print '这里打印实验范本'
                        if __name__=='__main__':
                            print '如果这句话是被直接打印出来就说明不是import进来的
                                      ,而是直接python sth.py 的方式执行'
                        else:
                            print ' 这句话被打印出来的时候，
                                    就表示模块是被import进来的'
                        将这一段代码打包成exp.PY 然后分别import 和python exp.py


                     解释3：
                     #以下是更详细的理解
                       python中if __name__ == '__main__': 的解析

                       当你打开一个.py文件时,经常会在代码的最下面看到if __name__ == '__main__':,现在就来介 绍一下它的作用.

                       模块是对象，并且所有的模块都有一个内置属性 __name__。




                       一个模块的 __name__ 的值取决于您如何应用模块。
                       如果 import 一个模块，那么模块__name__ 的值通常为模块文件名，不带路径或者文件扩展名。
                      但是您也可以像一个标准的程序样直接运行模块，
                       在这 种情况下, __name__ 的值将是一个特别缺省"__main__"。







                       ///////////////////////////////////////////////////////////////////////////////////////////////////

                       在cmd 中直接运行.py文件(或者python sth.py),则__name__的值是'__main__';

                       而在import 一个.py文件后,__name__的值就不是'__main__'了;

                       从而用if __name__ == '__main__'来判断是否是在直接运行该.py文件

                       如:

                       #Test.py

                       class Test:

                           def __init(self):
                               pass

                           def f(self):
                               print 'Hello, World!'


                       if __name__ == '__main__':

                           Test().f()

                       #End



                       你在cmd中输入:

                       C:>python Test.py

                       Hello, World!

                       说明:"__name__ == '__main__'"是成立的



                       你再在cmd中输入:

                       C:>python

                       >>>import Test

                       >>>Test.__name__                #Test模块的__name__

                       'Test'

                       >>>__name__                       #当前程序的__name__

                       '__main__'

                       无论怎样,Test.py中的"__name__ == '__main__'"都不会成立的!

                       所以,下一行代码永远不会运行到!
'''
            color.cp(h)
        if k=='string':

            h='''
                   1.判断字符串的长度为空可以采用 len(str)==0来表示信息为空的时候

                 Python 字符串操作（string替换、删除、截取、复制、连接、比较、查找、包含、大小写转换、分割等）
                 Python 字符串操作（string替换、删除、截取、复制、连接、比较、查找、包含、大小写转换、分割等）




                            去空格及特殊符号 (这里只能去掉首和尾的)
                           s.strip() .lstrip() .rstrip(',')
                            Python strip()方法
                            描述
                            Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
                            语法
                            strip()方法语法：
                            str.strip([chars]);
                            参数
                            chars -- 移除字符串头尾指定的字符。
                            返回值
                            返回移除字符串头尾指定的字符生成的新字符串。
                            实例
                            以下实例展示了strip()函数的使用方法：
                            #!/usr/bin/python

                            str = "0000000this is string example....wow!!!0000000";
                            print str.strip( '0' );
                            以上实例输出结果如下：
                            this is string example....wow!!!

                            复制字符串

                           #strcpy(sStr1,sStr)
                           sStr= 'strcpy'
                           sStr = sStr
                           sStr= 'strcpy'
                           print sStr

连接字符串
#strcat(sStr1,sStr)
sStr= 'strcat'
sStr = 'append'
sStr+= sStr
print sStr

查找字符
#strchr(sStr1,sStr)
sStr= 'strchr'
sStr = 's'
nPos = sStr1.index(sStr)
print nPos

比较字符串
#strcmp(sStr1,sStr)
sStr= 'strchr'
sStr = 'strch'
print cmp(sStr1,sStr)

扫描字符串是否包含指定的字符
#strspn(sStr1,sStr)
sStr= '1345678'
sStr = '456'
#sStrand chars both in sStrand sStr
print len(sStrand sStr)

字符串长度
#strlen(sStr1)
sStr= 'strlen'
print len(sStr1)

将字符串中的大小写转换
#strlwr(sStr1)
sStr= 'JCstrlwr'
sStr= sStr1.upper()
#sStr= sStr1.lower()
print sStr

追加指定长度的字符串
#strncat(sStr1,sStr,n)
sStr= '1345'
sStr = 'abcdef'
n = 3
sStr+= sStr[0:n]
print sStr

字符串指定长度比较
#strncmp(sStr1,sStr,n)
sStr= '1345'
sStr = '13bc'
n = 3
print cmp(sStr1[0:n],sStr[0:n])

复制指定长度的字符
#strncpy(sStr1,sStr,n)
sStr= ''
sStr = '1345'
n = 3
sStr= sStr[0:n]
print sStr

将字符串前n个字符替换为指定的字符
#strnset(sStr1,ch,n)
sStr= '1345'
ch = 'r'
n = 3
sStr= n * ch + sStr1[3:]
print sStr

扫描字符串
#strpbrk(sStr1,sStr)
sStr= 'cekjgdklab'
sStr = 'gka'
nPos = -1
for c in sStr1:
     if c in sStr:
         nPos = sStr1.index(c)
         break
print nPos

翻转字符串
#strrev(sStr1)
sStr= 'abcdefg'
sStr= sStr1[::-1]
print sStr

查找字符串
#strstr(sStr1,sStr)
sStr= 'abcdefg'
sStr = 'cde'
print sStr1.find(sStr)

分割字符串
#strtok(sStr1,sStr)
sStr= 'ab,cde,fgh,ijk'
sStr = ','
sStr= sStr1[sStr1.find(sStr) + 1:]
print sStr
 或者
s = 'ab,cde,fgh,ijk'
print(s.split(','))

连接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
PHP 中 addslashes 的实现
def addslashes(s):
     d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)
s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print s
print addslashes(s)

只显示字母与数字
def OnlyCharNum(s,oth=''):
     s = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz013456789'
    for c in s:
        if not c in fomart:
             s = s.replace(c,'');
     return s;
print(OnlyStr("a000 aa-b"))

本文出自 “王伟” 博客，请务必保留此出处http://wangwei007.blog.51cto.com/68019/903426

'''
            color.cp(h)
        if k=='concept':
            h='''
                     标准库 就是把python开发者开发的模块文件内置到python中，标准库包含很多模块文件，就像os，sys模块文件

'''
            color.cp(h)
        if k=='list':
            h='''

			创建列表
			sample_list = ['a',1,('a','b')]
			Python 列表操作
			sample_list = ['a','b',0,1,3]

			得到列表中的某一个值
			value_start = sample_list[0]
			end_value = sample_list[-1]

			删除列表的第一个值
			del sample_list[0]

			在列表中插入一个值
			sample_list[0:0] = ['sample value']

			得到列表的长度
			list_length = len(sample_list)

			列表遍历
			for element in sample_list:
			    print(element)

			Python 列表高级操作/技巧

			产生一个数值递增列表
			num_inc_list = range(30)
			#will return a list [0,1,2,...,29]

			用某个固定值初始化列表
			initial_value = 0
			list_length = 5
			sample_list = [ initial_value for i in range(10)]
			sample_list = [initial_value]*list_length
			# sample_list ==[0,0,0,0,0]


			附：python内置类型
			1、list：列表（即动态数组，C++标准库的vector，但可含不同类型的元素于一个list中）
			a = ["I","you","he","she"]      ＃元素可为任何类型。

			下标：按下标读写，就当作数组处理
			以0开始，有负下标的使用
			0第一个元素，-1最后一个元素，
			-len第一个元 素，len-1最后一个元素
			取list的元素数量
			len(list)   #list的长度。实际该方法是调用了此对象的__len__(self)方法。

			创建连续的list
			L = range(1,5)      #即 L=[1,2,3,4],不含最后一个元素
			L = range(1, 10, 2) #即 L=[1, 3, 5, 7, 9]

			list的方法
			L.append(var)   #追加元素
			L.insert(index,var)
			L.pop(var)      #返回最后一个元素，并从list中删除之
			L.remove(var)   #删除第一次出现的该元素
			L.count(var)    #该元素在列表中出现的个数
			L.index(var)    #该元素的位置,无则抛异常
			L.extend(list)  #追加list，即合并list到L上
			L.sort()        #排序
			L.reverse()     #倒序
			list 操作符:,+,*，关键字del
			a[1:]       #片段操作符，用于子list的提取
			[1,2]+[3,4] #为[1,2,3,4]。同extend()
			[2]*4       #为[2,2,2,2]
			del L[1]    #删除指定下标的元素
			del L[1:3]  #删除指定下标范围的元素
			list的复制
			L1 = L      #L1为L的别名，用C来说就是指针地址相同，对L1操作即对L操作。函数参数就是这样传递的
			L1 = L[:]   #L1为L的克隆，即另一个拷贝。

			list comprehension
			   [ <expr1> for k in L if <expr2> ]

			2、dictionary： 字典（即C++标准库的map）
			dict = {'ob1':'computer', 'ob2':'mouse', 'ob3':'printer'}
			每一个元素是pair，包含key、value两部分。key是Integer或string类型，value 是任意类型。
			键是唯一的，字典只认最后一个赋的键值。

			dictionary的方法
			D.get(key, 0)       #同dict[key]，多了个没有则返回缺省值，0。[]没有则抛异常
			D.has_key(key)      #有该键返回TRUE，否则FALSE
			D.keys()            #返回字典键的列表
			D.values()
			D.items()

			D.update(dict2)     #增加合并字典
			D.popitem()         #得到一个pair，并从字典中删除它。已空则抛异常
			D.clear()           #清空字典，同del dict
			D.copy()            #拷贝字典
			D.cmp(dict1,dict2)  #比较字典，(优先级为元素个数、键大小、键值大小)
			                    #第一个大返回1，小返回-1，一样返回0

			dictionary的复制
			dict1 = dict        #别名
			dict2=dict.copy()   #克隆，即另一个拷贝。

			3、tuple：元组（即常量数组）
			tuple = ('a', 'b', 'c', 'd', 'e')
			可以用list的 [],:操作符提取元素。就是不能直接修改元素。

			4、string：     字符串（即不能修改的字符list）
			str = "Hello My friend"
			字符串是一个整 体。如果你想直接修改字符串的某一部分，是不可能的。但我们能够读出字符串的某一部分。
			子字符串的提取
			str[:6]
			字符串包含 判断操作符：in，not in
			"He" in str
			"she" not in str

			string模块，还提供了很多方法，如
			S.find(substring, [start [,end]]) #可指范围查找子串，返回索引值，否则返回-1
			S.rfind(substring,[start [,end]]) #反向查找
			S.index(substring,[start [,end]]) #同find，只是找不到产生ValueError异常
			S.rindex(substring,[start [,end]])#同上反向查找
			S.count(substring,[start [,end]]) #返回找到子串的个数

			S.lowercase()
			S.capitalize()      #首字母大写
			S.lower()           #转小写
			S.upper()           #转大写
			S.swapcase()        #大小写互换

			S.split(str, ' ')   #将string转list，以空格切分
			S.join(list, ' ')   #将list转string，以空格连接

			处理字符串的内置函数
			len(str)                #串长度
			cmp("my friend", str)   #字符串比较。第一个大，返回1
			max('abcxyz')           #寻找字符串中最大的字符
			min('abcxyz')           #寻找字符串中最小的字符

			string的转换

			oat(str) #变成浮点数，float("1e-1")  结果为0.1
			int(str)        #变成整型，  int("12")  结果为12
			int(str,base)   #变成base进制整型数，int("11",2) 结果为2
			long(str)       #变成长整型，
			long(str,base)  #变成base进制长整型，

			字符串的格式化（注意其转义字符，大多如C语言的，略）
			str_format % (参数列表) #参数列表是以tuple的形式定义的，即不可运行中改变
			>>>print ""%s's height is %dcm" % ("My brother", 180)
			          #结果显示为 My brother's height is 180cm

			。。。。。。。。。。。。。。。。。。

			list 和 tuple 的相互转化

			tuple(ls)
			list(ls)

'''




            color.cp(h)
        if k=='lxml':
            h='''
                      #这里是解释xpth模块来处理网页信息
                        Path是门语言，不得不说它所具备的优点：
			1） 可在XML中查找信息
			2） 支持HTML的查找
			3） 通过元素和属性进行导航
			python开发使用XPath条件：
			由于XPath属于lxml库模块，所以首先要安装库lxml，
                        具体的安装过程可以查看博客，包括easy_install 和 pip 的安装方法。
                        XPath的简单调用方法：

			from lxml import etree

			selector=etree.HTML(源码)  #将源码转化为能被XPath匹配的格式
			selector.xpath(表达式)  #返回为一列表
			XPath的使用方法：
			首先讲一下XPath的基本语法知识：
			四种标签的使用方法
			1) // 双斜杠 定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表的形式返回。
			2) / 单斜杠 寻找当前标签路径的下一层路径标签或者对当前路标签内容进行操作
			3) /text() 获取当前路径下的文本内容
			4) /@xxxx 提取当前路径下标签的属性值
			5) | 可选符 使用|可选取若干个路径 如//p | //div 即在当前路径下选取所有符合条件的p标签和div标签。
			6) . 点 用来选取当前节点
			7) .. 双点 选取当前节点的父节点
			另外还有starts-with(@属性名称,属性字符相同部分)，string(.)两种重要的特殊方法后面将重点讲。
			利用实例讲解XPath的使用：
			from lxml import etree
			html="""
			    <!DOCTYPE html><html><headlang="en"><title>测试</title><metahttp-equiv="Content-Type"content="text/html; charset=utf-8" /></head><body><divid="content"><ulid="ul"><li>NO.1</li><li>NO.2</li><li>NO.3</li></ul><ulid="ul2"><li>one</li><li>two</li></ul></div><divid="url"><ahref="http:www.58.com"title="58">58</a><ahref="http:www.csdn.net"title="CSDN">CSDN</a></div></body></html>
			"""
			selector=etree.HTML(html)
			c//div[@id="content"]/ul[@id="ul"]/li/text()') #这里使用id属性来定位哪个div和ul被匹配 使用text()获取文本内容
			for i in content:
			    print i
			#输出为
			NO.1
			NO.2
			NO.3

			con=selector.xpath('//a/@href') #这里使用//从全文中定位符合条件的a标签，使用“@标签属性”获取a便签的href属性值
			for each in con:
			    print each
			#输出结果为：
			http:www.58.com
			http:www.csdn.net

			con=selector.xpath('/html/body/div/a/@title') #使用绝对路径定位a标签的title
			con=selector.xpath('//a/@title') #使用相对路径定位 两者效果是一样的
			print len(con)
			print con[0]con[1]

			#输出结果为：
			2
			58 CSDN
			介绍XPath的特殊用法：
			1) starts-with 解决标签属性值以相同字符串开头的情况
			举例说明
			from lxml import etree
			html="""
			    <body>
			        <div>aa</div>
			        <div>ab</div>
			        <div>ac</div>
			    </body>
			    """
			selector=etree.HTML(html)
			c>'//div[starts-with(@id,"a")]/text()') #这里使用starts-with方法提取div的id标签属性值开头为a的div标签for each in content:
			    print each
			#输出结果为：
			aa
			ab
			ac
			2） string(.) 标签套标签
			html="""
			    <div>
			    left
			        <span>
			        right
			            <ul>
			            up
			                <li>down</li>
			            </ul>
			        east
			        </span>
			        west
			    </div>
			"""#下面是没有用string方法的输出
			sel=etree.HTML(html)
			con=sel.xpath('//div[@id="a"]/text()')
			for i in con:
			    print i   #输出内容为left westdata=sel.xpath('//div[@id="a"]')[0]
			info=data.xpath('string(.)')
			c>'\n','').replace(' ','')
			for i in content:
			    print i #输出为 全部内容
		'''
            color.cp(h)
        if k=='xpath.exp':
            h='''
			    实成功模块（杨明）：
			       import urllib2,urllib
			       from lxml import etree #这个地方是导入xpath解析模块
			       url='http://www.weather.com.cn/weather1d/101020100.shtm #dingzhi_first '

			       #我提取的是中国天气网上上海天气的栏目,上面那个#是url里面的
			       re= urllib2.urlopen('http://www.weather.com.cn/weather1d/101020100.shtml#dingzhi_first').read()
			       #这里提取出来的是html页面
			       yang=etree.HTML(re)#这一步开始将html网页进行结构化处理
			       #下面开始进行各种各样的提取
			       con=yang.xpath('//a/@href') #这里使用//从全文中定位符合条件的a标签，使用“@标签属性”获取a便签的href属性值
			       for i in con:
			           print i

                               #下面开始解说常见的各个xpath
                               con=yang.xpath('//div/input/@value')
                               #这里使用//从全文中定位符合条件的input标签，然后抽取除value值
        		       con=yang.xpath('//a/@href')
                                #这里使用//从全文中定位符合条件的a标签，使用“@标签属性”获取a便签的href属性值
'''
            color.cp(h)
        if k=='read':

            h='''

                     #这里将展示如何一行行读取文件爱
                      for line in open('/root/exp'):
                          print line
'''
            color.cp(h)
        if k=='urllib':
            print'''
                       #注意2与3的不同诶
                       #这个模块的主要作用是从网页中去取数据
                       #在python2 中叫urllib2.urlopen()


'''
            color.cp(h)
        if k=='datastruc':
            h='''

                       字典     values = {"username":"1016903103@qq.com","password":"XXXX"}

                               #以下是常见的赋值模式
                                values = {}

                                values['username'] = "1016903103@qq.com"
                                values['password'] = "XXXX"
                       列表    [1,2,3,'a','string']


                       元组

'''
            color.cp(h)

        if k=='pachong':
            h= '''
                      1.下面是爬取一个网页最简单的方法
                      #这里即将爱展示我自已做的爬虫系统
                      import urllib2#这是标准库自带的，不需要安装
                      print urllib2.urlopen('http://www.baidu.com').read()

                      2.分析爬网页的方法
                      那么我们来分析这两行代码，第一行


                       response = urllib2.urlopen("http://www.baidu.com")
                       首先我们调用的是urllib2库里面的urlopen方法，传入一个URL
                       ，这个网址是百度首页，协议是HTTP协议，当然你也可以把HTTP
                       换做FTP,FILE,HTTPS 等等，只是代表了一种访问控制协议，urlopen一般接受三个参数，它的参数如下：


                       urlopen(url, data, timeout)

                       第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

                       第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

                       第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，
                       返回一个response对象，返回信息便保存在这里面。



                       print response.read()
                       response对象有一个read方法，可以返回获取到的网页内容。

                       如果不加read直接打印会是什么？答案如下：


                       <addinfourl at 139728495260376 whose fp = <socket._fileobject object at 0x7f1513fb3ad0>>
                       直接打印出了该对象的描述，所以记得一定要加read方法，否则它不出来内容可就不怪我咯！


                       3.构造Requset

                       其实上面的urlopen参数可以传入一个request请求,它其实就是一个Request类的实例，
                       构造时需要传入Url,Data等等的内容。比如上面的两行代码，我们可以这么改写


                      import urllib2

                      request = urllib2.Request("http://www.baidu.com")
                      response = urllib2.urlopen(request)
                      print response.read()
                      运行结果是完全一样的，只不过中间多了一个request对象，推荐大家这么写 ，
                      因为在构建请求时还需要加入好多内容，通过构建一个request，
                      服务器响应请求得到应答，这样显得逻辑上清晰明确。




                     4.POST和GET数据传送
yangming
yangming                     上面的程序演示了最基本的网页抓取，不过，现在大多数网站都是动态网页
yangming                     ，需要你动态地传递参数给它，它做出对应的响应。所以，在访问时
yangming                     ，我们需要传递数据给它。最常见的情况是什么？对了，就是登录注册的时候呀。
yangming
yangming                     把数据用户名和密码传送到一个URL，然后你得到服务器处理之后的响应
yangming                     ，这个该怎么办？下面让我来为小伙伴们揭晓吧！
yangming
yangming                     数据传送分为POST和GET两种方式，两种方式有什么区别呢？
yangming
yangming                     最重要的区别是GET方式是直接以链接形式访问，链接中包含了所有的参数，
yangming                     当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容
yangming                     。POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了，大家可以酌情选择。
yangming


                    POST方式：

                    上面我们说了data参数是干嘛的？对了，它就是用在这里的，我们传送的数据就是这个参数data，下面演示一下POST方式。

#`
#`w                    import urllib
#`w                    import urllib2
#`w
#`w                    values = {"username":"1016903103@qq.com","password":"XXXX"}
#`w                    data = urllib.urlencode(values) #注意这里是将账户与密码信息放在url里面
#`w                    url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#`w                    request = urllib2.Request(url,data)#这里是将账户与密码信息放在url里面
#`w                    response = urllib2.urlopen(request)
#`w                    print response.read()
#`
!o                    我们引入了urllib库，现在我们模拟登陆CSDN，当然上述代码可能登陆不进去，
!                    因为还要做一些设置头部header的工作，或者还有一些参数没有设置全，
!
!                    还没有提及到在此就不写上去了，在此只是说明登录的原理。
!
!                    我们需要定义一个字典，名字为values，
!                    参数我设置了username和password，下面利用urllib的urlencode方法将字典编码，命名为data，
!                    构建request时传入两个参数，url和data，运行程序，即可实现登陆，
!                    返回的便是登陆后呈现的页面内容。当然你可以自己搭建一个服务器来测试一下。
!
!                    注意上面字典的定义方式还有一种，下面的写法是等价的


@                     #  import urllib
@                     #  import urllib2
@
@                     #  values = {}
@                     #  values['username'] = "1016903103@qq.com"
@                     #  values['password'] = "XXXX"
@		     #               data = urllib.urlencode(values)
@
@                     #  url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
@                     #  request = urllib2.Request(url,data)
@                     #  response = urllib2.urlopen(request)
@                     #  print response.read()
@                     #  以上方法便实现了POST方式的传送
@
@                     #  GET方式：
@                     #  至于GET方式我们可以直接把参数写到网址上面，直接构建一个带参数的URL出来即可。


                    import urllib
                    import urllib2

#                  #values={}
yangming                    #values['username'] = "1016903103@qq.com"
       @             #values['password']="XXXX"
       @             #data = urllib.urlencode(values)
       @             #url = "http://passport.csdn.net/account/login"
       @             #geturl = url + "?"+data
       @             #request = urllib2.Request(geturl)
       @             #response = urllib2.urlopen(request)
       @             #print response.read()

       @             #你可以print geturl，打印输出一下url，发现其实就是原来的url加？然后加编码后的参数


       @             #http://passport.csdn.net/account/login?username=1016903103%40qq.com&password=XXXX

       @             #和我们平常GET访问方式一模一样，这样就实现了数据的GET方式传送。
       @
       @             实验：模拟登录qq邮箱，时间2016年3月17日
#
                     values={}

!0                    values['username']='756260386'
!                     values['password']='15099667237'
!
!                     data=urllib.urlencode(values)
!
!                     url='https://mail.qq.com/'
!
!                     geturl=url+'?'+data
!
!                     request=urllib2.Request(geturl)
!
!                     response=urllib2.urlopen(request)
!
!                     print response.read()
!
!

'''
            color.cp(h)
        if k=='write':
            h= '''
                     这里主要是介绍文件的写入
                     #简易写入模式
                     模式1：用追加模式写入


                     f=open('/root/exp','a')
                     #这里要以追加模式才不会清除之前的资料
                     f.write('yang11111111\ n')

                     f.close()
                     #用\ n这种模式来保证换行

                     #整数的换行写入
                      for i in range(5):
                          f.write(str(i)+'\ n')


'''
            color.cp(h)
	if k=='for':
	    h='''
                这里展示for循环的基本格式
		for k in range(5):

			print 'i love you'		'''
            color.cp(h)

	if k=='author':
            h= '''


# 此处的目的是在与直接在交互屏幕上显示对我们友好的帮助信息
#2016年3月6日10:23:36
#作者：杨明
#版本：0.0（nt）
#邮箱：756260386@qq.com    yang756260386@gmail.com
#项目地址：
#使用方法：nt中 将此模块文件放在python的目录下。然后在python解释器环境下使用import sheet，假如要获取for 的帮助信息，键入sheet.show('for')

#保护版权，f/从你我做起

#屏幕截图参见我的github地址:https://github.com/oxfordyang2016
'''
            color.cp(h)

	if k=='class':
            h= '''
		       这里是类最简单的基本格式：
		       class a( object):#这里是不继承任何东西
                           def __init__(self, name, score):#这里是在设计类的时候，就绑定类的一些属性的办法
                               self.name = name
                               self.score = score
                           def c(self):#这里是在定义基本的方法,默认情况下第一个参数必须是self
                               print‘ i love python’
                       t=a('yangming') #这里是在进行实例化
		       t.c()#这里实在使用实例化方法
'''
            color.cp(h)
	if k=='print':
            h= """
                     常见的输入格式 
                           s=5
                           1.print 'yangming'+str(a)+'i love you'
                           2.windows 解决输出办法 print uniode('年后一定好好学习','gbk')


                     1. 这里的这种格式print ''' ''' 专制各种符号，各种换行，各种奇怪的格式
                     2.这里是打印多个表达式 用逗号隔开就行， print "Name : ", self.name,  " Salary: ", self.salary
                     3.在同一行打印：print 'hallo',
                                     print 'world'
                                    注：这里将打印出hello，world
                     4.代替性的打印格式
                         A. print "Total Employee %d" % Employee.empCount             


                     使用一个字符串作为模板。模板中有格式符，这些格式符为真实值预留位置，并说明真实数值应该呈现的格式。
                    Python用一个tuple将多个值传递给模板，每个值对应一个格式符。

                    比如下面的例子：

                    print("I'm %s. I'm %d year old" % ('Vamei', 99))
                    上面的例子中，
                    
                    "I'm %s. I'm %d year old" 为我们的模板。%s为第一个格式符，表示一个字符串。
                    %d为第二个格式符，表示一个整数。('Vamei', 99)的两个元素'Vamei'和99为替换%s和%d的真实值。 
                    在模板和tuple之间，有一个%号分隔，它代表了格式化操作。
                    
                    整个"I'm %s. I'm %d year old" % ('Vamei', 99) 实际上构成一个字符串表达式。
                    我们可以像一个正常的字符串那样，将它赋值给某个变量。比如:
                    
                    a = "I'm %s. I'm %d year old" % ('Vamei', 99)
                    print(a)
                     
                    
                    我们还可以用词典来传递真实值。如下：
                    
                    print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})
                    可以看到，我们对两个格式符进行了命名。命名使用()括起来。每个命名对应词典的一个key。
                    
                     
                    
                    格式符
                    
                    格式符为真实值预留位置，并控制显示的格式。
                    格式符可以包含有一个类型码，用以控制显示的类型，如下:
                    
                    %s    字符串 (采用str()的显示)
                    
                    %r    字符串 (采用repr()的显示)
                    
                    %c    单个字符
                    
                    %b    二进制整数
                    
                    %d    十进制整数
                    
                    %i    十进制整数
                    
                    %o    八进制整数
                    
                    %x    十六进制整数
                    
                    %e    指数 (基底写为e)
                    
                    %E    指数 (基底写为E)
                    
                    %f    浮点数
                    
                    %F    浮点数，与上相同
                    
                    %g    指数(e)指数或浮点数 (根据显示长度)
                    
                    %G    指数(E)或浮点数 (根据显示长度)
                    
                     
                    
                    %%    字符"%"
                    
                     
                    
                    可以用如下的方式，对格式进行进一步的控制：
                    
                    %[(name)][flags][width].[precision]typecode
                    
                    (name)为命名
                    
                    flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，
                    表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。

                    
                    width表示显示宽度
                    
                    precision表示小数点后精度
                    
                     
                    
                    比如：
                    
                    print("%+10x" % 10)
                    print("%04d" % 5)
                    print("%6.3f" % 2.3)
                     
                    
                    上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。比如：
                    
                    print("%.*f" % (4, 1.2))
                    Python实际上用4来替换*。所以实际的模板为"%.4f"。
                    
                     
                    
                    总结
                    
                    Python中内置的%操作符可用于格式化字符串操作，控制字符串的呈现格式。
                    Python中还有其他的格式化字符串的方式，但%操作符的使用是最方便的。






                         
                   



"""
            color.cp(h)
        if k=='import':
            h= '''
                      #注意urllib 在2与3版本中的不同，导致了import urllib 与 import urllib.request，见了请不要见怪
                      #import sys,os,sheet 这里的意思是一次导入多个模块
                      #from A import B     解释为从A模块里面导入B函数或B类
                      #from A import *     表示导入模块的所有功能
                      #import C            表示导入C模块
                      #import sheet as c  使用c.show('all')这样的效果和sheet.show('all')是一样的
                      #from sheet import show as b 这样就可以使b('all'),就可以展示出所有的东西，源代码应该会将公共变量提取出来
 

                      #下面进行特别说明：
                      #1. 假如我在sheet.PY这个文件当中有import os 这句话，当我import sheet 时候，直接os.listdir('/root')
                      #  是不会有任何作用的,但是使用sheet.os.listdir('/root')是会有作用的

                      下面是更详细的笔记
                        python语法31[module/package+import]

                      

                       一 module
               通常模块为一个文件，直接使用import来导入就好了。
               可以作为module的文件类型有".py"、".pyo"、".pyc"、".pyd"、".so"、".dll"。
               二 package
               通常包总是一个目录，可以使用import导入包，或者from + import来导入包中的部分模块。
               包目录下为首的一个文件便是 __init__.py。
               然后是一些模块文件和子目录，假如子目录中也有 __init__.py 那么它就是这个包的子包了。
               
               参考：http://wiki.woodpecker.org.cn/moin/PythonEssentialRef8
               
               一模块
               你可以使用import语句将一个源代码文件作为模块导入.例如:
               # file : spam.py
               a = 37                    # 一个变量
               def foo:                  # 一个函数
                   print "I'm foo"
               class bar:                # 一个类
                   def grok(self):
                       print "I'm bar.grok"
               b = bar()                 # 创建一个实例
               使用import spam 语句就可以将这个文件作为模块导入。系统在导入模块时，要做以下三件事：
               1.为源代码文件中定义的对象创建一个名字空间，通过这个名字空间可以访问到模块中定义的函数及变量。
               2.在新创建的名字空间里执行源代码文件.
               3.创建一个名为源代码文件的对象，该对象引用模块的名字空间，这样就可以通过这个对象访问模块中的函数及变量，如：
                import spam           # 导入并运行模块 spam
                print spam.a          # 访问模块 spam 的属性
                spam.foo()
                c = spam.bar()
 ...
用逗号分割模块名称就可以同时导入多个模块:
import socket, os, regex模块导入时可以使用 as 关键字来改变模块的引用对象名字:
import os as system
import socket as net, thread as threads
system.chdir("..")
net.gethostname()

使用from语句可以将模块中的对象直接导入到当前的名字空间.
 from语句不创建一个到模块名字空间的引用对象，而是把被导入模块的一个或多个对象直接放入当前的名字空间:
from socket import gethostname
                               # 将gethostname放如当前名字空间
print gethostname()            # 直接调用
socket.gethostname()           # 引发异常NameError: socket
from语句支持逗号分割的对象，也可以使用星号(*)代表模块中除下划线开头的所有对象:
from socket import gethostname, socket
from socket import *   # 载入所有对象到当前名字空间

不过，如果一个模块如果定义有列表__all__，则from module import * 语句只能导入__all__列表中存在的对象。
# module: foo.py
__all__ = [ 'bar', 'spam' ]     # 定义使用 `*` 可以导入的对象

另外, as 也可以和 from 联合使用:
from socket import gethostname as hostname
h = hostname()

import 语句可以在程序的任何位置使用，你可以在程序中多次导入同一个模块，
但模块中的代码*仅仅*在该模块被首次导入时执行。
后面的import语句只是简单的创建一个到模块名字空间的引用而已。
sys.modules字典中保存着所有被导入模块的模块名到模块对象的映射。
这个字典用来决定是否需要使用import语句来导入一个模块的最新拷贝.
from module import * 语句只能用于一个模块的最顶层.*特别注意*：
由于存在作用域冲突，不允许在函数中使用from 语句。
每个模块都拥有 __name__ 属性，它是一个内容为模块名字的字符串。
最顶层的模块名称是 __main__ .命令行或是交互模式下程序都运行在__main__ 模块内部. 
利用__name__属性，我们可以让同一个程序在不同的场合（单独执行或被导入)具有不同的行为，象下面这样做：
# 检查是单独执行还是被导入
if __name__ == '__main__':
      # Yes
      statements
else:
      # No (可能被作为模块导入)
      statements

模块搜索路径
导入模块时,解释器会搜索sys.path列表,这个列表中保存着一系列目录。一个典型的sys.path 列表的值：
Linux:
['', '/usr/local/lib/python2.0',
     '/usr/local/lib/python2.0/plat-sunos5',
     '/usr/local/lib/python2.0/lib-tk',
     '/usr/local/lib/python2.0/lib-dynload',
     '/usr/local/lib/python2.0/site-packages']
Windows:
['', 'C:\\WINDOWS\\system32\\python24.zip', 'C:\\Documents and Settings\\weizhong', 'C:\\Python24\\DLLs', 'C:\\Python24\\lib', 'C:\\Python24\\lib\\plat-win', 'C:\\Python24\\lib\\lib-tk', 'C:\\Python24\\Lib\\site-packages\\pythonwin', 'C:\\Python24', 'C:\\Python24\\lib\\site-packages', 'C:\\Python24\\lib\\site-packages\\win32', 'C:\\Python24\\lib\\site-packages\\win32\\lib', 'C:\\Python24\\lib\\site-packages\\wx-2.6-msw-unicode']

空字符串 代表当前目录. 要加入新的搜索路径,只需要将这个路径加入到这个列表.

模块导入和汇编
到现在为止，本章介绍的模块都是包含Python源代码的文本文件. 不过模块不限于此，可以被 import 语句导入的模块共有以下四类:
•使用Python写的程序( .py文件)
•C或C++扩展(已编译为共享库或DLL文件)
•包(包含多个模块)
•内建模块(使用C编写并已链接到Python解释器内)
当查询模块 foo 时,解释器按照 sys.path 列表中目录顺序来查找以下文件(目录也是文件的一种):
1.定义为一个包的目录 foo
2.foo.so, foomodule.so, foomodule.sl,或 foomodule.dll (已编译扩展)
3.foo.pyo (只在使用 -O 或 -OO 选项时)
4.foo.pyc
5.foo.py

对于.py文件,当一个模块第一次被导入时,它就被汇编为字节代码,并将字节码写入一个同名的 .pyc文件.后来的导入操作会直接读取.pyc文件而不是.py文件.(除非.py文件的修改日期更新,这种情况会重新生成.pyc文件) 在解释器使用 -O 选项时，扩展名为.pyo的同名文件被使用. pyo文件的内容虽去掉行号,断言,及其他调试信息的字节码，体积更小,运行速度更快.如果使用-OO选项代替-O,则文档字符串也会在创建.pyo文件时也被忽略.
如果在sys.path提供的所有路径均查找失败,解释器会继续在内建模块中寻找,如果再次失败，则引发 ImportError 异常.
.pyc和.pyo文件的汇编,当且仅当import 语句执行时进行.
当 import 语句搜索文件时,文件名是大小写敏感的。即使在文件系统大小写不敏感的系统上也是如此(Windows等). 这样, import foo 只会导入文件foo.py而不会是FOO.PY.

重新导入模块
如果更新了一个已经用import语句导入的模块，内建函数reload()可以重新导入并运行更新后的模块代码.它需要一个模块对象做为参数.例如:
import foo
... some code ...
reload(foo)          # 重新导入 foo
在reload()运行之后的针对模块的操作都会使用新导入代码，不过reload()并不会更新使用旧模块创建的对象，因此有可能出现新旧版本对象共存的情况。 *注意* 使用C或C++编译的模块不能通过 reload() 函数来重新导入。记住一个原则，除非是在调试和开发过程中，否则不要使用reload()函数.

                                                     二.包

                                                     多个关系密切的模块应该组织成一个包，以便于维护和使用。
                                                     这项技术能有效避免名字空间冲突。
                                                     创建一个名字为包名字的文件夹并在该文件夹下创建一个__init__.py 文件就定义了一个包。
                                                     你可以根据需要在该文件夹下存放资源文件、已编译扩展及子包。举例来说，一个包可能有以下结构:
                                                     Graphics/
                                                           __init__.py
                                                           Primitive/
                                                              __init__.py
                                                              lines.py
                                                              fill.py
                                                              text.py
                                                              ...
                                                           Graph2d/
                                                              __init__.py
                                                              plot2d.py
                                                              ...
                                                           Graph3d/
                                                              __init__.py
                                                              plot3d.py
                                                              ...
                                                           Formats/
                                                              __init__.py
                                                              gif.py
                                                              png.py
                                                              tiff.py
                                                              jpeg.py

                                   import语句使用以下几种方式导入包中的模块:
                                   * import Graphics.Primitive.fill 导入模块Graphics.Primitive.fill,
                                      只能以全名访问模块属性,例如 Graphics.Primitive.fill.floodfill(img,x,y,color).
                                   * from Graphics.Primitive import fill 导入模块fill ,
                                      只能以 fill.属性名这种方式访问模块属性,例如 fill.floodfill(img,x,y,color).
                                   * from Graphics.Primitive.fill import floodfill 导入模块fill ,
                                          并将函数floodfill放入当前名称空间,直接访问被导入的属性，例如 floodfill(img,x,y,color).

                                   无论一个包的哪个部分被导入, 在文件__init__.py中的代码都会运行.
                                   这个文件的内容允许为空,不过通常情况下它用来存放包的初始化代码。
                                   导入过程遇到的所有 __init__.py文件都被运行.
                                   因此 import Graphics.Primitive.fill 语句会顺序运行 Graphics 和 Primitive 文件夹下的__init__.py文件.

                                   下边这个语句具有歧义:
                                   from Graphics.Primitive import *
                                   这个语句的原意图是想将Graphics.Primitive包下的所有模块导入到当前的名称空间.
                                   然而,由于不同平台间文件名规则不同(比如大小写敏感问题), Python不能正确判定哪些模块
                                   要被导入.这个语句只会顺序运行 Graphics 和 Primitive 文件夹下的__init__.py文件.
                                   要解决这个问题，应该在Primitive文件夹下面的__init__.py中定义一个名字all的列表，例如:
                                                 # Graphics/Primitive/__init__.py
                                                 __all__ = ["lines","text","fill",...]
                                                  这样,上边的语句就可以导入列表中所有模块.

                                   下面这个语句只会执行Graphics目录下的__init__.py文件，而不会导入任何模块:
                                   import Graphics
                                   Graphics.Primitive.fill.floodfill(img,x,y,color)  # 失败!


       不过既然 import Graphics 语句会运行 Graphics 目录下的 __init__..py文件,我们就可以采取下面的手段来解决这个问题：
       # Graphics/__init__.py
       import Primitive, Graph2d, Graph3d
       # Graphics/Primitive/__init__.py
       import lines, fill, text, ...
       这样import Graphics语句就可以导入所有的子模块(只能用全名来访问这些模块的属性).

        三 sys.path 和sys.modules
       sys.path包含了module的查找路径；
       sys.modules包含了当前所load的所有的modules的dict（其中包含了builtin的modules）；

完！

'''
            color.cp(h)
        if k=='sys':
            h= '''
                    python sys模块详解!
2011年06月28日
　　sys.argv           命令行参数List，第一个元素是程序本身路径
　　sys.modules.keys() 返回所有已经导入的模块列表
　　sys.exc_info()     获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
　　sys.exit(n)        退出程序，正常退出时exit(0)
　　sys.hexversion     获取Python解释程序的版本值，16进制格式如：0x020403F0
　　sys.version        获取Python解释程序的版本信息
　　sys.maxint         最大的Int值
　　sys.maxunicode     最大的Unicode值
　　sys.modules        返回系统导入的模块字段，key是模块名，value是模块
　　sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
　　sys.platform       返回操作系统平台名称
　　sys.stdout         标准输出
　　sys.stdin          标准输入
　　sys.stderr         错误输出
　　sys.exc_clear()    用来清除当前线程所出现的当前的或最近的错误信息
　　sys.exec_prefix    返回平台独立的python文件安装的位置
　　sys.byteorder      本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
　　sys.copyright      记录python版权相关的东西
　　sys.api_version    解释器的C的API版本
　　sys.version_info
　　>>> sys.version_info
　　(2, 4, 3, 'final', 0) 'final'表示最终,也有'candidate'表示候选，表示版本级别，是否有后继的发行
　　sys.displayhook(value)      如果value非空，这个函数会把他输出到sys.stdout，并且将他保存进__builtin__._.指在python的交互式解释器里，'_'代表上次你输入得到的结果，hook是钩子的意思，将上次的结果钩过来
　　sys.getdefaultencoding()    返回当前你所用的默认的字符编码格式
　　sys.getfilesystemencoding() 返回将Unicode文件名转换成系统文件名的编码的名字
　　sys.setdefaultencoding(name)用来设置当前默认的字符编码，如果name和任何一个可用的编码都不匹配，抛出LookupError，这个函数只会被site模块的sitecustomize使用，一旦别site模块使用了，他会从sys模块移除
　　sys.builtin_module_names    Python解释器导入的模块列表
　　sys.executable              Python解释程序路径
　　sys.getwindowsversion()     获取Windows的版本
　　sys.stdin.readline()        从标准输入读一行，sys.stdout.write("a") 屏幕输出a

'''
            color.cp(h)
        if k=='try':
            h= '''
                     这里主要是介绍try系列的用法：
                     s='hello'
                     try:
                         print '这一句将在没有任何异常的情况下被打印出来'
                     except indexError(这里指出错误类型)：
                         print '当try部分出现错误的时候即将回跳到相应错误类型下面语句执行'
                     except  c:
                         def k()
                     #当然except 后面可以为空，表示捕获任何类型的异常
                     do what (这一个动作无论如何都会执行)

'''
            color.cp(h)

        if k=='urljoin':
            h='''


j= urljoin('https://www.douban.com/group/shanghaizufang/','discussion?start='+str(h))

#拼接整体思路展示
 for i in range(45):
             h=i
             j= urljoin('http://jobzpgl.swufe.edu.cn/','RCPT/Pub01/xyzp/CompanyDemandList.aspx?page='+str(h))
             k=trickvisit.spider(j,'//td/a[@title]/text()','/root/info/sp1')


'''
            color.cp(h)


        if k=='os':
            h= '''
                  Python中OS模块的操作

                  #注意：使用路径的时候使用这种格式（'/root/exp'）




os和os.path模块
                创建文件

                创建文件：
                 1) os.mknod("test.txt") 创建空文件
                 2) open("test.txt",w)           直接打开一个文件，如果文件不存在则创建文件


                os.listdir(dirname)：列出dirname下的目录和文件


                 例：os.listdir('/root')
                 os.getcwd()：获得当前工作目录
                 os.curdir:返回当前目录（'.')
                 os.chdir(dirname):改变工作目录到dirname
                 os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
                 os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
                 os.path.exists(name):判断是否存在文件或目录name
                 os.path.getsize(name):获得文件大小，如果name是目录返回0L

                 os.path.abspath(name):获得绝对路径(注意：这里的实验没有成功)


                 os.path.normpath(path):规范path字符串形式
                 os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
                 os.path.splitext():分离文件名与扩展名
                 os.path.join(path,name):连接目录与文件名或目录
                 os.path.basename(path):返回文件名
                 os.path.dirname(path):返回文件路径
                 os.remove()函数用来删除一个文件
                 1.重命名：os.rename(old, new)        2.删除：os.remove(file)                    3.列出目录下的文件：os.listdir(path)
                 4.获取当前工作目录：os.getcwd()        5.改变工作目录：os.chdir(newdir)          6.创建多级目录：os.makedirs(r"c:\python\test")
                 7.创建单个目录：os.mkdir("test")      8.删除多个目录：os.removedirs(r"c:\python") #删除所给路径最后一个目录下所有空目录。
                 9.删除单个目录：os.rmdir("test")        10.获取文件属性：os.stat(file)          11.修改文件权限与时间戳：os.chmod(file)
                 12.执行操作系统命令：os.system("dir")  13.启动新进程：os.exec(), os.execvp()      14.在后台执行程序：osspawnv()
                 15.终止当前进程：os.exit(), os._exit()
                 16.分离文件名：os.path.split(r"c:\python\hello.py") --> ("c:\\python", "hello.py")
                 17.分离扩展名：os.path.splitext(r"c:\python\hello.py") --> ("c:\\python\\hello", ".py")
                 18.获取路径名：os.path.dirname(r"c:\python\hello.py") --> "c:\\python"
                 19.获取文件名：os.path.basename(r"r:\python\hello.py") --> "hello.py"
                 20.判断文件是否存在：os.path.exists(r"c:\python\hello.py") --> True
                 21.判断是否是绝对路径：os.path.isabs(r".\python\") --> False
                 22.判断是否是目录：os.path.isdir(r"c:\python") --> True
                 23.判断是否是文件：os.path.isfile(r"c:\python\hello.py") --> True
                 24.判断是否是链接文件：os.path.islink(r"c:\python\hello.py") --> False
                 25.获取文件大小：os.path.getsize(filename)
                 26.*******：os.ismount("c:\\") --> True
                 27.搜索目录下的所有文件：os.path.walk()

                 shutil模块对文件的操作：
                 1.复制单个文件：shultil.copy(oldfile, newfle)
                 2.复制整个目录树：shultil.copytree(r".\setup", r".\backup")
                 3.删除整个目录树：shultil.rmtree(r".\backup") '''
            color.cp(h)


