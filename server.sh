#！/usr/bin envy bash



netip = '10.0.111'
for hostip in $(seq 2 254)
do
 { 
  ping -c1 ${netip}.${hotip} &> /dev/null
  if [ $? -eq 0 ];then
     echo '{${netip}.${hostip}:online}' >> online.json
  else
     echo '{${netip}.${hostip}:online}' >> offline.json
  fi


 }&

done
wait
echo 'finish'
