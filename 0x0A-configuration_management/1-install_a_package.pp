# Installs Flask version 2.1.0

package{
  'flask':
  ensure          => '2.1.0',
  provider        => pip3,
  install_options => ['--break-system-packages']
}