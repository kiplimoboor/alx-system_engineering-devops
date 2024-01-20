# Installs Flask version 2.1.0

package{
  'werkzeug':
  ensure          => '2.1.1',
  provider        => pip3,
  install_options => ['--break-system-packages']
}

package{
  'flask':
  ensure          =>'2.1.0',
  provider        =>pip3,
  require         => Package['werkzeug'],
  install_options => ['--break-system-packages'],
}
