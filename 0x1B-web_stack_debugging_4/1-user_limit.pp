# increase file limit for a user

exec { 'increase-hard-limt':
        command => "/bin/sed -i /etc/security/limits.conf -e 's/hard nofile [0-9]\+/hard nofile 97816/g'"
}

exec { 'increase-soft-limit':
        command => "/bin/sed -i /etc/security/limits.conf -e 's/soft nofile [0-9]\+/soft nofile 97816/g'"
}
