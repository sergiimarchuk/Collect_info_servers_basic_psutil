 ssh TestSrv 'mkdir /home/SergiiMarchuk/link-nfs'
 rsync -ar -e ssh /home/SergiiMarchuk/link-nfs/ TestSrv:/home/SergiiMarchuk/link-nfs/


for i in $(cat inventory); do echo $i; ssh -q $i mkdir /home/SergiiMarchuk/link-nfs; done
for i in $(cat inventory); do echo $i; ssh -q $i mkdir ls -ld /home/SergiiMarchuk/link-nfs; done

for i in $(cat inventory); do echo $i; rsync -ar -e ssh /home/SergiiMarchuk/link-nfs/ $i:/home/SergiiMarchuk/link-nfs/; done
