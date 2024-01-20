# Installs flask from pip3 using puppet

package{'python3-pip':
  ensure => installed,
}

package{'flask':
  ensure   => '2.1.0',
  require  => Package['python3-pip'],
  provider =>'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  require  => Package['python3-pip'],
  provider => 'pip3',
}
