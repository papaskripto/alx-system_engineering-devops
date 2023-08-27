# sets up client SSH configuration file so that
# you can connect to a server without typing a password
include stdlib
file_line { 'Turn off password authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '  PasswordAuthentication no'
}

file_line { 'Identity File':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '  IdentityFile ~/.ssh/school'
}
