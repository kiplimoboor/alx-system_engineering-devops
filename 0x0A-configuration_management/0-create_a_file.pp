# Creates a file in tmp/school with the parameters shown

file{
    '/tmp/school':
    ensure  => present,
    owner   => www-data,
    group   => www-data,
    mode    => '0744',
    content => 'I love Puppet',
}
