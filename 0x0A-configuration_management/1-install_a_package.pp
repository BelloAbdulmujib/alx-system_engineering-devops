#This will install flask and werkzeug with their versions
package{'flaskg':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package{'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
