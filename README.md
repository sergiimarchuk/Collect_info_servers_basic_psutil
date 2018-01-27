#### py_qal


#### collect logs file on servers and get to monitoring server back
<pre>
[sergii@monitoringServer psutils]$ cd /home/sergii/collect_info/psutils/ && rm -rf local*; ansible-playbook -i inventory qalpy.yml; sleep 5; ./pars_log.py
</pre>
