#!/home/SergiiMarchuk/link-nfs/python-port/python27/bin/python
##!/opt/python27/bin/python
from collections import Counter
import glob
import os
import socket

hfqdn = socket.getfqdn()

#Current directory path
_pwd_ = os.getcwd()

#Read all files with .ext in current directory
a = glob.glob("*")

# function do parsing log file for Memory.
def pars_log_mem(log_name):
        html_mem = ""
        """ Parsing Memory log """
        print "                                                                                                                                         _ _ _  _ _ _  _ _ _  MEMORY STATUS."
        with open(_pwd_ +  "/" + el, "rb") as log_f:
                for line in log_f:
                        if ".:SECTION MEMORY:." in line:
                                print line.split(" ")
                                date_ = line.split(" ")[0]
                                time_ = (line.split(" ")[1]).split(".")[0]
                                fqdn_ = line.split(" ")[2]
                                hn_ = str(line.split(" ")[4]).replace(":","")
                                memory_col_ = str(line.split(" ")[6]).replace(":.","")
                                status_ = line.split(" ")[7]
                                status_value_ = line.split(" ")[8]
                                print date_
                                print time_
                                print fqdn_
                                print hn_
                                print memory_col_
                                print status_
                                print status_value_
                                html_mem = html_mem + "<tr><td>" + date_ + " " + time_  + "</td><td>" + hn_ + "</td><td>" + memory_col_ + "</td>""<td>" + status_value_ + "</td></tr>\n"
                                print date_ + " " + time_ +  " " + fqdn_ + " " + hn_.replace(":","") + " " + memory_col_.replace(":.","") + " " + status_ + " " +  status_value_
        return(html_mem)
# function do parsing log file for SWAP.
def pars_log_swap(log_name):
        html_swap = ""
        """ Parsing SWAP log """
        print "                                                                                                                                         _ _ _  _ _ _  _ _ _   SWAP STATUS"
        with open(_pwd_ +  "/" + el, "rb") as log_f:
                for line in log_f:
                        if ".:SECTION SWAP:." in line:
                                print line.split(" ")
                                date_ = line.split(" ")[0]
                                time_ = (line.split(" ")[1]).split(".")[0]
                                fqdn_ = line.split(" ")[2]
                                hn_ = str(line.split(" ")[4]).replace(":","")
                                swap_ = str(line.split(" ")[6]).replace(":.","")
                                status_ = line.split(" ")[7]
                                status_value_ = line.split(" ")[8]
                                #print "    ###   Run Function Test SWAP Pars"
                                print date_
                                print time_
                                print fqdn_
                                print hn_
                                print swap_
                                print status_
                                print status_value_
                                html_swap = html_swap + "<tr><td>" + date_ + " " + time_ + "</td><td>" + hn_ + "</td><td>" + swap_ + "</td>""<td>" + status_value_ + "</td></tr>\n"
                                #print date_ + " " + time_ +  " " + fqdn_ + " " + hn_.replace(":","") + " " + memory_col_.replace(":.","") + " " + status_ + " " +  status_value_
        return(html_swap)


def pars_log_cpu(log_name):
        html_cpu = ""
        """ Parsing CPU log """
        print "                                                                                                                                         _ _ _  _ _ _  _ _ _    CPU STATUS"
        with open(_pwd_ +  "/" + el, "rb") as log_f:
                c = 0
                for line in log_f:
                        if ".:SECTION CPU:." in line:
                                #print line.split(" ")
                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]

                                core_arr= (str((str(str((line).split(" ")[7:])).replace("[","").replace("]","").replace("'","").replace(",","").replace("\\n","")).split("::")).replace("[","").replace("]","").replace(" ","").replace("''","").replace(",","")).split("''")
                                #print (core_arr)
                                for yi in (core_arr):
                                        c = c + 1
                                        #var = "var1" + str(c)
                                        var  =  (yi).replace("'","").split(".")
                                        var1 = (yi).replace("'","").split(".")[0]
                                        var2 = str((yi).replace("'","").split(".")[1]).replace("Status","")
                                        html_cpu = html_cpu + "<tr><td>" + date_ + " " + time_ + "</td><td>" + hn_ + "</td><td>" + "CPU:" + var1  + "</td>""<td>" + var2 + "</td></tr>\n"
                                        #print str(date_) + " " + str(time_) + " " + str(fqdn_) + " " +  str(hn_)  + " " + var
        return(html_cpu)
