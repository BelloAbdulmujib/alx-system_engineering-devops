#!/usr/bin/python3
 """This script used API to get information of a user and return the TODO list progress"""

 import sys
 import requests as req

  if __name__ == "--main--":
      url = 'https://jsonplaceholder.typicode.com/todos/1'
      usr_id = req.get('users/{}'.format(sys.argv[1])).json()
      to_do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()

      completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
        print(completed)
        print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
        [print("\t {}".format(title)) for title in completed]