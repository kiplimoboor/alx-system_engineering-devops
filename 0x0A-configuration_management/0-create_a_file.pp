file{
    '/tmp/school':
    ensure => present,
    target => 'tmp/school',
    owner  => www-data,
    group  => www-data,
    mode   => '0744',
}
