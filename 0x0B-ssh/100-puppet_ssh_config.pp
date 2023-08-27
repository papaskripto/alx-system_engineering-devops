# set up client ssh 

file_line { 'PasswordAuthentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}

file_line { 'IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/shh_config',
  line   => 'IdentityFile ~/.ssh/school'
}
