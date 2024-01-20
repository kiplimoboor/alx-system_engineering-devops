# Installs flask from pip3 using puppet

package{'python3':
  ensure => installed,
}

package{'flask':
  ensure          => '2.1.0',
  require         => Package['python3'],
  provider        =>'pip3',
  install_options => ['--break-system-packages']
}

package { 'werkzeug':
  ensure          => '2.1.1',
  require         => Package['python3'],
  provider        => 'pip3',
  install_options => ['--break-system-packages']
}