###
def pars_log_disk(log_name):
        html_disk = ""
        """ Parsing Partition log """
        print "                                 i                                                                                               _ _ _  _ _ _  _ _ _     Partition STATUS"
        with open(_pwd_ +  "/" + el, "rb") as log_f:
                c = 0
                for line in log_f:
                        if ".:SECTION DISKS:." in line:
                                #print line.split(" ")
                                part = str(line.split(" ")[7:]).split(",', ")

                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1].split(".")[0]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]

                                #print part
                                for p in part:
                                        #print (p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()
                                        status_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[0]).replace(",","")
                                        status_val_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[1]).replace(",","")
                                        part_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[2]).replace(",","")
                                        part_name_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[3]).replace(",","")
                                        print status_
                                        print status_val_
                                        print part_
                                        print part_name_
                                       inf_mess_= status_ + " " + status_val_ + " " + part_ + " " + part_name_
                                        inf_mess_item_0 = inf_mess_.split(". ")[0].split(" ")[1]        #               #
                                        inf_mess_item_1 = inf_mess_.split(". ")[1]      #
                                        inf_mess_item_2 = inf_mess_.split(". ")[2]      #               # Partition name
                                        html_disk = html_disk + "<tr><td>" + date_ + " " + time_ + "</td><td>" + hn_ + "</td><td>" + "Part.: "  + inf_mess_item_2 + "</td>""<td>" + inf_mess_item_0 + "</td></tr>\n"
                                        print str(date_) + " " + str(time_) + " " + str(fqdn_) + " " + str(hn_) + " " + inf_mess_

        return(html_disk)
###
#read files in current directory from where we run this script and as result we got list all files in this directory, tring to find file which containts file name with suf' or pref' 'local' and after all file we do transfer to 'function pars_log(file_name)'
def  send_html_report(html):
            # html = "<h3>Test header</h3>"
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            import smtplib

            #me = hfqdn
            me = 'root@collect-srv.local'
            #you = emails
            you = ['sergii.marchuk@.com']

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Possible issue on server " + hfqdn
            msg['From'] = me
            msg['To'] = ','.join(you)

            part2 = MIMEText(html, 'html')

            msg.attach(part2)

            s = smtplib.SMTP('smtp.Server')
            s.sendmail(me, you, msg.as_string())
            s.quit()
            print(html)

html = ""
for el in a:
        if "local" in el:
            print ""
            print "... ... ...                                                                   ... NAME FILE LOG ... NAME FILE LOG ... File name :         ",el
            l_n = "Log file for server:  " + str(el).replace("local","Log file: ").split("_")[1]

            html = html + "<h3>" + l_n + "2</h3>\n"
            html = html + "<table border=1 >\n"
            html = html + "<tr><td>Date </td><td>Server Name</td><td>Target status</td><td>Values Status</td></tr>\n"
            html = html + pars_log_mem(el)
            html = html + pars_log_swap(el)
            html = html + pars_log_cpu(el)

            html = html + pars_log_disk(el)

            #pars_log_swap(el)
            #pars_log_cpu(el)
            #pars_log_disk(el)
            html = html + "</table>\n"
send_html_report(html);
# function do parsing log file for Memory.
def pars_log():
        """ Parsing Partition log """
        #print "...............................Partition STATUS"
        with open("localhost-5656", "rb") as log_f:
                c = 0
                for line in log_f:
                        if ".:SECTION DISKS:." in line:
                                #print line.split(" ")
                                part = str(line.split(" ")[7:]).split(",', ")

                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]

                                #print part
                                for p in part:
                                        #print (p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()
                                        status_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[0]).replace(",","")
                                        status_val_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[1]).replace(",","")
                                        part_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[2]).replace(",","")
                                        part_name_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[3]).replace(",","")
                                        print status_
                                        print status_val_
                                        print part_
                                        print part_name_
                                        inf_mess_= status_ + " " + status_val_ + " " + part_ + " " + part_name_
                                        print str(date_) + " " + str(time_) + " " + str(fqdn_) + " " + str(hn_) + " " + inf_mess_

#pars_log()

