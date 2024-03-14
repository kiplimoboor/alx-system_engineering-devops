# Increase number of open files to be handled by nginx

exec {'increase nofile':
  command => 'sed -i s/15/4096/ /etc/default/nginx',
  path    => ['/bin/', '/usr/bin/'],
}


exec {'restart nginx':
  command => 'service nginx restart',
  path    => ['/bin/', '/usr/bin/'],
  require => Exec['increase nofile']
}

