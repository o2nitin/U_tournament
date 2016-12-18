##Project: Tournament Results
The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and  the code that will use it.

#How to run
1-Install Virtualbox (https://www.virtualbox.org/wiki/Downloads)
2-Install Vagrant ( https://www.vagrantup.com/downloads.html )
3-Clone the Repository (git clone https://github.com/o2nitin/U_tournament.git)

changee the folder

```sh
$ cd U_tournament/vagrant
```
run the command
```sh
$ vagrant up
```

```sh
$ vagrant ssh
```

go to ```cd /vagrant```
go to ```cd tournament```
###Initialize the database
```psql
   vagrant=> \i tournament.sql
   vagrant=> \q
```
##Run the unit tests
```
   $ python tournament_test.py
```
