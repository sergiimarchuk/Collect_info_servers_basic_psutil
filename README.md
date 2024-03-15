#### py_qal

#### Prepare Files on Remote Servers
```bash
ssh TestSrv 'mkdir /home/SergiiMarchuk/link-nfs'
rsync -ar -e ssh /home/SergiiMarchuk/link-nfs/ TestSrv:/home/SergiiMarchuk/link-nfs/

for i in $(cat inventory); do
  echo $i
  ssh -q $i mkdir /home/SergiiMarchuk/link-nfs
done

for i in $(cat inventory); do
  echo $i
  ssh -q $i mkdir ls -ld /home/SergiiMarchuk/link-nfs
done

for i in $(cat inventory); do
  echo $i
  rsync -ar -e ssh /home/SergiiMarchuk/link-nfs/ $i:/home/SergiiMarchuk/link-nfs/
done

[sergii@monitoringServer psutils]$ cd /home/sergii/collect_info/psutils/ && rm -rf local*; ansible-playbook -i inventory qalpy.yml; sleep 5; ./pars_log.py

