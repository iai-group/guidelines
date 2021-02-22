# Folder permissions

  - For each project create a group on gustav1 using this command `sudo groupadd group_name`
  - Then add all the users involved in that project to that group `sudo usermod -a -G group_name user_name`
  - Give group level full permission to a folder `setfacl -R -m g:group_name:rwX /data/project_folder`
  - Also make permissions default for all future folder created by everyone `setfacl -Rd -m g:group_name:rwX /data/project_folder`
