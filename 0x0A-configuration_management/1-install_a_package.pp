# Installs flask from pip3 using puppet

package{'python3':
  ensure=> 3.8.10,
}

package{'flask':
  ensure   => '2.1.0',
  require  => Package['pyhton3'],
  provider =>'pip3'
}

package { 'werkzeug':
  ensure   => '2.1.1',
  require  => Package['python3'],
  provider => 'pip3'
}
