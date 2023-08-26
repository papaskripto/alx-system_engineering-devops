# kills a process named killmenow

exec { 'kill':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow'
}
