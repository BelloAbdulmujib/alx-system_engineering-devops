#This will install flask with a version of 2.1.0
package{'flaskg':
  ensure   => '2.1.0',
  provider => 'pip3',
}
#This will install werkzeug with a version of 2.1.1
package{'Werkzeug':
  ensure   => '2.1.1',
  providwr => 'pip3',
}
