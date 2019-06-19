#!/usr/bin/env bash
#
# author: bavdu
# email: bavduer@163.com
# date: 2019/06/16
# usage: Detect host survivability.
netip='192.168.161'
for hostip in $(seq 2 254)
do
  {
    ping -c1 ${netip}.${hostip} &>/dev/null
    if [ $? -eq 0 ];then
      echo '{${netip}.${hostip}:online}' >>OnlineIP.json
    else
      echo '{${netip}.${hostip}:offline}' >>OfflineIP.json
    fi
  }&
done
wait
echo 'Complete OK.'
[root@git ServerAPI]# git add ServerOnline.sh
[root@git ServerAPI]# git commit -m 'Add ServerOnline.sh shell scripts'
[master 2c5e2a2] Add ServerOnline.sh shell scripts
 1 file changed, 22 insertions(+)
 create mode 100644 ServerOnline.sh
