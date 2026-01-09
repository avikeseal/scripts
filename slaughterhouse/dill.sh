#!usr/bin/env bash
 



#list packages that can be upgraded:
sudo apt list --upgradable
read -p "Press Y to upgrade and N to abort $foo?" output
if [[ $output = y ]] ; then 
      #update package lists:
      sudo apt update

      #upgrade all installed packages:
      sudo apt upgrade -y

      #remove unnecessary packages:
      sudo apt autoremove -y

      #clean up package cache:
      sudo apt clean
      
      echo " "

      echo "===SYSTEM UPDATE AND CLEANUP COMPETE==="

else
      echo " "
      echo "GOODBYE"
fi
      



 

