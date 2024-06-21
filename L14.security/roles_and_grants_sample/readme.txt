open two terminal windows in linux

in the first one - run ./_create.sh;
   this will create and run the docker-container with postgresql and all *.sql files from the folder

in the second one run ./_psql.sh
   this will open the container's psql shell

and now you can execute any sql statements or metacommands
or execute .sql files; to execute .sql file use the following command:
   \i /repo/some_file_name.sql

=============================================

Other psql commands that can be usefull for you:

Listing databases:    \l
Switching Databases:  \c database
Listing Tables:       \dt
List of Relations:    \d
Quit:                 \q
Execute query:        \i /repo/sample_query_1.sql
List of roles:        \du
Show current user:    :whoami   (this is a short alias to get current user defined in .psqlrc)
