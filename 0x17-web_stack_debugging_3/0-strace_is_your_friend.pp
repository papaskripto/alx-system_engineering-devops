# Fix Apache server internal error

exec { 'fix-apache-error' : 
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'}
