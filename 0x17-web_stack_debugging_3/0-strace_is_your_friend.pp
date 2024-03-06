# Changes file extension name

exec {'correct_extension':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path    => ['/bin/', '/usr/bin/'],
}
